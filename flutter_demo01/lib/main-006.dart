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
    return Wrap(children: <Widget>[
      MyButton(),
      MyButton(),
      MyButton(),
      MyButton(),
      MyButton(),
      MyButton(),
      MyButton(),
      MyButton()
    ], alignment: WrapAlignment.spaceAround, spacing: 10, runSpacing: 20);
  }
}

class MyButton extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return RaisedButton(
        textColor: Colors.blue,
        child: Text("第一个按钮"),
        textTheme: ButtonTextTheme.primary);
  }
}
