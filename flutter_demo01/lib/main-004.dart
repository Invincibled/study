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
            ListTile(title: Text("张三"), subtitle: Text("高级高功能测试")),
            ListTile(
              title: Text("电话 xxxxx"),
            )
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
