import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { DetailsUsersService } from 'src/app/services/details-users.service';

@Component({
  selector: 'app-sign-in',
  templateUrl: './sign-in.component.html',
  styleUrls: ['./sign-in.component.css']
})
export class SignInComponent implements OnInit{
  mail:string=""
  pass:string=""
  constructor(public du:DetailsUsersService, public r:Router){}
  ngOnInit(): void {
    this.du.flagCnisa=false
  }
  GetUserByMailAndPassword()
  {
    this.du.getByMailAndPassword(this.mail, this.pass).subscribe(
      succ=>
      {
        this.du.u=succ
        this.du.fSignIn=true
        this.r.navigate([`diet`])
        // this.du.u.id = succ['_id']
      },
      err=>{alert("שגיאה")}
    )
  }
}
