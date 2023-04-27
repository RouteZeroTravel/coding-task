import 'dart:convert';

import 'package:carbon_app/button.dart';
import 'package:flutter/material.dart';

import 'http.dart';

// Skip to [TransportCarbonAppState] for the main logic of the app.
void main() {
  runApp(
    const MaterialApp(
      home: Scaffold(
        body: TransportCarbonApp()
      )
    )
  );
}

/// Displays carbon emissions for:
/// - a transport type chosen by the user via pressing on a button
/// - a distance entered in a text field
/// 
/// Skip to [TransportCarbonAppState] for the main logic of the app.
/// 
class TransportCarbonApp extends StatefulWidget {
  const TransportCarbonApp({super.key});

  @override
  State<StatefulWidget> createState() {
    return TransportCarbonAppState();
  }
}

class TransportCarbonAppState extends State<TransportCarbonApp> {
  static const _secretKey = "ecc3ef28-8d20-402e-b8ce-33acab957c4c";

  /// Displayed to the user.
  String _emissionsTonnes = "";

  /// Used to get the contents of a text field where the user has typed in a distance km.
  final _controller = TextEditingController();

  Future<void> _calculate(String transportMethod) async {
    // Text entered by the user
    final distanceKm = _controller.text;

    final url = 'http://127.0.0.1:5000/carbon-emissions/$transportMethod/$distanceKm';
    final r = await httpGet(url, headers: {
      "x-api-key": _secretKey
    });
    final j = json.decode(r.body);
    // Use [setState] to tell the UI to update to show the newly calculated emissions.
    // The value of _emissionsTonnes is shown to the user
    setState(() {
      if (j != null) {
        _emissionsTonnes = (j["emissionsKgCO2"] / 1000).toString();
      } else {
        _emissionsTonnes = "unknown"; 
      }
    });

    if (_emissionsTonnes == "unknown") {
      // Show some UI to tell the user that there was an error
      showDialog(
        context: context,
        builder: (context) =>
          const AlertDialog(
            title: Text("Error calculating emissions")
          )
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Text("Calculated emissions (tonnes): $_emissionsTonnes"),
        const SizedBox(height: 120),
        TextField(
          controller: _controller,
        ),
        const SizedBox(height: 120),
        Button(
          text: "Economy class flight",
          onPressed: () => _calculate("economyFlight")
        ),
        const SizedBox(height: 20),
        Button(
          text: "Business class flight", 
          onPressed: () => _calculate("businessFlight")
        ),
        const SizedBox(height: 20),
        Button(
          text: "Train", 
          onPressed: () => _calculate("train")
        )
      ]
    );
  }
}