# python stream process application
import logging
from quixstreams import Application


def main():
    logging.info("START")
    app = Application(
        broker_address="localhost:9092",
        loglevel="DEBUG",
        auto_offset_reset="earliest",
        consumer_group="weather_processor",
    )

    input_topic = app.topic("weather_data_demo")
    output_topic = app.topic("weather_data_processed")

    def transform(msg):

        # e.g. get data and process it
        celcius = msg["current"]["temperature_2m"]
        farenheit = (celcius * 9 / 5) + 32
        kelvin = celcius + 273.15

        new_msg = msg
        logging.debug("Returning: %s", new_msg)

        return new_msg

    # streaming dataframe
    sdf = app.dataframe(input_topic)
    sdf = sdf.apply(transform)
    sdf = sdf.to_topic(output_topic)


if __name__ == "__main__":
    logging.basicConfig(level="DEBUG")
    main()
