import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

// class SearchPage extends StatelessWidget {
//   final arguments;
//   SearchPage({this.arguments});

//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(
//         title: Text("搜索"),
//       ),
//       body: Container(
//         child: Text("你好跳转${arguments['id']}"),
//       ),
//     );
//   }
// }

class SearchPage extends StatefulWidget {
  final arguments;
  SearchPage({this.arguments});

  @override
  _SearchPageState createState() => _SearchPageState(arguments: {arguments});
}

class _SearchPageState extends State<SearchPage> {
  final arguments;
  _SearchPageState({this.arguments});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("搜索"),
      ),
      body: Container(
        child: Text("你好跳转${arguments['id']}"),
      ),
    );
  }
}
