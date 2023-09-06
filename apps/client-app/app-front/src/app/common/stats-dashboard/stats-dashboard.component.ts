import { Component, OnInit, Input, ViewChild, ElementRef } from '@angular/core';
import { YouTubeStatsDto } from 'src/app/models/yt-stats/yt.stats-dto';
import { SimpleChanges } from '@angular/core';
import Chart from 'chart.js/auto';

@Component({
  selector: 'app-stats-dashboard',
  templateUrl: './stats-dashboard.component.html',
  styleUrls: ['./stats-dashboard.component.scss']
})
export class StatsDashboardComponent implements OnInit {

  @Input() data!: YouTubeStatsDto;

  @ViewChild('statsChart') private chartRef!: ElementRef; // Declare chartRef as ElementRef

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['data'] && this.data) {
      console.log('Data changed:', this.data);
      this.createSummaryGraph();
    }
  }

  ngOnInit(): void {
    console.log('StatsDashboardComponent initialized');
  }

  createSummaryGraph(): void {
    if (!this.data || !this.chartRef) {
      return;
    }
    console.log('hello');
    const ctx = this.chartRef.nativeElement.getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Likes', 'Favorites', 'Comments', 'Views'],
        datasets: [{
          label: 'YouTube Stats',
          data: [this.data.likes, this.data.favourites, this.data.comments, this.data.views],
          backgroundColor: [
            'rgba(75, 192, 192, 0.6)', // Views
            'rgba(255, 99, 132, 0.6)', // Likes
            'rgba(255, 205, 86, 0.6)', // Favorites
            'rgba(54, 162, 235, 0.6)'  // Comments
          ],
          borderColor: [
            'rgba(75, 192, 192, 1)', // Views
            'rgba(255, 99, 132, 1)', // Likes
            'rgba(255, 205, 86, 1)', // Favorites
            'rgba(54, 162, 235, 1)'  // Comments
          ],
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
  }
  

}
