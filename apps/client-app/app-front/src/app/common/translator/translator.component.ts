import { Component, OnInit } from '@angular/core';
import { TranslateService } from '@ngx-translate/core';

@Component({
  selector: 'app-translator',
  templateUrl: './translator.component.html',
  styleUrls: ['./translator.component.scss']
})
export class TranslatorComponent implements OnInit {
  currentLanguage: string;


  constructor(private translateService: TranslateService) {
    this.currentLanguage = 'pl';
  }

  ngOnInit(): void {
      this.toggleLanguage();
  }

  toggleLanguage() {
    this.currentLanguage = this.currentLanguage === 'en' ? 'pl' : 'en'; 
    this.translateService.use(this.currentLanguage);
  }
}
