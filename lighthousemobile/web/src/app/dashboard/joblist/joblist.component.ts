import {Component, OnInit} from '@angular/core';
import {JobService} from '../jobservice/job.service';

@Component({
  selector: 'app-joblist',
  templateUrl: './joblist.component.html',
  styleUrls: ['./joblist.component.css']
})
export class JobListComponent implements OnInit {

  constructor(public josService: JobService) {
  }

  ngOnInit() {
    this.getJobs(1);
  }

  getJobs(page_number) {
    this.josService.getJobs(page_number).subscribe((res) => {
      console.log('res', res);
    });
  }

}
