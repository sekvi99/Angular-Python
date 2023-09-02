import { Component } from '@angular/core';
import { socials } from './socials';
import { ISocialLinks } from 'src/app/interfaces/social-interface';
import { pages } from '../sidenav/pages';
import { INavigationData } from 'src/app/interfaces/nav-interface';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.scss']
})
export class FooterComponent {

  socials: ISocialLinks[];
  footerPages: INavigationData[];

  constructor() {
    this.socials = socials;
    this.footerPages = pages.filter((page) => page.routeLink === 'home' || page.routeLink === 'about');
  }

}
