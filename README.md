## About
### The weather app 
This project is my first step into the field of app development. I decided to give it a try to create a simple weather app, which further in development ended in a weather app focusing on multiple units of measurement one encounters during studying physics. 
The app supports basic SI units with the temperature given in $^\circ C$, natural units as well as typical measurements in astronomy. The code is mostly python with the focus set on the module kivy. 
## Formulas used 
### Natural Units 
This system of units is mostly used in the field of particle physics. Its build around the convention to set reoccuring constants to $1$, such as $c=\hbar=G=1$. As a consequence energy, $E$ and mass, $m$, are related through the well known mass-energy relation, $E=mc^2$, where energy is expressed in units $[E]=\text{ eV}$ and mass in terms of $[m]=\text{ eV}/c^2$. Within this mode, following measures are used: 
* Temperature: $E=k_bT$
* Percentage in multiples of the finestructure constant $\alpha$, eg. $100\\%=137\alpha$
* Velocity in multiples of the speed of light $c$
* Angles in [rad]
* Length in dimension of $\frac{1}{\text{eV}}$ via $\hbar c\approx 197\text{MeV}\\,\text{fm}$
* Pressure in dimensions of $\frac{\text{eV}^4}{\hbar^2c^3}$
* 
### Astronomical Units 
Units used in astronomy are linked to typical scales encountered in that field of physics. An example, often met is expressing mass in terms of the solar mass or the mass of Jupiter. 
In addition, some measures are related to their observable properties, such as the chemical composition of a star has its distinct spectral footprint. The scales used within this application are: 
* Temperature converted to wavelength via Wien' displacement law: $\lambda=2.898\cdot 10^{-3}\text{m}\\,\text{K}\frac{1}{T}$
* Percentage in terms of steradian $\Omega=\frac{A}{r^2}$, where A is the area, and r the radius of a sphere, such that $100\\%=4\pi\\,\text{sr}$
* Velocity in terms of astronomical units (AU) by years (yr).
* Angles in arcsecond, $1"=\frac{1}{3600}^\circ$
* Length in multiples of the radius of the earth $r_♁=6371\\,\text{km}$
* Pressure is a bit far-fetched: It's given as radius of a neutron star, with homogenous density of $\rho=8.35\cdot 10^{16}\frac{\text{kg}}{\text{m}^3}$ ,whose inner pressure coincides with our atmospheric pressure. $r=\sqrt{\frac{3}{2\pi}\frac{P}{G\rho^2}}$
* 
## Installation
### Prerequisits
In addition to python, the following modules are required in order to run the project using a python compiler: kivy, requests, datetime, matplotlib, android.
Some of them have to be installed, which is done easily in the console with:
```console
pip install kivy
pip install requests
pip install matplotlib
```
When building the application for android use, then I highly recommend building the app using buildozer. In that case, feel free to follow the [installation guide](https://buildozer.readthedocs.io/en/latest/installation.html)
In order to use the app, you will also need an individual API key to receive the weather data provided by [OpenWeatherMap](https://openweathermap.org/). Simply register on the website and verify your account. After that, your key is located under your profile/My API keys and you're good to go.
## Using the weather app
#### On Linux
When using Linux, simply run
```console
python3 /PATH-TO-PROJECT/main.py
```
, where /PATH-TO-PROJECT needs to be replaced with the path to where the project is located.
  
#### On Android
After following the former steps, simply navigate to the directory, where main.py is located and run the command
```console
buildozer -v android debug
```
It will take a few minutes building the apk. As soon as the building process is finished, the application is located in the /bin directory. Drsg the file onto your mobile and install it. 

### Using the the app the first time 
When you use the app for the first time, go into settings and replace 'API key' with your API key received by OpenWeatherMap. 
### General use 
The app is ready to use after inserting the key. In the setting, you are able to change the units, the weather should represented with. Other then that, its a simple (confusing) weather app. The first page displays the current weather. When swiping to the right you'll see a 5-day-forecast. 
## Future plans I will try further to work on the app in my free time: 
- [ ] Clean up the weather.kv file
- [ ] Enhance widget placement for different screens
- [ ] Implement further units of measurement (not included: Imperial units)
- [ ] Include maps
      
## License 
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
