import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
    providedIn: 'root'
})
export class AuthEventService {
    private loggedInSubject: BehaviorSubject<boolean> = new BehaviorSubject<boolean>(false);

    constructor() { }

    isLoggedIn(): Observable<boolean> {
        return this.loggedInSubject.asObservable();
    }

    login() {
        this.loggedInSubject.next(true);
    }

    logout() {
        this.loggedInSubject.next(false);
    }
}