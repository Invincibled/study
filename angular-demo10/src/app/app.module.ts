import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {UserModule} from "./module/user/user.module";
import {ProductModule} from "./module/product/product.module";
import {ArticleModule} from "./module/article/article.module";

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    // UserModule,
    // ProductModule,
    // ArticleModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
