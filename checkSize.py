import os

def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

path_to_json = './'
json_files_names = [pos_json  for pos_json in os.listdir(path_to_json) if pos_json.endswith('.pickle')]
json_files_size = [convert_bytes(os.stat(pos_json).st_size) for pos_json in os.listdir(path_to_json) if pos_json.endswith('.pickle')]
print(json_files_names)
print(json_files_size)