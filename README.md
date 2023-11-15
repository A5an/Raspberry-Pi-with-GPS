<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body>

  <h1>Raspberry Pi Geolocation Maintenance</h1>

  <h2>Overview</h2>

  <p>This Python script is designed to run on a Raspberry Pi and utilizes GPS data to determine the device's geolocation.
    The script reads NMEA sentences from a GPS module connected to the Raspberry Pi's serial port and updates the geolocation
    information in a Firebase Realtime Database.</p>

  <h2>Requirements</h2>

  <ul>
    <li>Raspberry Pi (or similar single-board computer)</li>
    <li>GPS module supporting NMEA sentences</li>
    <li>Python 3.x</li>
    <li><code>serial</code> library</li>
    <li><code>pynmea2</code> library</li>
    <li><code>firebase-admin</code> library</li>
    <li>Firebase project with a Realtime Database</li>
  </ul>

  <h2>Setup</h2>

  <ol>
    <li>Connect the GPS module to the Raspberry Pi's serial port (e.g., <code>/dev/ttyAMA0</code>).</li>
    <li>Install the required Python libraries:</li>
  </ol>

  <pre><code>pip install serial pynmea2 firebase-admin
  </code></pre>

  <ol start="3">
    <li>Create a Firebase project and download the credentials JSON file (<code>credentials.json</code>).</li>
    <li>Update the <code>credentials.json</code> path in the script with the correct file path.</li>
  </ol>

  <h2>Firebase Configuration</h2>

  <p>Make sure to set up a Firebase Realtime Database with a structure that matches the script's expectations. In the
    provided script, the geolocation information is stored under the <code>Location</code> node.</p>

  <h2>Usage</h2>

  <p>Run the script on the Raspberry Pi:</p>

  <pre><code>python your_script_name.py
  </code></pre>

  <p>The script continuously reads GPS data, extracts the latitude and longitude from the GPRMC NMEA sentence, and updates
    the Firebase Realtime Database with the current geolocation. The update interval is set to 3 seconds in the provided
    script (<code>time.sleep(3)</code>), but you can adjust this value based on your requirements.</p>

  <h2>Important Note</h2>

  <ul>
    <li>Ensure the serial port is correctly configured in the <code>geoloc</code> function (variable
      <code>port</code>).</li>
    <li>Verify the correctness of the NMEA sentence check (<code>if data[0:6] == "$GPRMC":</code>) based on your GPS
      module's output.</li>
  </ul>

</body>

</html>
