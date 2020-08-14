import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class FormPage extends StatelessWidget {
  String title;
  FormPage(String title) {
    this.title = title;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(this.title),
      ),
      body: ListView(
        children: [
          ListTile(
            title: Text("我是表单"),
          ),
          ListTile(
            title: Text("我是表单"),
          ),
        ],
      ),
      floatingActionButton: FloatingActionButton(
        child: Text("返回"),
        onPressed: () {
          // Navigator.of(context).pop();
          Navigator.pushNamed(context, '/search');
        },
      ),
    );
  }
}
