import { DatePipe } from '@angular/common';
import { Component, OnInit, computed, inject, signal } from '@angular/core';
import { Router } from '@angular/router';

import { AuditApiService } from './audit-api.service';
import { AuditHabilitations } from './models';

@Component({
  selector: 'app-audit-habilitations',
  imports: [DatePipe],
  templateUrl: './audit-habilitations.component.html',
  styleUrl: './audit-habilitations.component.css',
})
export class AuditHabilitationsComponent implements OnInit {
  private readonly api = inject(AuditApiService);
  private readonly router = inject(Router, { optional: true });

  protected readonly audits = signal<AuditHabilitations[]>([]);
  protected readonly currentPage = signal(1);
  protected readonly pageSize = 10;
  protected readonly pageCount = computed(() =>
    Math.max(1, Math.ceil(this.audits().length / this.pageSize)),
  );
  protected readonly displayedAudits = computed(() => {
    const start = (this.currentPage() - 1) * this.pageSize;
    return this.audits().slice(start, start + this.pageSize);
  });
  protected readonly loading = signal(true);
  protected readonly generating = signal(false);
  protected readonly downloadingId = signal<number | null>(null);
  protected readonly loadError = signal(false);
  protected readonly actionError = signal<string | null>(null);

  ngOnInit(): void {
    this.load();
  }

  protected load(): void {
    this.loading.set(true);
    this.loadError.set(false);
    this.api.getAudits().subscribe({
      next: (audits) => {
        this.audits.set(audits);
        this.currentPage.set(1);
        this.loading.set(false);
      },
      error: () => {
        this.loading.set(false);
        this.loadError.set(true);
      },
    });
  }

  protected generate(): void {
    this.generating.set(true);
    this.actionError.set(null);
    this.api.generateAudit().subscribe({
      next: (audit) => {
        this.audits.update((audits) => [audit, ...audits]);
        this.currentPage.set(1);
        this.generating.set(false);
      },
      error: () => {
        this.generating.set(false);
        this.actionError.set('La génération de l’audit a échoué. Réessayez dans un instant.');
      },
    });
  }

  protected download(audit: AuditHabilitations): void {
    this.downloadingId.set(audit.id);
    this.actionError.set(null);
    this.api.getAuditExport(audit.id).subscribe({
      next: (file) => {
        const url = URL.createObjectURL(file);
        const link = document.createElement('a');
        link.href = url;
        link.download = 'audit_habilitations_' + audit.id + '.csv';
        link.click();
        URL.revokeObjectURL(url);
        this.downloadingId.set(null);
      },
      error: () => {
        this.downloadingId.set(null);
        this.actionError.set('Le téléchargement du CSV a échoué. Réessayez dans un instant.');
      },
    });
  }

  protected openAudit(auditId: number): void {
    void this.router?.navigate(['/audit-habilitations', auditId]);
  }

  protected previousPage(): void {
    this.currentPage.update((page) => Math.max(1, page - 1));
  }

  protected nextPage(): void {
    this.currentPage.update((page) => Math.min(this.pageCount(), page + 1));
  }
}
