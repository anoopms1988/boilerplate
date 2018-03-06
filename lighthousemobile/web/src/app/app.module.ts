import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';


import {AppComponent} from './app.component';
import {AppRoutingModule} from './app-routing.module';
import {HttpService} from './core/http-service/http.service';
import {HttpClientModule} from '@angular/common/http';
import {CoreModule} from './core/core.module';
import {SharedService} from './shared/shared.service';
import {StorageService} from './shared/storage.service';
import {LoginGuard} from './login/login.guard';
import {AuthGuard} from './shared/auth.guard';
import {HeaderComponent} from './layout/header/header.component';


@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    CoreModule
  ],
  providers: [
    HttpService,
    SharedService,
    StorageService,
    LoginGuard,
    AuthGuard
  ],
  bootstrap: [AppComponent]
})
export class AppModule {
}
