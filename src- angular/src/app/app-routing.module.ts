import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FormComponent } from './comps/form/form.component';
import { AboutComponent } from './comps/about/about.component';
import { DietComponent } from './comps/diet/diet.component';
import { SignInComponent } from './comps/sign-in/sign-in.component';

const routes: Routes = [
  {path: 'signIn', component: SignInComponent},
  {path: 'logIn', component: FormComponent},
  {path: 'diet', component: DietComponent},
  {path: 'updateDetails', component: FormComponent},
  {path: 'about', component: AboutComponent},
  

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
