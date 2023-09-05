import { Component, NgModule, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { RegisterUserService } from 'src/app/services/register-service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})

export class RegisterComponent implements OnInit {

  registrationForm!: FormGroup;
  registrationStatusMessage: string | null = null; 

  constructor(private formBuilder: FormBuilder,
              private registerUserService: RegisterUserService,
              private router: Router) { }

  ngOnInit(): void {
    this.registrationForm = this.formBuilder.group({
      username: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]],
      connected_mail: ['', Validators.required]
    });
  }

  onSubmit() {
    if (this.registrationForm.valid) {
      const formData = this.registrationForm.value;
      this.registerUserService.register(formData)
        .subscribe(
          (response) => {
            this.registrationStatusMessage = 'Registration successful';
            console.log(response);
          },
          (error) => {
            this.registrationStatusMessage = 'Registration failed';
            console.error(error);
          }
        );
    } else {
      console.log(this.registrationForm.valid);
    }
  }

}
