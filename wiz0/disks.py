import json


class ScenarioDisk:

    def __init__(self, filename='trebor_sux.json'):
        self.filename = filename
        self.data = self.load_disk()

    def load_disk(self):
        data = _load_disk(self.filename)
        if data and isinstance(data, dict):
            return data
        else:
            return {'roster': {}}

    def save_disk(self):
        with open(self.filename, 'w') as disk_file:
            disk_file.write(json.dumps(self.data, indent=4, sort_keys=True))

def _load_disk(filename):
    try:
        with open(filename) as disk_file:
            data = json.load(disk_file)
    except FileNotFoundError:
        data = None
    return data


# def decorator_example(*args, **kwargs):
#     def sub_func(*args, **kwargs):
#         s = ' '.join([arg for arg in args])
#         return s
#     return sub_func  # <---- This is an actual function being returned, not the returned value from a function call.
