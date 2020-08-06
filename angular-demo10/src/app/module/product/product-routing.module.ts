import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {ProductModule} from "./product.module";
import {PlistComponent} from "./components/plist/plist.component";
import {PcontentComponent} from "./components/pcontent/pcontent.component";

const routes: Routes = [
  {
    path:'', component:ProductModule
  },
  {
    path:'plist', component:PlistComponent
  },
  {
    path:'pcontent', component:PcontentComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ProductRoutingModule { }
