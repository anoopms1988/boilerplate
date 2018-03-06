import {Injectable} from '@angular/core';
import {CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, Router} from '@angular/router';
import {Observable} from 'rxjs/Observable';
import {SharedService} from './shared.service';

@Injectable()
export class AuthGuard implements CanActivate {
  constructor(private router: Router,
              private sharedService: SharedService) {

  }

  canActivate(next: ActivatedRouteSnapshot,
              state: RouterStateSnapshot): Observable<boolean> | Promise<boolean> | boolean {
    if (this.sharedService.isLoggedIn()) {
      return true;
    } else {
      this.router.navigate(['login']);
    }
  }
}
