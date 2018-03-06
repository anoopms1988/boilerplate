import {NgModule} from '@angular/core';
import {Routes, RouterModule} from '@angular/router';
import {JobListComponent} from './joblist/joblist.component';

const routes: Routes = [
  {
    path: '',
    component: JobListComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DashboardRoutingModule {
}
