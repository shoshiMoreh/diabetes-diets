import { Component, OnInit } from '@angular/core';
import { DetailsUsersService } from 'src/app/services/details-users.service';

@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.css']
})
export class AboutComponent implements OnInit{
  ngOnInit(): void {
    this.du.flagCnisa=false
  }
  constructor(public du:DetailsUsersService){}
}
