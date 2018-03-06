import {Injectable} from '@angular/core';

@Injectable()
export class StorageService {

  constructor() {
  }

  /**
   * set item into local storage
   * @param name
   * @param value
   */
  set(name: string, value: any) {
    value = typeof value === 'string' ? value : JSON.stringify(value);
    window.localStorage.setItem(name, value);
  }

  /**
   * get value from local storage
   * @param name
   * @returns {any}
   */
  get(name) {
    let val;
    try {
      val = JSON.parse(window.localStorage.getItem(name));
    } catch (error) {
      val = window.localStorage.getItem(name);
    }
    return val;
  }

}
