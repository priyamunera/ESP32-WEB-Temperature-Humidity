# Autogenerated file
def render(humidity,temperature):
    yield """
<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <title>ESP32 WEB SERVER</title>
    <meta http-equiv=\"refresh\" content=\"5\">
</head>
<body style=\"background-color: #3c424d\">
  <div style=\"color: #e9ecf2\">
       <h4 style=\"text-align: center;\">9.928695, -83.979138 </h4>
       <h5 style=\"text-align: center;\">Temperature: """
    yield str(temperature)
    yield """ || Humidity: """
    yield str(humidity)
    yield """ </h5>
  </div>
</body>
</html>"""
