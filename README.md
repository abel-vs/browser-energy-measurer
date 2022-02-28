# browser-energy-measurer
Automated Energy Measurement of Browsers.

## Set up
Install all necessary packages with: ```pip install -r requirements.txt```
### Safari
Safari only works with MacOS and the driver is installed with the operating system.
The driver is kept up-to-date automatically. 
The driver has to be enabled safari-driver.
Run in terminal: ```safaridriver --enable```
### Measure on Windows

Simple test run:

``` & 'C:\Program Files\Intel\Power Gadget 3.6\PowerLog3.0.exe' -file output.csv -cmd python .\src\main.py```

Automatic test measurements:

``` run.ps1```

