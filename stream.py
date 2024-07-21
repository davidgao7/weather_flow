# python stream process application
import logging
from requests_sse import EventSource


def main():
    logging.info("START")

    with EventSource(
        "http://github-firehose.libraries.io/events", timeout=30
    ) as event_source:
        for event in event_source:
            logging.info("Got event: %s", event)


if __name__ == "__main__":
    logging.basicConfig(level="DEBUG")
    main()
