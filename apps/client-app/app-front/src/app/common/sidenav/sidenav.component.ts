import { Component } from '@angular/core';
import { INavigationData } from 'src/app/interfaces/nav-interface';
import { pages } from './pages';
import { TranslateService } from '@ngx-translate/core';

@Component({
  selector: 'app-sidenav',
  templateUrl: './sidenav.component.html',
  styleUrls: ['./sidenav.component.scss']
})
export class SidenavComponent {
  collapsed: boolean = false;
  navPages: INavigationData[] = [];
  currentLang: string;

  constructor(private translateService: TranslateService) {
    this.currentLang = this.translateService.currentLang;
    console.log(this.currentLang);
    this.navPages = pages;
  }

  toggleCollapse(): void {
    this.collapsed = !this.collapsed;
  }

  closeSidenav(): void {
    this.collapsed = false;
  }
}
