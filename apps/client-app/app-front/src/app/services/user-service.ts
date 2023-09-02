import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { map, catchError } from 'rxjs/operators';
import { environment } from 'src/environments/environment';
import { AuthenticationDto } from '../models/auth/authentication-dto';
import { AuthenticationResponseDto } from '../models/auth/authentication-response-dto';

@Injectable({
    providedIn: 'root'
})

export class UserService {
    jwtToken: string = 'jwt';

    constructor(private httpClient: HttpClient) { }

    // authenticate(authData: AuthenticationDto): Observable<boolean> {


    // }

    logout() {
        localStorage.removeItem(this.jwtToken);
    }

    isLogged(): boolean {
        return !!localStorage.getItem(this.jwtToken);
    }

    getToken(): string {
        return localStorage.getItem(this.jwtToken)!;
    }

    private storeToken(token: string) {
        localStorage.setItem(this.jwtToken, token);
    }
}
