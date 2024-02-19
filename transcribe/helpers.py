import os

def save_file(file_path,content):
    if type(content) == dict:
        import json
        with open(file_path+'.json', 'w') as fp:
            json.dump(content, fp)
            fp.close()
    else:
        with open(file_path, "a+") as f:
            f.write(content)
            f.close()