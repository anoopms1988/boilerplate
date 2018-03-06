import {Component, OnInit} from '@angular/core';
import {Router} from '@angular/router';
import {LoginService} from 'app/login/login.service';
import {SharedService} from '../shared/shared.service';
import {StorageService} from '../shared/storage.service';

export class LoginModel {
  username?: string;
  password?: string;
}

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent implements OnInit {
  public loginModel: LoginModel;

  constructor(public router: Router,
              public loginService: LoginService,
              public sharedService: SharedService,
              public storageService: StorageService) {
    this.loginModel = new LoginModel();
  }

  ngOnInit() {
    this.hasToken();
  }

  login() {
    this.loginService.login(this.loginModel).subscribe((res) => {
      if (res.token) {
        this.storageService.set('access_token', res.token);
        this.router.navigate(['dashboard']);
        this.sharedService.setLoggedInSubject(true);
      }
    });
  }

  hasToken() {
    const hasToken = this.sharedService.isLoggedIn();
    if (!hasToken) {
      this.sharedService.setLoggedInSubject(hasToken);
    }
  }

}
