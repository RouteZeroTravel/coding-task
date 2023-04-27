
import 'package:http/http.dart' as http;

Future<http.Response> httpGet(String url, {Map<String, String>? headers}) {
  return http.get(Uri.parse(url), headers: headers);
}