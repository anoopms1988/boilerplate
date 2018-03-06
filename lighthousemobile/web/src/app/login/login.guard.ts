import {Injectable} from '@angular/core';
import {CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, Router} from '@angular/router';
import {Observable} from 'rxjs/Observable';
import {SharedService} from '../shared/shared.service';

@Injectable()
export class LoginGuard implements CanActivate {
  constructor(private router: Router,
              private sharedService: SharedService) {

  }

  canActivate(next: ActivatedRouteSnapshot,
              state: RouterStateSnapshot): Observable<boolean> | Promise<boolean> | boolean {
    if (this.sharedService.isLoggedIn()) {
      this.router.navigate(['dashboard']);
    } else {
      return true;
    }
  }
}
