import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ProductComponent } from './components/product/product.component';
import { NewsComponent } from './components/news/news.component';
import { HomeComponent } from './components/home/home.component';
import { NewscontentComponent } from './components/newscontent/newscontent.component';

const routes: Routes = [
  {
    path:"home", component: HomeComponent
  },
  {
    path:"news",component: NewsComponent
  },
  {
    path:"newscontent", component:NewscontentComponent
  },
  {
    path:"product", component:ProductComponent
  },

  {
    path:"**",redirectTo:'home'
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
