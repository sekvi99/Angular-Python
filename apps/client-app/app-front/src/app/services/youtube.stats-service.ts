import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { UserService } from "./user-service";
import { Observable } from "rxjs";
import { YouTubeStatsDto } from "../models/yt-stats/yt.stats-dto";
import { environment } from "src/environments/environment";
import { HttpParams } from "@angular/common/http";

@Injectable({
    providedIn: 'root'
})

export class YoutubeStatsService {
    constructor(private httpClient: HttpClient, private userService: UserService) {}

    getStats(videoUrl: string): Observable<YouTubeStatsDto> {
        let params = new HttpParams()
            .set('url', videoUrl)
            .set('token', this.userService.getToken());

        return this.httpClient.get<YouTubeStatsDto>(`${environment.url}/youtube-stats`, {params: params});
    }
}