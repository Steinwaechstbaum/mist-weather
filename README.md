## About
### The Weather App 
This project is my first step into the field of app development. I decided to give it a try and create a simple weather app, which in further development ended up in a weather app that focuses on several units of measurement you encounter when studying physics. 
The app supports basic SI units with the temperature given in $^\circ C$, natural units as well as typical measures in astronomy. The code is mostly written in Python with the module kivy.
## Formulas used 
### Natural Units 
This unit system is most commonly used in the field of particle physics. It is built around the convention of setting reccuring constants to $1$, such as $c=\hbar=G=1$. As a consequence energy, $E$, and mass, $m$, are related by the well-known mass-energy relation, $E=mc^2$, where energy is expressed in units of $[E]=\text{ eV}$ and mass is expressed in units of $[m]=\text{ eV}/c^2$. Within this mode the following measures are used: 
* Temperature: $E=k_bT$.
* Percentage in multiples of the finestructure constant $\alpha$, e.g. $100\\%=137\alpha$.
* Speed in multiples of the speed of light $c$.
* Angle in [rad]
* Length in dimensions of $\frac{1}{\text{eV}}$ over $\hbar c\approx 197\text{MeV}\\,\text{fm}$.
* Pressure in dimensions of $\frac{\text{eV}^4}{\hbar^2c^3}$.
  
### Astronomical Units 
The Units used in astronomy are related to the typical scales encountered in this field of physics. A common example is expressing mass in terms of the solar mass or the mass of Jupiter. 
In addition, some measures are related to their observable properties, such as the chemical composition of a star has its distinct spectral footprint. The scales used in this application are: 
* Temperature converted to wavelength by Wien's displacement law: $\lambda=2.898\cdot 10^{-3}\text{m}\\,\text{K}\frac{1}{T}$.
* Percent in terms of steradian $\Omega=\frac{A}{r^2}$, where A is the area, and r is the radius of a sphere, so that $100\\%=4\pi\\,\text{sr}$.
* Velocity in terms of astronomical units (AU) by years (yr).
* Angle in arcseconds, $1"=\frac{1}{3600}^\circ$.
* Length in multiples of the Earth's radius $r_♁=6371\\,\text{km}$.
* The pressure is a bit far-fetched: It's given as the radius of a neutron star, with a homogeneous density of $\rho=8.35\cdot 10^{16}\frac{\text{kg}}{\text{m}^3}$, whose internal pressure coincides with our atmospheric pressure. $r=\sqrt{\frac{3}{2\pi}\frac{P}{G\rho^2}}$
  
## Installation
### Prerequisits
In addition to python, the following modules are required in order to run the project with a python compiler: kivy, requests, datetime, matplotlib, android.
Some of these need to be installed, which is easily done in the console with:
```console
pip install kivy
pip install requests
pip install matplotlib
```
When building the application for Android use, then I highly recommend building the application using Buildozer. In this case, feel free to follow the [Installation Guide](https://buildozer.readthedocs.io/en/latest/installation.html).
In order to use the app, you will also need an individual API key to receive the weather data provided by [OpenWeatherMap](https://openweathermap.org/). Just register on the website and verify your account. After that, your key can be found under your Profile/My API keys and you're ready to go.

## Using the Weather App
#### On Linux
If you are using Linux, just run
```console
python3 /PATH-TO-PROJECT/main.py
```
, where /PATH-TO-PROJECT/ must be replaced with the path to where the project is located.
  
#### On Android
After following the previous steps, simply navigate to the directory, where main.py is located and run the command
```console
buildozer -v android debug
```
It will take a few minutes to build the apk. Once the build is finished, the application will be located in the /bin directory. Copy the file to your phone and install it. 

### First time use
If you are using the app for the first time, go to the settings and replace 'API key' with the API key you received from OpenWeatherMap. 

### General use 
The application is ready to use after inserting the key. In the settings you are able to change the units in which the weather should be displayed. Other then that, it is a simple (confusing) weather app. The first page shows the current weather. Swipe to the right and you'll see a 5-day forecast. 

## Future plans 
I will try further to work on the app in my free time: 
- [ ] Include background images
- [ ] Clean up the weather.kv file
- [ ] Enhance widget placement for different screens
- [ ] Implement further units of measurement (not included: Imperial units)
- [ ] Include maps
      
## License 
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
