from quixstreams import Application

app = Application(
    broker_address="localhost:9092",
    loglevel="DEBUG",
    consumer_group="weather_consumer",
)

with app.get_consumer() as consumer:
    consumer.subscribe(["weather_data_demo"])

    # reading loop
    while True:
        msg = consumer.poll(1)

        if msg is None:
            print("breaking...")
        elif msg.error() is not None:
            raise Exception(msg.error())
        else:
            breakpoint()
