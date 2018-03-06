import {Injectable} from '@angular/core';
import 'rxjs/add/operator/do';
import {
  HttpErrorResponse, HttpEvent, HttpHandler, HttpInterceptor, HttpRequest,
  HttpResponse
} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';

/**
 * Intercepting http request and response
 */
@Injectable()
export class HttpInterceptorService implements HttpInterceptor {
  constructor() {
  }

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    return next.handle(req).do((event: HttpEvent<any>) => {
      if (event instanceof HttpResponse) {
        // TODO: Do some thing
      }
    }, (err: HttpErrorResponse) => {
      // TODO: Do something
    });
  }

}
