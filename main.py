import collections
import json

FILE = "./sales_log.json"

def load_json_data(path_to_file):
    try:
        with open(path_to_file, "r", encoding="utf8") as opened_file:
            json_data = json.load(opened_file)
        return json_data
    except ValueError:
        return None
        
def print_stat(sales_stat):
    for item, count in sales_stat.most_common():
        print('{} - {}'.format(item, count))
    
if __name__ == '__main__':
    SALES = load_json_data(FILE)
    sales_stat = collections.Counter(SALES)
    print_stat(sales_stat)
