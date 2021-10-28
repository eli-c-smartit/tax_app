import sys
def get_path():
    #return sys.path 
    return "path"

print("my_system.py " + __name__)

if __name__ == "__main__":
    path = get_path()
    print(path)