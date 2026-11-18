import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';

import { AuditHabilitations, ModelRecord } from './models';

@Injectable({ providedIn: 'root' })
export class AuditApiService {
  private readonly http = inject(HttpClient);
  private readonly baseUrl = '/api/';

  getCollection(path: string): Observable<ModelRecord[]> {
    return this.http.get<ModelRecord[]>(this.baseUrl + path);
  }

  getAudits(): Observable<AuditHabilitations[]> {
    return this.http.get<AuditHabilitations[]>(this.baseUrl + 'audits/');
  }

  generateAudit(): Observable<AuditHabilitations> {
    return this.http.post<AuditHabilitations>(this.baseUrl + 'audits/', {});
  }

  getAuditExport(auditId: number): Observable<Blob> {
    return this.http.get(this.baseUrl + 'audits/' + auditId + '/export/', {
      responseType: 'blob',
    });
  }
}
