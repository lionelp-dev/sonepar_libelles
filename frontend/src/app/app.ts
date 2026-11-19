import { Component, inject } from '@angular/core';
import { Router, RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';

@Component({
  imports: [RouterLink, RouterLinkActive, RouterOutlet],
  selector: 'app-root',
  styleUrl: './app.css',
  templateUrl: './app.html',
})
export class App {
  protected readonly router = inject(Router);
  protected readonly navigation = [
    { label: 'AuditHabilitations', path: '/audit-habilitations' },
    { label: 'LibellesFonctions', path: '/fonctions' },
    { label: 'LibellesNiveauxAcces', path: '/niveaux-acces' },
    { label: 'LibellesOptions', path: '/options' },
  ];

  protected readonly m3Navigation = [
    { label: 'MNS150MI_LstUsers', path: '/utilisateurs' },
    { label: 'MNS405MI_Lst', path: '/roles' },
    { label: 'MNS410MI_LstRolesByUser', path: '/affectations' },
    { label: 'SES400MI_LstAuthByRole', path: '/autorisations' },
  ];

  protected m3MenuOpen = true;

  protected toggleM3Menu(): void {
    this.m3MenuOpen = !this.m3MenuOpen;
  }

  protected isAuditDetail(): boolean {
    return /^\/audit-habilitations\/\d+\/?$/.test(this.router.url);
  }
}
