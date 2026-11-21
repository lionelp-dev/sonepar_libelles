import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable, map } from 'rxjs';

export type LabelKind = 'function' | 'option' | 'program' | 'role' | 'opCode';

interface FunctionLabelResponse { code_fonction: string; libelle: string | null; }
interface OptionLabelResponse { code_option: string; libelle: string | null; }
interface ProgramLabelResponse { code_programme: string; libelle: string | null; }
interface RoleLabelResponse { code_role: string; libelle: string | null; }
interface OpCodeLabelResponse { op_code: string; libelle: string | null; }

export interface LabelRecord { code: string; libelle: string | null; }

interface LabelPageResponse {
  count: number;
  page: number;
  page_size: number;
  results: (FunctionLabelResponse | OptionLabelResponse | ProgramLabelResponse | RoleLabelResponse | OpCodeLabelResponse)[];
}

export interface LabelPage {
  count: number;
  page: number;
  pageSize: number;
  results: LabelRecord[];
}

@Injectable({ providedIn: 'root' })
export class LabelApiService {
  private readonly http = inject(HttpClient);
  private readonly baseUrl = '/api/';

  list(kind: LabelKind, page: number, pageSize: number): Observable<LabelPage> {
    const params = new HttpParams()
      .set('page', page)
      .set('page_size', pageSize);
    return this.http.get<LabelPageResponse>(this.path(kind), { params }).pipe(
      map((response) => ({
        count: response.count,
        page: response.page,
        pageSize: response.page_size,
        results: response.results.map((row) => this.toRecord(kind, row)),
      })),
    );
  }

  update(kind: LabelKind, code: string, libelle: string): Observable<LabelRecord> {
    return this.http.put<FunctionLabelResponse | OptionLabelResponse | ProgramLabelResponse | RoleLabelResponse | OpCodeLabelResponse>(`${this.path(kind)}${encodeURIComponent(code)}/`, { libelle }).pipe(
      map((row) => this.toRecord(kind, row)),
    );
  }

  private path(kind: LabelKind): string {
    const paths: Record<LabelKind, string> = {
      function: 'function-labels/',
      option: 'option-labels/',
      program: 'program-labels/',
      role: 'role-labels/',
      opCode: 'op-code-labels/',
    };
    return `${this.baseUrl}${paths[kind]}`;
  }

  private toRecord(kind: LabelKind, row: FunctionLabelResponse | OptionLabelResponse | ProgramLabelResponse | RoleLabelResponse | OpCodeLabelResponse): LabelRecord {
    const code = {
      function: (row as FunctionLabelResponse).code_fonction,
      option: (row as OptionLabelResponse).code_option,
      program: (row as ProgramLabelResponse).code_programme,
      role: (row as RoleLabelResponse).code_role,
      opCode: (row as OpCodeLabelResponse).op_code,
    }[kind];
    return { code, libelle: row.libelle };
  }
}
