from kivy.app import App
from kivy.storage.jsonstore import JsonStore
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty
import functions.draw as draw
#Remove
from kivy.core.window import Window
Window.size = (300, 500)

#Storage modules
settings = JsonStore('./settings.json')

#Custom togglebutton for settings
class UnitsButton(Widget):
    unit = NumericProperty(0)
    def on_state(self, value):
        self.unit = value
        if self.parent:
            settings_screen = self.parent.parent
            settings_screen.update_units(self, value)

class SettingsScreen(Screen):
    #Define and initialize settings
    settings = settings.get('settings')
    city = StringProperty(settings.get('city'))
    units = NumericProperty(settings.get('units'))
    API = StringProperty(settings.get('API'))

    #Initialize settings screen
    def __init__(self, *args, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        self.ids.API_field.text = self.API 
        if self.units ==0:
            self.ids.unit_select.button1.state = 'down'
        elif self.units == 1:
            self.ids.unit_select.button2.state = 'down'
        else:
            self.ids.unit_select.button3.state = 'down'

    #Store settings
    def update_city(self, new_city):
        self.city = new_city
        settings.put('settings', city=new_city, units=self.units, API=self.API)

    def update_units(self, instance, new_unit):
        self.units = new_unit
        settings.put('settings', city=self.city, units=self.units, API=self.API)
    
    def update_API(self, new_API):
        self.API = new_API
        settings.put('settings', city=self.city, units=self.units, API=new_API)

class MainScreen(Screen):
    weather_icon = StringProperty('Images/Icons/Weather_08.png')
    background_img = StringProperty('Images/background_night_08.png')

    #Define and initialize settings
    settings_data = settings.get('settings')
    city = StringProperty(settings_data.get('city'))
    units = NumericProperty(settings_data.get('units'))
    API = StringProperty(settings_data.get('API'))

    #Define and initialize variables
    loc = StringProperty('A')
    time = StringProperty('0\n0')
    temp = StringProperty('0')
    temp_min = StringProperty('0')
    temp_max = StringProperty('0')
    hum = StringProperty('0%')
    overcast = StringProperty('0 (blank)')
    wind = StringProperty('0 (0)')
    overall = StringProperty('Clear')
    future_image = StringProperty('./forecast.png')

    #Initialize main screen
    def __init__(self, *args, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.load_settings()
        self.update_current()

    #Apply settings after leaving them
    def on_enter(self):
        self.load_settings()
        self.update_current()
        self.update_future()

    #Load current settings
    def load_settings(self):
        settings = JsonStore('./settings.json')
        self.settings_data = settings.get('settings')
        self.city = self.settings_data.get('city')
        self.units = self.settings_data.get('units')
        self.API = self.settings_data.get('API')

    #Update first screen and background
    def update_current(self):
        data_file_current = JsonStore('current.json')
        main = data_file_current.get('main')
        weather = data_file_current.get('weather')
        clouds = data_file_current.get('clouds')
        wind_dict = data_file_current.get('wind')
        self.loc = data_file_current['name']
        self.time = draw.write_time(data_file_current['dt'], self.units)
        self.overall = weather[0]['main']
        self.temp =  draw.write_temp(main['temp'], self.units)
        self.temp_min = draw.write_temp(main['temp_min'], self.units)
        self.temp_max = draw.write_temp(main['temp_max'], self.units)
        self.hum = draw.write_perc(main['humidity'], self.units)
        self.overcast = draw.write_clouds(clouds['all'], weather[0]['description'], self.units)
        self.wind = draw.write_wind(wind_dict['speed'], wind_dict['deg'], self.units)
        #Set weather icon
        self.weather_icon = 'Images/Icons/Weather_' + draw.weather_icon(weather[0]['id'])
        self.ids.Icon.reload()
        #Set background image
        self.background_img = 'Images/Background/background_' + draw.background_image(data_file_current['dt'], weather[0]['id'])
        #self.ids.background.reload()
    
    #Plot and update forecast
    def update_future(self):
        draw.plot_all(self.units)
        self.ids.ForeCast.reload()

#Build app
class WeatherApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm
    
if __name__ == '__main__':
    WeatherApp().run()