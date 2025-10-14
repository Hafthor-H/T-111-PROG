file_name = input()

try:
    with open("/src/"+file_name, "rb") as file_in:
        x = 0
        for i in file_in.read():
            x ^= i
        checksum = f"{x:02x}"
        print(f"The checksum is {checksum}")
except:
    print(f"No file named {file_name} could be found")