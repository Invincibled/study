import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {ArticleModule} from "./article.module";

const routes: Routes = [
  {
    path:'', component:ArticleModule
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ArticleRoutingModule { }
