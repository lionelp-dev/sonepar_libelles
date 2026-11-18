import { provideHttpClient } from '@angular/common/http';
import { HttpTestingController, provideHttpClientTesting } from '@angular/common/http/testing';
import { TestBed } from '@angular/core/testing';

import { AuditHabilitationsComponent } from './audit-habilitations.component';

describe('AuditHabilitationsComponent', () => {
  let http: HttpTestingController;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AuditHabilitationsComponent],
      providers: [provideHttpClient(), provideHttpClientTesting()],
    }).compileComponents();

    http = TestBed.inject(HttpTestingController);
  });

  afterEach(() => {
    http.verify();
  });

  it('generates an audit and adds it to the history', () => {
    const fixture = TestBed.createComponent(AuditHabilitationsComponent);
    fixture.detectChanges();
    http.expectOne('/api/audits/').flush([]);

    const button = fixture.nativeElement.querySelector('.primary-button') as HTMLButtonElement;
    button.click();
    const request = http.expectOne('/api/audits/');
    expect(request.request.method).toBe('POST');
    request.flush({
      id: 4,
      created_at: '2026-11-18T09:30:00Z',
      habilitations_count: 12,
    });
    fixture.detectChanges();

    expect(fixture.nativeElement.textContent).toContain('#4');
    expect(fixture.nativeElement.textContent).toContain('12');
  });

  it('displays an error when the audit history cannot be loaded', () => {
    const fixture = TestBed.createComponent(AuditHabilitationsComponent);
    fixture.detectChanges();
    http.expectOne('/api/audits/').flush('Erreur', { status: 500, statusText: 'Server Error' });
    fixture.detectChanges();

    expect(fixture.nativeElement.textContent).toContain('Impossible de charger l’historique des audits');
  });

  it('displays an error when audit generation fails', () => {
    const fixture = TestBed.createComponent(AuditHabilitationsComponent);
    fixture.detectChanges();
    http.expectOne('/api/audits/').flush([]);
    (fixture.nativeElement.querySelector('.primary-button') as HTMLButtonElement).click();
    http.expectOne('/api/audits/').flush('Erreur', { status: 500, statusText: 'Server Error' });
    fixture.detectChanges();

    expect(fixture.nativeElement.textContent).toContain('La génération de l’audit a échoué');
  });

  it('paginates the audit history by five items', () => {
    const fixture = TestBed.createComponent(AuditHabilitationsComponent);
    fixture.detectChanges();
    http.expectOne('/api/audits/').flush(
      Array.from({ length: 6 }, (_, index) => ({
        id: index + 1,
        created_at: '2026-11-18T09:30:00Z',
        habilitations_count: index + 1,
      })),
    );
    fixture.detectChanges();

    expect(fixture.nativeElement.textContent).not.toContain('#6');
    (fixture.nativeElement.querySelector('.pagination button:last-child') as HTMLButtonElement).click();
    fixture.detectChanges();

    expect(fixture.nativeElement.textContent).toContain('#6');
    expect(fixture.nativeElement.textContent).toContain('Page 2 sur 2');
  });
});
