import { Injectable } from '@angular/core';
import { Router, CanActivate } from '@angular/router';
import { UserService } from 'src/app/services/user-service';

@Injectable({
  providedIn: 'root'
})

export class AuthGuard implements CanActivate {
  constructor(public auth: UserService, public router: Router) {}
  canActivate(): boolean {
    if (!this.auth.isLogged()) {
      this.router.navigate(['login']);
      return false;
    }
    return true;
  }
}