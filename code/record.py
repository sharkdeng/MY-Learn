
import logging
from datetime import datetime
import os


# 1 get logger
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s\n %(message)s\n\n') # terminal
                    
logger = logging.getLogger()


# 2 add file handler
log_path = '../logs/'
today = datetime.now().strftime('%Y%m%d')
log_name = f'{log_path}{today}.log'

if os.path.exists(log_name):
    fh = logging.FileHandler(log_name, mode='a')
else:
    fh = logging.FileHandler(log_name, mode='w')
    
    
# 3 logging format
formatter = logging.Formatter(fmt='%(asctime)s\n%(message)s\n\n',
                              datefmt='%m-%d-%Y %I:%M:%S') # file 
fh.setFormatter(formatter)

logger.addHandler(fh)




logger.info('good')
