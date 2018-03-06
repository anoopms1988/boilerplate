import {Component, OnInit, OnDestroy} from '@angular/core';
import {SharedService} from 'app/shared/shared.service';
import {Subscription} from 'rxjs/Subscription';
import {Router} from '@angular/router';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit, OnDestroy {

  constructor() {

  }

  ngOnInit() {

  }

  ngOnDestroy(): void {
  }

}
