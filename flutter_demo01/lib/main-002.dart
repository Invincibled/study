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
//       height: 400,
//       width: 400,
//       color: Colors.red,
//       child: Stack(
//         children: <Widget>[
//           Align(
//               alignment: Alignment(1, 0.2),
//               child: Icon(
//                 Icons.search,
//                 size: 40,
//                 color: Colors.white,
//               )),
//           Align(
//               alignment: Alignment(1, -0.2),
//               child: Icon(
//                 Icons.home,
//                 size: 40,
//                 color: Colors.white,
//               )),
//           Align(
//               alignment: Alignment(-1, -0.2),
//               child: Icon(
//                 Icons.send,
//                 size: 40,
//                 color: Colors.white,
//               ))
//         ],
//       ),
//     ));
//   }
// }

class HomeContent extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Center(
        child: Container(
      height: 400,
      width: 400,
      color: Colors.red,
      child: Stack(
        children: <Widget>[
          Positioned(
              left: 0,
              child: Icon(
                Icons.search,
                size: 40,
                color: Colors.white,
              )),
          Positioned(
              right: 0,
              child: Icon(
                Icons.home,
                size: 40,
                color: Colors.white,
              )),
          Positioned(
              bottom: 0,
              child: Icon(
                Icons.send,
                size: 40,
                color: Colors.white,
              ))
        ],
      ),
    ));
  }
}
