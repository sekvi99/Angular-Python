import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms'; // Import Validators and FormGroup
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
  };

  loginForm: FormGroup; // Use FormGroup

  constructor(
    private userService: UserService,
    private authEventService: AuthEventService,
    private router: Router,
    private formBuilder: FormBuilder // Inject the FormBuilder
  ) {
    // Initialize the login form with validators
    this.loginForm = this.formBuilder.group({
      username: ['', [Validators.required]],
      password: ['', [Validators.required]]
    });
  }

  ngOnInit(): void {
    this.authEventService.logout();
  }

  public onLogin(): void {
    // Check if the form is valid before submitting
    if (this.loginForm.valid) {
      // Assign form values to the authRequest object
      this.authRequest['username'] = this.loginForm.get('username')?.value;
      this.authRequest['password'] = this.loginForm.get('password')?.value;

      this.userService.authenticate(this.authRequest).subscribe(
        (response) => {
          if (response) {
            this.authEventService.login();
            this.router.navigateByUrl('/home');
          } else {
            this.isErrorInLogin = true;
          }
        },
        (error) => {
          this.isErrorInLogin = true;
        }
      );
    }
  }
  
}