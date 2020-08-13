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

// class HomeContent extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return Center(
//         child: Container(
//             child: Text(
//               '我是大神',
//               textAlign: TextAlign.center,
//             ),
//             width: 300.0,
//             height: 300.0,
//             color: Colors.yellow,
//             padding: EdgeInsets.all(20.0)));
//   }
// }

// class HomeContent extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return Center(
//         child: Container(
//             child: ClipOval(
//                 child: Image.asset("images/a.jpeg", width: 300, height: 600))));
//   }
// }

class HomeContent extends StatelessWidget {
  final List list = new List();
  HomeContent() {
    for (var i = 0; i < 20; i++) {
      list.add("我是第$i条数据");
    }
  }

  @override
  Widget build(BuildContext context) {
    // return ListView(padding: EdgeInsets.all(20), children: <Widget>[
    //   ListTile(
    //     leading: Icon(Icons.settings),
    //     title: Text("你好"),
    //     subtitle: Text("副标题"),
    //   ),
    //   ListTile(
    //     leading: Icon(Icons.home),
    //     title: Text("你好"),
    //     subtitle: Text("副标题"),
    //   )
    // ]);

    return ListView.builder(
        itemCount: this.list.length,
        itemBuilder: (context, index) {
          return ListTile(title: Text(this.list[index]));
        });
  }
}
