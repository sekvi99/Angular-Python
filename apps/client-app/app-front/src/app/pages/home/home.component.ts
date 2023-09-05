import { Component } from '@angular/core';
import { YoutubeStatsService } from 'src/app/services/youtube.stats-service';
import { YouTubeStatsDto } from 'src/app/models/yt-stats/yt.stats-dto';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent {

  videoUrl: string = '';
  stats!: YouTubeStatsDto;
  videoForm!: FormGroup;

  constructor(
    private youTubeStatsService: YoutubeStatsService,
    private formBuilder: FormBuilder // Inject the FormBuilder
  ) {
    this.videoForm = this.formBuilder.group({
      videoUrl: ['', [Validators.required]]
    });
  }

  onVideoSubmit(): void {
    console.log(this.videoForm.value.videoUrl);

    if (this.videoForm.valid) {
      this.youTubeStatsService.getStats(this.videoForm.value.videoUrl).subscribe(
        res => {
          this.stats = res;
          console.log(this.stats);
        },
        error => {
          console.log('Error', error);
        }
      );
    } else {
      console.log('Form is invalid.');
    }
  }

}
