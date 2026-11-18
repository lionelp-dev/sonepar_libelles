import { provideHttpClient } from '@angular/common/http';
import { HttpTestingController, provideHttpClientTesting } from '@angular/common/http/testing';
import { TestBed } from '@angular/core/testing';
import { ActivatedRoute } from '@angular/router';

import { ModelTableComponent } from './model-table.component';

describe('ModelTableComponent', () => {
  let http: HttpTestingController;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ModelTableComponent],
      providers: [
        provideHttpClient(),
        provideHttpClientTesting(),
        {
          provide: ActivatedRoute,
          useValue: { snapshot: { data: { model: 'MNS150MI_LstUsers' } } },
        },
      ],
    }).compileComponents();

    http = TestBed.inject(HttpTestingController);
  });

  afterEach(() => {
    http.verify();
  });

  it('loads and displays a model collection', () => {
    const fixture = TestBed.createComponent(ModelTableComponent);
    fixture.detectChanges();
    http.expectOne('/api/users/').flush([
      { user_id: 'DUPONTJ', nom_complet: 'Jeanne Dupont', statut: 'ACTIF' },
    ]);
    fixture.detectChanges();

    expect(fixture.nativeElement.textContent).toContain('Jeanne Dupont');
    expect(fixture.nativeElement.textContent).toContain('1 enregistrement');
  });

  it('displays an error when a model collection cannot be loaded', () => {
    const fixture = TestBed.createComponent(ModelTableComponent);
    fixture.detectChanges();
    http.expectOne('/api/users/').flush('Erreur', { status: 500, statusText: 'Server Error' });
    fixture.detectChanges();

    expect(fixture.nativeElement.textContent).toContain('Impossible de charger ces données');
  });

  it('paginates model collections by five items', () => {
    const fixture = TestBed.createComponent(ModelTableComponent);
    fixture.detectChanges();
    http.expectOne('/api/users/').flush(
      Array.from({ length: 6 }, (_, index) => ({
        user_id: 'USER' + (index + 1),
        nom_complet: 'Utilisateur ' + (index + 1),
        statut: 'ACTIF',
      })),
    );
    fixture.detectChanges();

    expect(fixture.nativeElement.textContent).not.toContain('Utilisateur 6');
    (fixture.nativeElement.querySelector('.pagination button:last-child') as HTMLButtonElement).click();
    fixture.detectChanges();

    expect(fixture.nativeElement.textContent).toContain('Utilisateur 6');
    expect(fixture.nativeElement.textContent).toContain('Page 2 sur 2');
  });
});
