import 'package:flutter/material.dart';
import 'package:flutter_demo01/pages/form.dart';
import 'package:flutter_demo01/pages/search.dart';
import './pages/tabs.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatefulWidget {
  MyApp({Key key}) : super(key: key);

  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  final rounters = {
    '/': (context) => Tabs(),
    '/search': (context, {arguments}) => SearchPage(arguments: arguments),
    '/form': (context, {arguments}) => FormPage("arguments:arguments")
  };
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      // initialRoute: '/',
      home: Tabs(),
      onGenerateRoute: (RouteSettings settings) {
        print("1111111111s");
        final String name = settings.name;
        print(name);
        final Function pageContentBuilder = this.rounters[name];
        // if (pageContentBuilder != null) {
        if (settings.arguments != null) {
          final Route route = MaterialPageRoute(
              builder: (context) =>
                  pageContentBuilder(context, arguments: settings.arguments));
          return route;
        } else {
          final Route route = MaterialPageRoute(
              builder: (context) => pageContentBuilder(context));
          return route;
        }
        // }
      },
    );
  }
}

// class MyApp extends StatelessWidget {
//   // final arguments;
//   // MyAPP({this.arguments});

//   final rounters = {
//     '/': (context) => Tabs(),
//     '/search': (context, {arguments}) => SearchPage(arguments: arguments),
//     '/form': (context, {arguments}) => FormPage("arguments:arguments")
//   };

//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       initialRoute: '/',
//       onGenerateRoute: (RouteSettings settings) {
//         print(settings);
//         final String name = settings.name;
//         print(name);
//         final Function pageContentBuilder = this.rounters[name];
//         // if (pageContentBuilder != null) {
//         if (settings.arguments != null) {
//           final Route route = MaterialPageRoute(
//               builder: (context) =>
//                   pageContentBuilder(context, arguments: settings.arguments));
//           return route;
//         } else {
//           final Route route = MaterialPageRoute(
//               builder: (context) => pageContentBuilder(context));
//           return route;
//         }
//         // }
//       },
//     );
//   }
// }
