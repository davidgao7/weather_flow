import requests
from quixstreams import Application
import json

response = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={
        "latitude": 42.42,
        "longitude": -71.07,
        "current": "temperature_2m",  # 2m above sea level
    },
)

weather = response.json()

app = Application(broker_address="localhost:9092", loglevel="DEBUG")

with app.get_producer() as producer:
    producer.produce(
        topic="weather_data_demo",
        key="Boston",
        value=json.dumps(weather, indent=4),
    )
