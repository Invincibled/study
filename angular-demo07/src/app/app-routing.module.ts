import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { HomeComponent } from './components/home/home.component';
import { ProductComponent } from './components/product/product.component';
import { PcateComponent } from './components/product/pcate/pcate.component';
import { PlistComponent } from './components/product/plist/plist.component';
import { WelcomeComponent } from './components/home/welcome/welcome.component';
import { SettingComponent } from './components/home/setting/setting.component';

const routes: Routes = [
  {
    path:'home', component: HomeComponent,
    children:[
      {
        path:'welcome', component: WelcomeComponent
      },
      {
        path:'setting', component: SettingComponent
      },
      {
        path:"**", redirectTo:"welcome"
      }
    ]
  },
  {
    path:'product', component: ProductComponent,
    children:[
      {
        path:'pcate', component: PcateComponent
      },
      {
        path:'plist', component: PlistComponent
      },
      {
        path:"**", redirectTo:"plist"
      }
    ]
  },
  {
    path:"**", redirectTo:"home"
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
