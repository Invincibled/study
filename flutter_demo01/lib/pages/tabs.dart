import 'package:flutter/cupertino.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'category.dart';
import 'home.dart';
import 'setting.dart';

class Tabs extends StatefulWidget {
  Tabs({Key key}) : super(key: key);

  @override
  _TabsState createState() => _TabsState();
}

class _TabsState extends State<Tabs> {
  int _currentIndex = 0;
  List<Widget> list = [HomePages(), Categorys(), Settings()];
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
          appBar: AppBar(title: Text('Flutter Demo')),
          body: list[this._currentIndex],
          bottomNavigationBar: BottomNavigationBar(
            currentIndex: this._currentIndex,
            onTap: (int value) {
              setState(() {
                this._currentIndex = value;
              });
            },
            iconSize: 36,
            fixedColor: Colors.red,
            type: BottomNavigationBarType.fixed,
            items: [
              BottomNavigationBarItem(
                icon: Icon(Icons.home),
                title: Text("主页"),
              ),
              BottomNavigationBarItem(
                  icon: Icon(Icons.category), title: Text("分类")),
              BottomNavigationBarItem(
                  icon: Icon(Icons.settings), title: Text("设置")),
            ],
          )),
    );
  }
}
