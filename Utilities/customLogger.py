import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="C:/Users/WIN 10/PycharmProjects/nopCommerce_Hybrid/Logs",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
