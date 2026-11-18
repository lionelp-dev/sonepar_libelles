import { provideHttpClient } from '@angular/common/http';
import { HttpTestingController, provideHttpClientTesting } from '@angular/common/http/testing';
import { TestBed } from '@angular/core/testing';

import { AuditApiService } from './audit-api.service';

describe('AuditApiService', () => {
  let service: AuditApiService;
  let http: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [provideHttpClient(), provideHttpClientTesting()],
    });
    service = TestBed.inject(AuditApiService);
    http = TestBed.inject(HttpTestingController);
  });

  afterEach(() => {
    http.verify();
  });

  it('requests the CSV for the selected audit only', () => {
    service.getAuditExport(42).subscribe();

    const request = http.expectOne('/api/audits/42/export/');
    expect(request.request.responseType).toBe('blob');
    request.flush(new Blob(['user_id'], { type: 'text/csv' }));
  });
});
