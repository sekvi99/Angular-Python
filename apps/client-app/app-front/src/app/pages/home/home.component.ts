import { Component } from '@angular/core';
import { YoutubeStatsService } from 'src/app/services/youtube.stats-service';
import { YouTubeStatsDto } from 'src/app/models/yt-stats/yt.stats-dto';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent {

  videoUrl: string = '';
  stats!: YouTubeStatsDto;

  constructor(private youTubeStatsService: YoutubeStatsService) { }

  onVideoSubmit(): void{
    console.log(this.videoUrl);
    if (this.videoUrl.length > 0) {
      this.youTubeStatsService.getStats(this.videoUrl).subscribe(
        res => {
          this.stats = res;
          console.log(this.stats);
        },
        error => {
          console.log('Error', error);
        }
      );

    }else {
      console.log(`Can not process this url: ${this.videoUrl}`);
    }
  }

}
