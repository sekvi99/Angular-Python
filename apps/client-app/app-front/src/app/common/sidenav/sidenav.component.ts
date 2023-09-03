import { Component, OnInit } from '@angular/core';
import { INavigationData } from 'src/app/interfaces/nav-interface';
import { pages } from './pages';
import { TranslateService } from '@ngx-translate/core';
import { UserService } from 'src/app/services/user-service';
import { AuthEventService } from 'src/events/auth-event-service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-sidenav',
  templateUrl: './sidenav.component.html',
  styleUrls: ['./sidenav.component.scss']
})
export class SidenavComponent implements OnInit {
  collapsed: boolean = false;
  navPages: INavigationData[] = [];
  currentLang: string;
  private loggedInSubscription: Subscription = Subscription.EMPTY;

  constructor(private translateService: TranslateService,
              private userService: UserService,
              private authEventService: AuthEventService) {
    this.currentLang = this.translateService.currentLang;
    this.navPages = pages;
  }

  ngOnInit(): void {
    this.loggedInSubscription = this.authEventService.isLoggedIn()
    .subscribe(loggedIn => {
      this.setLoginLogoutPage(loggedIn);
    });

  this.setLoginLogoutPage(this.userService.isLogged());
  }

  ngOnDestroy(): void {
    this.loggedInSubscription.unsubscribe();
  }

  private setLoginLogoutPage(loggedIn: boolean) {
    if (loggedIn) {
      this.navPages = pages.filter(page => page.routeLink !== 'login' && page.routeLink !== 'register');
    } else {
      this.navPages = pages.filter(page => page.routeLink === 'register' || page.routeLink === 'login');
    }
  }

  toggleCollapse(): void {
    this.collapsed = !this.collapsed;
  }

  closeSidenav(): void {
    this.collapsed = false;
  }
}
