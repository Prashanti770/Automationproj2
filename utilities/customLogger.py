import logging


class LogGen:

    @staticmethod
    def loginfo():
        logging.basicConfig(filename="C:\\Users\\USER\PycharmProjects\\Automationproj2\\Logs\\automationlogs.log",
                            format='%(asctime)s %(levelname)s %(message)s',
                            filemode='w',
                            datefmt='%m/%d/%Y %I:%M:%S %p',
                            force= True)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        # logger.setLevel(logging.ERROR)
        return logger


    #
    # def loggen():
    #     logging.basicConfig(filename=".\\Logs\\automation.log",
    #                         filemode='a',
    #                         format='%(asctime)s: %(levelname)s: %(message)s',
    #                         datefmt='%m/%d/%Y %I:%M:%S %p',
    #                         )
    #     logger = logging.getLogger()
    #     logger.setLevel(logging.INFO)
    #     return logger
