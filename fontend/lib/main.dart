import 'package:flutter/material.dart';
import 'package:fontend/Page/form_page.dart';
import 'package:fontend/Page/login_page.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      routes: {
        "/": (context)=> const FormPage(),
        "/login":(context) => const LoginePage()
      },
    );
  }
}
