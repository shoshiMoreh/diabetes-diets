import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { diet } from '../classes/diet';

@Injectable({
  providedIn: 'root'
})
export class DietUsersService {
  d:diet=new diet()
  constructor(public http: HttpClient) { }
  basicURL= "http://127.0.0.1:5000/diet/"

}
