#það hlýtur að vera betri leið til að gera þetta

file_one = input()
file_two = input()

file_one_text = []
file_two_text = []



with open(file_one, "r") as file_one_inn, open(file_two, "r") as file_two_inn: #Bæta við "/src/" á filenames til að þetta virki í kattis
    for line_one in file_one_inn:
        file_one_text.append(line_one)
    for line_two in file_two_inn:
        file_two_text.append(line_two)

def create_text(length, list_one, list_two ):
    complete_text = []
    for i in range(length):
        if i < len(list_one):
            complete_text.append(list_one[i])
        if i < len(list_two):
            complete_text.append(list_two[i])
        else:
            continue
    return complete_text


if len(file_one_text) >= len(file_two_text):
    print_list = create_text(len(file_one_text), file_one_text , file_two_text)
elif len(file_one_text) <= len(file_two_text):
    print_list = create_text(len(file_two_text), file_one_text , file_two_text)

for line in print_list:
    line= line.strip("\n")
    print(line)



#Gamalt

# # with open(file_one, "r") as file_one_inn, open(file_two, "r") as file_two_inn:
# files = [file_one, file_two]
# files_text = []
# for file in files:
#     files = open(file, "r")
#     files_text.append(files)

# for i in files_text:
#     print(files_text[0].read())
#     print(files_text[1].read())
