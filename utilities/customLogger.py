import logging


# class LogGen:
#
#     @staticmethod
#     def loginfo():
#         logging.basicConfig(filename="C:\\Users\\USER\PycharmProjects\\Automationproj2\\Logs\\automationlogs.log",
#                             format='%(asctime)s %(levelname)s %(message)s',
#                             filemode='w',
#                             datefmt='%m/%d/%Y %I:%M:%S %p',
#                             force= True)
#
#         logger = logging.getLogger()
#         logger.setLevel(logging.INFO)
#         # logger.setLevel(logging.ERROR)
#         return logger

import inspect
import logging


def customLogger(logLevel=logging.DEBUG):

    # Gets the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("automation.log", mode='a')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')

    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger