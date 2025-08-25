import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { details } from '../classes/details';
import { Observable } from 'rxjs';
import { diet } from '../classes/diet';

@Injectable({
  providedIn: 'root'
})
export class DetailsUsersService {
  u:details=new details()
  d:diet=new diet()
  fLogIn:boolean=false
  fSignIn:boolean=false
  fUpdate:boolean=false
  flagCnisa:boolean=true
  constructor(public http: HttpClient) { }
  basicURL= "http://127.0.0.1:5000/users/"
  addUser():Observable<any>
  {
    return this.http.post<any>(`${this.basicURL}addUser`, this.u)
  }
  getByMailAndPassword(mail:string, password:string):Observable<any>
  {
    return this.http.post<any>(`${this.basicURL}GetUserByMailAndPassword`, {'mail': mail, 'password': password})
  }
  updateUser():Observable<any>
  {
    return this.http.post<any>(`${this.basicURL}updateUser`,  this.u)
  }
  addDiet():Observable<any>
  {
    return this.http.post<any>(`${this.basicURL}addDiet`, {'user': this.u, 'diet': this.d})
  }
  updateDiet():Observable<any>
  {
    return this.http.post<any>(`${this.basicURL}updateDiet`, {'user': this.u, 'diet': this.d})
  }
  getDietById():Observable<any>
  {
    return this.http.post<any>(`${this.basicURL}GetDietById`, this.u.id)
  }
}