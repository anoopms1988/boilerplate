import {Injectable} from '@angular/core';
import {HttpService} from 'app/core/http-service/http.service';
import {Constants} from 'app/core/constants';

@Injectable()
export class LoginService {

  constructor(public httpService: HttpService) {
  }

  login(data) {
    return this.httpService.httpPost(Constants.login(), data);
  }

}
