import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';

import { ModelRecord } from './models';

@Injectable({ providedIn: 'root' })
export class M3DataApiService {
  private readonly http = inject(HttpClient);
  private readonly baseUrl = '/api/';

  getCollection(path: string): Observable<ModelRecord[]> {
    return this.http.get<ModelRecord[]>(this.baseUrl + path);
  }
}
