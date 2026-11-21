import { Component, OnInit, computed, inject, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';

import { LabelApiService, LabelKind, LabelRecord } from './label-api.service';

@Component({
  selector: 'app-label-management',
  imports: [FormsModule],
  templateUrl: './label-management.component.html',
  styleUrl: './label-management.component.css',
})
export class LabelManagementComponent implements OnInit {
  private readonly api = inject(LabelApiService);
  private readonly route = inject(ActivatedRoute);

  protected readonly activeKind = signal<LabelKind>('function');
  protected readonly rows = signal<LabelRecord[]>([]);
  protected readonly currentPage = signal(1);
  protected readonly totalCount = signal(0);
  protected readonly pageSize = 15;
  protected readonly pageCount = computed(() =>
    Math.max(1, Math.ceil(this.totalCount() / this.pageSize)),
  );
  protected readonly loading = signal(true);
  protected readonly error = signal(false);
  protected readonly editingCode = signal<string | null>(null);
  protected draftLabel = '';
  protected formError = '';

  ngOnInit(): void {
    this.activeKind.set(this.route.snapshot.data['kind'] as LabelKind);
    this.load();
  }

  protected codeField(): string {
    const fields: Record<LabelKind, string> = {
      function: 'Code fonction',
      option: 'Code option',
      program: 'Code programme',
      role: 'Code rôle',
      opCode: 'op_code',
    };
    return fields[this.activeKind()];
  }

  protected pageTitle(): string {
    const titles: Record<LabelKind, string> = {
      function: 'Libellés des fonctions',
      option: 'Libellés des options',
      program: 'Libellés des programmes',
      role: 'Libellés des rôles',
      opCode: 'Libellés des codes opération',
    };
    return titles[this.activeKind()];
  }

  protected pageDescription(): string {
    const descriptions: Record<LabelKind, string> = {
      function: 'Associez un libellé aux fonctions M3 présentes dans le journal d’audit.',
      option: 'Associez un libellé aux options de droits présentes dans le journal d’audit.',
      program: 'Associez un libellé aux programmes M3 présents dans le journal d’audit.',
      role: 'Associez un libellé aux rôles M3 présents dans le journal d’audit.',
      opCode: 'Associez un libellé aux codes opération présents dans le journal d’audit.',
    };
    return descriptions[this.activeKind()];
  }

  protected startEdit(row: LabelRecord): void {
    this.editingCode.set(row.code);
    this.draftLabel = row.libelle ?? '';
    this.formError = '';
  }

  protected cancelEdit(): void {
    this.editingCode.set(null);
    this.draftLabel = '';
    this.formError = '';
  }

  protected clearFormError(): void {
    this.formError = '';
  }

  protected save(row: LabelRecord): void {
    const libelle = this.draftLabel.trim();
    if (!libelle) {
      this.formError = 'Le libellé est obligatoire.';
      return;
    }
    this.api.update(this.activeKind(), row.code, libelle).subscribe({
      next: (updated) => {
        this.rows.update((rows) => rows.map((item) => item.code === updated.code ? updated : item));
        this.cancelEdit();
      },
      error: () => this.formError = 'La modification du libellé a échoué.',
    });
  }

  protected load(): void {
    this.loading.set(true);
    this.error.set(false);
    this.api.list(this.activeKind(), this.currentPage(), this.pageSize).subscribe({
      next: (response) => {
        this.rows.set(response.results);
        this.totalCount.set(response.count);
        this.currentPage.set(response.page);
        this.loading.set(false);
      },
      error: () => {
        this.error.set(true);
        this.loading.set(false);
      },
    });
  }

  protected previousPage(): void {
    this.currentPage.update((page) => Math.max(1, page - 1));
    this.load();
  }

  protected nextPage(): void {
    this.currentPage.update((page) => Math.min(this.pageCount(), page + 1));
    this.load();
  }
}
