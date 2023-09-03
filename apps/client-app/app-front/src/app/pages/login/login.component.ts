import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/services/user-service';
import { Router } from '@angular/router';
import { AuthEventService } from 'src/events/auth-event-service';
import { AuthenticationDto } from 'src/app/models/auth/authentication-dto';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  isErrorInLogin: boolean = false;
  authRequest: AuthenticationDto = {
    username: '',
    password: ''
  }

  constructor(private userService: UserService, private authEventService: AuthEventService, private router: Router) { }

  ngOnInit(): void {
      this.authEventService.logout();
  }

  public onLogin(): void {
    this.userService.authenticate(this.authRequest).subscribe(response => {
      if (response) {
        this.authEventService.login();
        this.router.navigateByUrl('/home');
      } else {
        this.isErrorInLogin = true;
      }
    }, error => {
      this.isErrorInLogin = true;
    });
  }
  

}
