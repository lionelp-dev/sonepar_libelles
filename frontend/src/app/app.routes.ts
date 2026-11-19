import { Routes } from '@angular/router';

import { ModelTableComponent } from './model-table.component';

export const routes: Routes = [
  { path: 'catalogue-fonctions', component: ModelTableComponent, data: { model: 'MNS110MI_Lst' } },
  { path: 'utilisateurs', component: ModelTableComponent, data: { model: 'MNS150MI_LstUsers' } },
  { path: 'roles', component: ModelTableComponent, data: { model: 'MNS405MI_Lst' } },
  { path: 'affectations', component: ModelTableComponent, data: { model: 'MNS410MI_LstRolesByUser' } },
  { path: 'autorisations-role', component: ModelTableComponent, data: { model: 'SES400MI_LstAuthByRole' } },
  { path: 'autorisations-utilisateur', component: ModelTableComponent, data: { model: 'SES401_CMNPUS' } },
  { path: 'historique-habilitations', component: ModelTableComponent, data: { model: 'SES510MI_Lst' } },
  { path: 'fonctions', component: ModelTableComponent, data: { model: 'LibellesFonctions' } },
  { path: 'options', component: ModelTableComponent, data: { model: 'LibellesOptions' } },
  { path: '', pathMatch: 'full', redirectTo: 'utilisateurs' },
  { path: '**', redirectTo: 'utilisateurs' },
];
