import {environment} from '../../environments/environment';

const api_url = environment.api_url;
export const Constants = {
  login: () => {
    return api_url + '/api/account/auth';
  },
  getJobs: (page_number) => {
    return api_url + '/api/job/form/job_list?start=' + page_number;
  }
};
