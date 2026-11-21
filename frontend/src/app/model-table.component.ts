import { Component, OnInit, computed, inject, signal } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { M3DataApiService } from './m3-data-api.service';
import { tableConfigurations } from './table-configurations';
import { DatabaseTableName, TableConfiguration, TableRecord, TableColumn } from './tables';

@Component({
  selector: 'app-model-table',
  templateUrl: './model-table.component.html',
  styleUrl: './model-table.component.css',
})
export class ModelTableComponent implements OnInit {
  private readonly route = inject(ActivatedRoute);
  private readonly api = inject(M3DataApiService);

  protected configuration: TableConfiguration = tableConfigurations.ses510mi_lst;
  protected readonly rows = signal<TableRecord[]>([]);
  protected readonly currentPage = signal(1);
  protected readonly pageSize = 15;
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
    const tableName = this.route.snapshot.data['table'] as DatabaseTableName;
    this.configuration = tableConfigurations[tableName] ?? tableConfigurations.ses510mi_lst;
    this.load();
  }

  protected load(): void {
    this.loading.set(true);
    this.error.set(false);
    this.api.getCollection(this.configuration.apiPath).subscribe({
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

  protected displayValue(row: TableRecord, column: TableColumn): string | number | boolean {
    return row[column.key] ?? '—';
  }

  protected previousPage(): void {
    this.currentPage.update((page) => Math.max(1, page - 1));
  }

  protected nextPage(): void {
    this.currentPage.update((page) => Math.min(this.pageCount(), page + 1));
  }
}
