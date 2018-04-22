import pickle

class Files:
    def write_file(self, file, object_to_write):
        with open(file, "wb") as f:
            picle.dump(object_to_write, file, protocol=4, fix_imports=False)

    def get_job_list_from_file(self, file):
        try:
            with open(file, "rb") as f:
                return picle.load(f, fix_imports=False, encoding=ASCII, errors="strict")
        except FileNotFoundError:
            print("******************************************  File not found !!!")

# Import this to jobmanager.py
files = Files()
