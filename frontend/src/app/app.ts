import { Component } from '@angular/core';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';

@Component({
  imports: [RouterLink, RouterLinkActive, RouterOutlet],
  selector: 'app-root',
  styleUrl: './app.css',
  templateUrl: './app.html',
})
export class App {
  protected readonly m3Navigation = [
    { label: 'ses510mi_lst', path: '/ses510mi' },
  ];

  protected m3MenuOpen = true;
  protected labelMenuOpen = true;

  protected toggleM3Menu(): void {
    this.m3MenuOpen = !this.m3MenuOpen;
  }

  protected toggleLabelMenu(): void {
    this.labelMenuOpen = !this.labelMenuOpen;
  }
}
