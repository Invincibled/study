import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
// import './search.dart';

class HomePages extends StatefulWidget {
  HomePages({Key key}) : super(key: key);

  @override
  _HomePagesState createState() => _HomePagesState();
}

class _HomePagesState extends State<HomePages> {
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        SizedBox(
          height: 300,
        ),
        RaisedButton(
          child: Text("跳转到搜索页面"),
          onPressed: () {
            // Navigator.of(context)
            //     .push(MaterialPageRoute(builder: (context) => SearchPage()));
            // Navigator.pushNamed(context, '/search');
            Navigator.of(context).pushNamed('/search');
          },
        ),
        RaisedButton(
          child: Text("调回来"),
          onPressed: () {
            print("222");
          },
        )
      ],
    );
  }
}
