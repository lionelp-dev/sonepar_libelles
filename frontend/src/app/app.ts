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
    { label: 'MNS110MI_Lst', path: '/catalogue-fonctions' },
    { label: 'MNS150MI_LstUsers', path: '/utilisateurs' },
    { label: 'MNS405MI_Lst', path: '/roles' },
    { label: 'MNS410MI_LstRolesByUser', path: '/affectations' },
    { label: 'SES400MI_LstAuthByRole', path: '/autorisations-role' },
    { label: 'SES401_CMNPUS', path: '/autorisations-utilisateur' },
    { label: 'SES510MI_Lst', path: '/historique-habilitations' },
    { label: 'LibellesFonctions', path: '/fonctions' },
    { label: 'LibellesOptions', path: '/options' },
  ];

  protected m3MenuOpen = true;

  protected toggleM3Menu(): void {
    this.m3MenuOpen = !this.m3MenuOpen;
  }
}
