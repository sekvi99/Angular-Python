import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/services/user-service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-logout',
  templateUrl: './logout.component.html',
  styleUrls: ['./logout.component.scss']
})
export class LogoutComponent implements OnInit {

  constructor(private userService: UserService,
              private router: Router) { }

  ngOnInit(): void {
      this.logoutUser();
  }

  logoutUser(): void{
    this.userService.logout();
    this.router.navigateByUrl('login');
  }

}
