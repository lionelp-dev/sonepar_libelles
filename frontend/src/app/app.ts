import { Component } from '@angular/core';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';

@Component({
  imports: [RouterLink, RouterLinkActive, RouterOutlet],
  selector: 'app-root',
  styleUrl: './app.css',
  templateUrl: './app.html',
})
export class App {
  protected readonly navigation = [
    { label: 'AuditHabilitations', path: '/audit-habilitations' },
    { label: 'Habilitations', path: '/lignes-habilitations' },
    { label: 'MNS150MI_LstUsers', path: '/utilisateurs' },
    { label: 'MNS405MI_Lst', path: '/roles' },
    { label: 'MNS410MI_LstRolesByUser', path: '/affectations' },
    { label: 'SES400MI_LstAuthByRole', path: '/autorisations' },
    { label: 'LibellesFonctions', path: '/fonctions' },
    { label: 'LibellesNiveauxAcces', path: '/niveaux-acces' },
    { label: 'LibellesOptions', path: '/options' },
  ];
}
