import { AfterViewInit, Component, ElementRef, OnInit, QueryList, ViewChildren } from '@angular/core';
import { details } from '../../classes/details';
import { DetailsUsersService } from 'src/app/services/details-users.service';
import { Router } from '@angular/router';
import { diet } from 'src/app/classes/diet';

@Component({
  selector: 'app-form',
  templateUrl: './form.component.html',
  styleUrls: ['./form.component.css']
})
export class FormComponent implements AfterViewInit, OnInit{
  d:details=new details()
  currentStep:number=0
  @ViewChildren('f') fieldsets!: QueryList<ElementRef>;
  upd:boolean=false
  constructor(public du:DetailsUsersService, public r:Router){}
  ngOnInit(): void {
    this.du.flagCnisa=false
  }
  ngAfterViewInit(): void {
    debugger
    console.log(this.fieldsets);
    console.log(this.fieldsets.length);
    
    this.fieldsets.forEach((fieldset, index) => {
      if (index > 0) {
        fieldset.nativeElement.style.display = 'none';
      }
    });
    if(this.r.url=='/updateDetails')
      {
        this.upd=true
      }
  }
  user()
  {
    console.log(this.du.u);
    if(!this.upd)
      {
        this.du.addUser().subscribe(
        succ=>{
          // alert("המשתמש נוסף בהצלחה!!")
          this.du.u.id=parseInt(succ)
          console.log(this.du.u)
          this.du.fLogIn=true
          this.r.navigate([`diet`])
        },
        err=>{
          alert("אמממ נסה שוב.....")
        }
      )
      }
    
  }
  updateDetails()
  {
    this.du.updateUser().subscribe(
      succ=>{
        console.log(succ);
        
        // alert("המשתמש עודכן בהצלחה!!")
        this.du.fSignIn=false
        this.du.fUpdate=true
        this.du.d=new diet()
        this.r.navigate([`diet`])
        
      },
      err=>{
        alert("אמממ נסה שוב.....")
      }
    )
  }
  
  // פונקציה להצגת הפעם הבאה של ה-fieldset
  nextStep()
  {
    const nextIndex = this.currentStep + 1;
    if (nextIndex < this.fieldsets.length) {
      this.fieldsets.toArray()[this.currentStep].nativeElement.style.display = 'none';
      this.fieldsets.toArray()[nextIndex].nativeElement.style.display = 'block';
      this.currentStep = nextIndex;
    }
  }

  // פונקציה להצגת הפעם הקודמת של ה-fieldset
  prevStep()
  {
    const prevIndex = this.currentStep - 1;
    if (prevIndex >= 0) 
      {
        this.fieldsets.toArray()[this.currentStep].nativeElement.style.display = 'none';
        this.fieldsets.toArray()[prevIndex].nativeElement.style.display = 'block';
        this.currentStep = prevIndex;
      }
  }
}
