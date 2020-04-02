import logging

def main():
    #fmtstr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d % (message)s"
    logging.basicConfig(level=logging.DEBUG, filename="output.log", filemode="w")


    logging.debug("this is a debug message")
    logging.info("this is an info message")
    logging.warning("this is a warning message")
    logging.error("This is a error message")
    logging.critical("This is a critical message")

    #formatted string
    logging.info("Heres a {} variable and an int:".format("string", 10))

if __name__ == "__main__":
    main()