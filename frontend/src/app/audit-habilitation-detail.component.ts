import { DatePipe } from '@angular/common';
import { Component, OnInit, computed, inject, signal } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { forkJoin } from 'rxjs';

import { AuditApiService } from './audit-api.service';
import { AuditHabilitations, Habilitation } from './models';

@Component({
  selector: 'app-audit-habilitation-detail',
  imports: [DatePipe],
  templateUrl: './audit-habilitation-detail.component.html',
  styleUrl: './audit-habilitation-detail.component.css',
})
export class AuditHabilitationDetailComponent implements OnInit {
  private readonly api = inject(AuditApiService);
  private readonly route = inject(ActivatedRoute);

  protected readonly audit = signal<AuditHabilitations | null>(null);
  protected readonly habilitations = signal<Habilitation[]>([]);
  protected readonly currentPage = signal(1);
  protected readonly pageSize = 10;
  protected readonly pageCount = computed(() =>
    Math.max(1, Math.ceil(this.habilitations().length / this.pageSize)),
  );
  protected readonly displayedHabilitations = computed(() => {
    const start = (this.currentPage() - 1) * this.pageSize;
    return this.habilitations().slice(start, start + this.pageSize);
  });
  protected readonly loading = signal(true);
  protected readonly loadError = signal(false);
  protected readonly downloading = signal(false);
  protected readonly actionError = signal<string | null>(null);

  private auditId: number | null = null;

  ngOnInit(): void {
    const auditId = Number(this.route.snapshot.paramMap.get('auditId'));
    this.auditId = Number.isInteger(auditId) && auditId > 0 ? auditId : null;
    this.load();
  }

  protected load(): void {
    if (this.auditId === null) {
      this.loading.set(false);
      this.loadError.set(true);
      return;
    }

    const auditId = this.auditId;
    this.loading.set(true);
    this.loadError.set(false);
    forkJoin({
      audit: this.api.getAudit(auditId),
      habilitations: this.api.getAuditHabilitations(auditId),
    }).subscribe({
      next: ({ audit, habilitations }) => {
        this.audit.set(audit);
        this.habilitations.set(habilitations);
        this.currentPage.set(1);
        this.loading.set(false);
      },
      error: () => {
        this.loading.set(false);
        this.loadError.set(true);
      },
    });
  }

  protected download(): void {
    if (this.auditId === null) {
      return;
    }

    this.downloading.set(true);
    this.actionError.set(null);
    this.api.getAuditExport(this.auditId).subscribe({
      next: (file) => {
        const url = URL.createObjectURL(file);
        const link = document.createElement('a');
        link.href = url;
        link.download = 'audit_habilitations_' + this.auditId + '.csv';
        link.click();
        URL.revokeObjectURL(url);
        this.downloading.set(false);
      },
      error: () => {
        this.downloading.set(false);
        this.actionError.set('Le téléchargement du CSV a échoué. Réessayez dans un instant.');
      },
    });
  }

  protected previousPage(): void {
    this.currentPage.update((page) => Math.max(1, page - 1));
  }

  protected nextPage(): void {
    this.currentPage.update((page) => Math.min(this.pageCount(), page + 1));
  }
}
