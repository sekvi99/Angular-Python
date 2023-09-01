import { Component, OnInit } from '@angular/core';
import { socials } from './socials';
import { ISocialLinks } from 'src/app/interfaces/social-interface';
import { pages } from '../sidenav/pages';
import { TranslateService } from '@ngx-translate/core';

type FooterNav = {
    url?: string | null | undefined;
    name?: string | undefined;
}

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.scss']
})
export class FooterComponent implements OnInit {

  socials: ISocialLinks[] = [];
  nav: FooterNav[] = [];

  constructor(private translateService: TranslateService) {}

  ngOnInit(): void {
      this.socials = socials;
      let filteredPages = pages.filter((page) => page.routeLink === 'home' || page.routeLink === 'about');
      this.nav= filteredPages.map(page => ({ 
          url: page.routeLink,
          name: this.translateService.currentLang === 'pl' ? page.labelPl : page.labelEng
        }))
  }

}
