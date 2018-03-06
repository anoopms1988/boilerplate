import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';

import {DashboardRoutingModule} from './dashboard-routing.module';
import {JobListComponent} from './joblist/joblist.component';
import {JobService} from './jobservice/job.service';
import {DataTableModule} from 'primeng/primeng';

@NgModule({
  imports: [
    CommonModule,
    DashboardRoutingModule,
    DataTableModule
  ],
  providers: [JobService],
  declarations: [JobListComponent]
})
export class DashboardModule {
}
