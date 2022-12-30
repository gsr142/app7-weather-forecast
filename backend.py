API_KEY = "a31b31ba27b38ec38198e6b6a34bb952"

def get_data(place, forecast_days, kind):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    return data