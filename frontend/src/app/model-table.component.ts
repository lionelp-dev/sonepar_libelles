import { Component, OnInit, computed, inject, signal } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { M3DataApiService } from './m3-data-api.service';
import { modelDefinitions, ReadOnlyModelName } from './model-definitions';
import { ModelDefinition, ModelRecord, ModelTableColumn } from './models';

@Component({
  selector: 'app-model-table',
  templateUrl: './model-table.component.html',
  styleUrl: './model-table.component.css',
})
export class ModelTableComponent implements OnInit {
  private readonly route = inject(ActivatedRoute);
  private readonly api = inject(M3DataApiService);

  protected definition: ModelDefinition = modelDefinitions.MNS150MI_LstUsers;
  protected readonly rows = signal<ModelRecord[]>([]);
  protected readonly currentPage = signal(1);
  protected readonly pageSize = 10;
  protected readonly pageCount = computed(() =>
    Math.max(1, Math.ceil(this.rows().length / this.pageSize)),
  );
  protected readonly displayedRows = computed(() => {
    const start = (this.currentPage() - 1) * this.pageSize;
    return this.rows().slice(start, start + this.pageSize);
  });
  protected readonly loading = signal(true);
  protected readonly error = signal(false);

  ngOnInit(): void {
    const modelName = this.route.snapshot.data['model'] as ReadOnlyModelName;
    this.definition = modelDefinitions[modelName] ?? modelDefinitions.MNS150MI_LstUsers;
    this.load();
  }

  protected load(): void {
    this.loading.set(true);
    this.error.set(false);
    this.api.getCollection(this.definition.apiPath).subscribe({
      next: (rows) => {
        this.rows.set(rows);
        this.currentPage.set(1);
        this.loading.set(false);
      },
      error: () => {
        this.loading.set(false);
        this.error.set(true);
      },
    });
  }

  protected displayValue(row: ModelRecord, column: ModelTableColumn): string | number | boolean {
    return row[column.key] ?? '—';
  }

  protected previousPage(): void {
    this.currentPage.update((page) => Math.max(1, page - 1));
  }

  protected nextPage(): void {
    this.currentPage.update((page) => Math.min(this.pageCount(), page + 1));
  }
}
