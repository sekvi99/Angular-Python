import { HttpClient } from "@angular/common/http";
import { environment } from "src/environments/environment";
import { HttpHeaders } from "@angular/common/http";
import { HttpParams } from "@angular/common/http";
import { IRegisterResponse } from "../models/register/register.response-dto";
import { Injectable } from "@angular/core";
import { UserService } from "./user-service";
import { Observable } from "rxjs";
import { tokenBack } from "src/token/token";

@Injectable({
    providedIn: 'root'
})

export class RegisterUserService {

    constructor(private httpClient: HttpClient) { }

    register(formData: any): Observable<IRegisterResponse> {
        let headers = new HttpHeaders()
            .set('accept', 'application/json')
            .set(tokenBack.tokenName, tokenBack.tokenValue)

        return this.httpClient.post<IRegisterResponse>(`${environment.url}/create-user`, formData,{headers: headers});
    }

}