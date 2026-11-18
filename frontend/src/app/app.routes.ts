import { Routes } from '@angular/router';

import { AuditHabilitationsComponent } from './audit-habilitations.component';
import { ModelTableComponent } from './model-table.component';

export const routes: Routes = [
  { path: 'audit-habilitations', component: AuditHabilitationsComponent },
  { path: 'utilisateurs', component: ModelTableComponent, data: { model: 'MNS150MI_LstUsers' } },
  { path: 'roles', component: ModelTableComponent, data: { model: 'MNS405MI_Lst' } },
  { path: 'affectations', component: ModelTableComponent, data: { model: 'MNS410MI_LstRolesByUser' } },
  { path: 'autorisations', component: ModelTableComponent, data: { model: 'SES400MI_LstAuthByRole' } },
  { path: 'fonctions', component: ModelTableComponent, data: { model: 'LibellesFonctions' } },
  { path: 'niveaux-acces', component: ModelTableComponent, data: { model: 'LibellesNiveauxAcces' } },
  { path: 'options', component: ModelTableComponent, data: { model: 'LibellesOptions' } },
  { path: 'lignes-habilitations', component: ModelTableComponent, data: { model: 'Habilitations' } },
  { path: '', pathMatch: 'full', redirectTo: 'audit-habilitations' },
  { path: '**', redirectTo: 'audit-habilitations' },
];
