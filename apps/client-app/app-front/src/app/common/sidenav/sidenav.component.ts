import { Component, OnInit } from '@angular/core';
import { INavigationData } from 'src/app/interfaces/nav-interface';
import { pages } from './pages';
import { TranslateService } from '@ngx-translate/core';

@Component({
  selector: 'app-sidenav',
  templateUrl: './sidenav.component.html',
  styleUrls: ['./sidenav.component.scss']
})
export class SidenavComponent implements OnInit {
  currentLanguage: string;
  collapsed: boolean = false;
  navPages: INavigationData[] = [];

  constructor(private translateService: TranslateService) {
    this.currentLanguage = translateService.currentLang;
  }

  ngOnInit(): void {
    if (this.currentLanguage === 'pl'){
      
      this.navPages = pages.map(({labelPl, ...rest}) => ({
        ...rest,
        currentLabel: labelPl
      }));

    }

    if (this.currentLanguage === 'eng'){

      this.navPages = pages.map(({labelEng, ...rest}) => ({
        ...rest,
        currentLabel: labelEng
      }));

    }
  }

  toggleCollapse(): void{
    this.collapsed = !this.collapsed;
  }

  closeSidenav(): void {
    this.collapsed = false; 
  }
}
