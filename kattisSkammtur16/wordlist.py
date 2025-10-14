

def open_file(file):
    try:
        with open(file, "r") as skra_inn:
            return skra_inn
    except:
        print("File not found!")
        return 0

def main():
    file_name = input("Enter filename:")
    file = open_file(file_name)

    openFile = file