import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
          appBar: AppBar(title: Text('Flutter Demo')), body: HomeContent()),
    );
  }
}

class HomeContent extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ListView(children: <Widget>[
      Card(
          margin: EdgeInsets.all(10),
          child: Column(children: [
            AspectRatio(
                aspectRatio: 20 / 9,
                child: Image.network(
                    "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1597320236858&di=cc10cb71028eb90c9e68823036b32060&imgtype=0&src=http%3A%2F%2Fattach.bbs.miui.com%2Fforum%2F201111%2F21%2F205700txzuacubbcy91u99.jpg",
                    fit: BoxFit.cover)),
            ListTile(
                title: Text("张三"),
                subtitle: Text("高级高功能测试"),
                leading: CircleAvatar(
                    backgroundImage: NetworkImage(
                        "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1597320236858&di=cc10cb71028eb90c9e68823036b32060&imgtype=0&src=http%3A%2F%2Fattach.bbs.miui.com%2Fforum%2F201111%2F21%2F205700txzuacubbcy91u99.jpg")))
          ])),
      Card(
          margin: EdgeInsets.all(10),
          child: Column(children: [
            ListTile(title: Text("张三"), subtitle: Text("高级高功能测试"))
          ])),
      Card(
          margin: EdgeInsets.all(10),
          child: Column(children: [
            ListTile(title: Text("张三"), subtitle: Text("高级高功能测试"))
          ])),
    ]);
  }
}
