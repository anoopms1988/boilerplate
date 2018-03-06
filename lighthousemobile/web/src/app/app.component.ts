import {Component, OnInit} from '@angular/core';
import {SharedService} from './shared/shared.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'app';
  public isLoggedIn = false;

  constructor(private sharedService: SharedService) {

  }

  ngOnInit(): void {
    this.hasToken();
  }

  hasToken() {
    this.sharedService.isLoggedInObserver.subscribe((res) => {
      if (res) {
        setTimeout(() => {
          this.isLoggedIn = res;
        });
      }
    });
  }
}
