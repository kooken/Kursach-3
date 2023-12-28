import os.path

from utils import load_operations, executed_operations, sorted_date, formatted_operations
from config import ROOT_DIR

OPERATIONS_FILE_PATH = os.path.join(ROOT_DIR, 'src', 'operations.json')

def main():
    all_operations = load_operations(OPERATIONS_FILE_PATH)
    exec_operations = executed_operations(all_operations)
    sorted_by_date = sorted_date(exec_operations)
    format_operations = formatted_operations(sorted_by_date)

    print(format_operations)

main()





