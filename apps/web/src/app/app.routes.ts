import { Routes } from '@angular/router';

import { ModelTableComponent } from './model-table.component';
import { LabelManagementComponent } from './label-management.component';

export const routes: Routes = [
  { path: 'ses510mi', component: ModelTableComponent, data: { table: 'ses510mi_lst' } },
  { path: 'libelles/fonctions', component: LabelManagementComponent, data: { kind: 'function' } },
  { path: 'libelles/programmes', component: LabelManagementComponent, data: { kind: 'program' } },
  { path: 'libelles/roles', component: LabelManagementComponent, data: { kind: 'role' } },
  { path: 'libelles/options', component: LabelManagementComponent, data: { kind: 'option' } },
  { path: 'libelles/op-codes', component: LabelManagementComponent, data: { kind: 'opCode' } },
  { path: 'libelles', pathMatch: 'full', redirectTo: 'libelles/fonctions' },
  { path: '', pathMatch: 'full', redirectTo: 'ses510mi' },
  { path: '**', redirectTo: 'ses510mi' },
];
