from src.logger import logging

def main():
    logging.info("Starting the application.")
    logging.info("This is a test log message.")
    try:
        x = 1 / 0  # Example error
    except Exception as e:
        logging.error("An error occurred", exc_info=True)

if __name__ == "__main__":
    main()
