import { Component } from '@angular/core';
import { details } from 'src/app/classes/details';
import { diet } from 'src/app/classes/diet';
import { DetailsUsersService } from 'src/app/services/details-users.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  constructor(public du:DetailsUsersService){}
  rload()
  {
    // this.du.d=new diet()
    // this.du.u=new details()
    location.reload()
    this.du.flagCnisa=true
  }
}
