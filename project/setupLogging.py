import os
import logging
import warnings
from datetime import datetime

def setupLogging():    
    logs_dir = 'Status Report Logs'

    #create logs_dir if it still does not exist
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
        
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_file = f'status_report_{timestamp}.log'

    logging.basicConfig(filename=os.path.join(logs_dir, log_file),
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        filemode='a')
