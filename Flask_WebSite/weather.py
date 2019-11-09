from darksky.api import DarkSky
from darksky.types import languages, units, weather


API_KEY = '23612e156976e7443d9ea43233f12e95'

darksky = DarkSky(API_KEY)

latitude = 34.74929
longitude = -77.42105
forecast = darksky.get_forecast(
    latitude, longitude,
    extend=False, # default `False`
    lang=languages.ENGLISH, # default `ENGLISH`
    units=units.AUTO, # default `auto`
    exclude=[weather.MINUTELY, weather.ALERTS] # default `[]`
)

print(forecast.currently.temperature)

forecast.latitude # 34.74929
forecast.longitude # -77.42105
forecast.timezone # timezone for coordinates. For exmaple: `America/North_Carolina`

forecast.currently # CurrentlyForecast. Can be found at darksky/forecast.py
forecast.minutely # MinutelyForecast. Can be found at darksky/forecast.py
forecast.hourly # HourlyForecast. Can be found at darksky/forecast.py
forecast.daily # DailyForecast. Can be found at darksky/forecast.py
forecast.alerts # [Alert]. Can be found at darksky/forecast.py