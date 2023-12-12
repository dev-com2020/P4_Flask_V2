import logging

log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

logging.basicConfig(level=logging.DEBUG,
                    format=log_format)

logging.debug('debug message')
logging.info('info message')
logging.warning('warning')
logging.error('error message')
logging.critical('critical message')

some_logger = logging.getLogger('some_logger')
some_logger.warning("warning message z some_logera")

# from colorama import Fore, Back, Style
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')