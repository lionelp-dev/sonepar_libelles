import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';

import { TableRecord } from './tables';

@Injectable({ providedIn: 'root' })
export class M3DataApiService {
  private readonly http = inject(HttpClient);
  private readonly baseUrl = '/api/';

  getCollection(path: string): Observable<TableRecord[]> {
    return this.http.get<TableRecord[]>(this.baseUrl + path);
  }
}
