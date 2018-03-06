import {Injectable} from '@angular/core';
import {HttpHeaders, HttpParams} from '@angular/common/http';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';

/**
 * Common gateway for handling http requests
 */
@Injectable()
export class HttpService {

  constructor(public httpClient: HttpClient) {
  }

  /**
   * http GET
   * @param url
   * @param requestParams
   * @returns {Observable<Object>}
   */
  httpGet(url: any, requestParams?: HttpParams): Observable<any> {
    const access_token = 'Bearer ' + window.localStorage.getItem('access_token');
    const headers = new HttpHeaders()
      .append('Authorization', access_token)
      .append('Accept', 'application/json');
    return this.httpClient.get(url, {
      responseType: 'json',
      headers: headers,
      params: requestParams
    });
  }

  /**
   * http POST
   * @param url
   * @param body
   * @returns {Observable<Object>}
   */
  httpPost(url: any, body: any): Observable<any> {
    let headers;
    const access_token = window.localStorage.getItem('access_token');
    if (access_token) {
      headers = new HttpHeaders()
        .set('Authorization', 'Bearer ' + access_token)
        .set('Content-Type', 'application/json');
    }
    return this.httpClient.post(url, body, {
      headers: headers
    });
  }


}
