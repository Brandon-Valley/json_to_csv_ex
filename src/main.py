

from sms.logger import logger # csv, horrible name
from sms.logger import json_logger

import os

HEADER_ORDER_LIST = ['datetime','open','high','low','close','volume'] # this defines the order of the headers in the output csv

SCRIPT_PARENT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
print(SCRIPT_PARENT_DIR_PATH)

TEST_DIR_PATH = os.path.abspath(os.path.join(SCRIPT_PARENT_DIR_PATH, '..', 'test'))
print(TEST_DIR_PATH)


INPUT_JSON_FILE_PATH = os.path.abspath(os.path.join(TEST_DIR_PATH, 'input_data.json'))
print(INPUT_JSON_FILE_PATH)

OUTPUT_CSV_FILE_PATH = os.path.abspath(os.path.join(TEST_DIR_PATH, 'output_data.csv'))
print(OUTPUT_CSV_FILE_PATH)



init_json_input_data_dld = json_logger.read(INPUT_JSON_FILE_PATH, return_if_file_not_found = False)

json_data_to_be_written_to_csv_dl = init_json_input_data_dld['candles']

print(json_data_to_be_written_to_csv_dl)

logger.write2CSV(logDictList = json_data_to_be_written_to_csv_dl, 
                 csvPath     = OUTPUT_CSV_FILE_PATH, 
                 headerList  = HEADER_ORDER_LIST)

print('output written: ', OUTPUT_CSV_FILE_PATH)







print('done')