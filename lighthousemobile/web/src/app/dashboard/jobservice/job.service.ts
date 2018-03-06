import {Injectable} from '@angular/core';
import {HttpService} from '../../core/http-service/http.service';
import {Constants} from 'app/core/constants';

@Injectable()
export class JobService {

  constructor(public httpService: HttpService) {
  }

  getJobs(page_number) {
    return this.httpService.httpGet(Constants.getJobs(page_number));
  }
}
