import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FormComponent } from './comps/form/form.component';
import { FormControl, FormsModule, NgModel } from '@angular/forms';
import { HomeComponent } from './comps/home/home.component';
import { DietComponent } from './comps/diet/diet.component';
import { AboutComponent } from './comps/about/about.component';
import { RouterModule } from '@angular/router';
import { SignInComponent } from './comps/sign-in/sign-in.component';
import { HttpClient, HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    FormComponent,
    HomeComponent,
    DietComponent,
    AboutComponent,
    SignInComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [NgModel,],
  bootstrap: [AppComponent]
})
export class AppModule { }
