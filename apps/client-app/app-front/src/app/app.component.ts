import { Component } from '@angular/core';
import { TranslateService } from '@ngx-translate/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'app-front';

  supportedLanguages: string[] = ['pl', 'en'];
  currentLanguage: string;

  constructor(private translateService: TranslateService) {
    this.translateService.addLangs(this.supportedLanguages);
    this.translateService.setDefaultLang(this.supportedLanguages[0]); // pl
    this.translateService.use('pl');
    this.currentLanguage = 'pl';
  }

}
