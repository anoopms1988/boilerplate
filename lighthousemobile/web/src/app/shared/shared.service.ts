import {Injectable} from '@angular/core';
import {BehaviorSubject} from 'rxjs/BehaviorSubject';
import {StorageService} from './storage.service';

@Injectable()
export class SharedService {

  private loggedInSubject: BehaviorSubject<any>;
  public isLoggedInObserver: any;

  constructor(private storageService: StorageService) {
    this.loggedInSubject = new BehaviorSubject(this.isLoggedIn());
    this.isLoggedInObserver = this.loggedInSubject.asObservable();
  }

  /**
   * check if already logged in
   */
  isLoggedIn() {
    return !!this.storageService.get('access_token');
  }

  setLoggedInSubject(bool) {
    this.loggedInSubject.next(bool);
  }

}
