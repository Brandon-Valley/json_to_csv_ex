

from sms.logger import logger # csv, horrible name
from sms.logger import json_logger

import os


SCRIPT_PARENT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
print(SCRIPT_PARENT_DIR_PATH)

TEST_DIR_PATH = os.path.abspath(os.path.join(SCRIPT_PARENT_DIR_PATH, '..', 'test'))
print(TEST_DIR_PATH)



INPUT_JSON_FILE_PATH = os.path.abspath(os.path.join(TEST_DIR_PATH, 'input_data.json'))
print(INPUT_JSON_FILE_PATH)


OUTPUT_CSV_FILE_PATH = os.path.abspath(os.path.join(TEST_DIR_PATH, 'output_data.csv'))
print(OUTPUT_CSV_FILE_PATH)









print('done')