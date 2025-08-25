import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { DetailsUsersService } from 'src/app/services/details-users.service';
interface Day {
  nameHe: string;
  nameEn: string;
  isFlipped: boolean;
}

@Component({
  selector: 'app-diet',
  templateUrl: './diet.component.html',
  styleUrls: ['./diet.component.scss']
})
export class DietComponent implements OnInit{
  constructor(public du:DetailsUsersService, public r: Router){}
  f:boolean=false
  days: Day[] = [
    { nameHe: 'יום ראשון', nameEn: 'ראשון', isFlipped: false },
    { nameHe: 'יום שני', nameEn: 'שני', isFlipped: false },
    { nameHe: 'יום שלישי', nameEn: 'שלישי', isFlipped: false },
    { nameHe: 'יום רביעי', nameEn: 'רביעי', isFlipped: false },
    { nameHe: 'יום חמישי', nameEn: 'חמישי', isFlipped: false },
    { nameHe: 'יום שישי', nameEn: 'שישי', isFlipped: false },
    { nameHe: 'יום שבת', nameEn: 'שבת', isFlipped: false }
  ];
  ngOnInit(): void {
     this.f=false  
  }
  addDiet()
  {
    this.f=true
    this.du.fLogIn=false
    console.log(this.du.u);
    this.du.addDiet().subscribe(
      succ=>{
        // alert("הדיאטה התקבלה!!!")
        this.du.d = succ
        console.log(this.du.d);
        this.f=false
        
      },
      err=>{
        alert("אמממ נסה שוב.....")
        this.f=false
        this.du.fLogIn=true
      }
    )
  }
  updateDiet()
  {
    debugger
    this.f=true
    this.du.fUpdate=false
    this.du.fSignIn=false
    this.du.updateDiet().subscribe(
      succ=>{
        // console.log(succ);
        
        // alert("הדיאטה עודכנה!!!")
        // this.du.fSignIn=true
        this.du.d = succ
        // console.log(this.du.d);
        this.f=false
        
      },
      err=>{
        alert("אמממ נסה שוב.....")
        this.f=false
        this.du.fUpdate=true
        this.du.fSignIn=true
      }
    )
  }
  getDiet()
  {
    debugger
    this.f=true    
    // this.onClickCoolButton()
    this.du.fSignIn=false
    this.du.getDietById().subscribe(
      succ=>{
        // alert("הדיאטה התקבלה!!!")
        this.du.d = succ
        console.log(this.du.d);
        this.f=false
        
      },
      err=>{
        alert("אמממ נסה שוב.....")
        this.f=false
        this.du.fSignIn=true
      }
    )
  } 

  toggleFlip(day: Day) {
    day.isFlipped = !day.isFlipped;
  }
  // onClickCoolButton(){
  //   console.log("dfghj");
  //   const coolButton = document.getElementById('cool-button') as HTMLButtonElement;
  //   coolButton.classList.add('clicked');
  //   setTimeout(() => {
  //     coolButton.style.display = 'none';
  //   }, 0); // זמן האנימציה
  // } 
}
