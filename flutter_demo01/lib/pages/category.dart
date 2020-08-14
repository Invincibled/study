import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'form.dart';

class Categorys extends StatefulWidget {
  Categorys({Key key}) : super(key: key);

  @override
  _CategorysState createState() => _CategorysState();
}

class _CategorysState extends State<Categorys> {
  @override
  Widget build(BuildContext context) {
    return Container(
      child: RaisedButton(
        child: Text("我要跳转表单"),
        onPressed: () {
          Navigator.of(context)
              .push(MaterialPageRoute(builder: (context) => FormPage("我是表单")));
        },
      ),
    );
  }
}
