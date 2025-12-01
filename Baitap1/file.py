# #open('text.txt', 'x') 
# # with open('text.txt', 'a') as f:
# #     f.write("if you speak your mind, then people think you're rude\n")
# #     f.write("if you stay quiet, then you're a coward\n")
# #file = open('text.txt', 'r')
# # print(file.readline())
# # print(file.readlines())
# file = open('text.txt', 'w')
# #file.write("ifyou're successful, then you will win some unfaithful friends\n")
# file.writelines(["ifyou're successful, then poeple think you're arrogant\n","if you're struggling, then you're just lazing\n"])
# file.close()    

# file = open('text.txt', 'a')
# #file.write("ifyou're successful, then you will win some unfaithful friends\n")
# file.writelines(["if you wear nice clothes, then poeple think you're showing up\n","if you wear simple clothes, then you're poor\n"])
# file.close()


# file = open('text.txt', 'r')

# print(file.read())
# file.close()

# with open('text.txt', 'r') as f: 
#     print(f.read())


# # Dữ liệu mẫu
# data = [
#     ['Name', 'Age', 'City'],
#     ['An', 25, 'Hanoi'],
#     ['Binh', 30, 'Ho Chi Minh City'],
#     ['Chi', 28, 'Da Nang']
# 



# import csv
# # Ghi dữ liệu vào file CSV
# with open('data.csv', 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)

# print("Đã tạo file CSV thành công.")

# import csv

# # Dữ liệu dạng dict
# data = [
#     {'Name': 'An', 'Age': 25, 'City': 'Hanoi'},
#     {'Name': 'BBinh', 'Age': 30, 'City': 'Ho Chi Minh City'},
#     {'Name': 'Chi', 'Age': 28, 'City': 'Da Nang'}
# ]

# with open('data1.csv', 'w', newline='', encoding='utf-8') as file:
#     fieldnames = ['Name', 'Age', 'City']
#     writer = csv.DictWriter(file, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerows(data)
# print("CSV file is created successfully with dictionary data.")



# import csv

# with open('data.csv', 'r', encoding='utf-8') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)




content = input("Input any text to write :")
file_name = input("Input file name to write (default is file.txt):")
if not file_name:
    file_name = "file.txt"

def write_to_file(filename, text):
    with open(filename,"w") as f:
        f.write(text)

write_to_file(file_name, content)
with open(file_name, 'r') as file:
    print(file.read())