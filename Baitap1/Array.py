array = ['1','2']

# array [3] =18 # Thay doi gia tri phan tu thu 4 cua mang
# tuple1 = (1,2,"ga",4,5) # không the thay doi gia tri phan tu trong tuple
# #array1 = array[1::2] # array1 [start:end:step] 
print(int(array[1])) # In ra phan tu thu 2 cua mang
# #array.insert(10,60)# thêm phan tu 60 vao vi tri thu 10, neu vi tri lon hon do dai mang thi no se them vao cuoi mang
# array.append(100) # them phan tu 10 vao cuoi mang
# #print(array.count(1)) # Dem so lan xuat hien cua phan tu trong mang 
# arary_test = list("python") # Chuyen doi chuoi thanh mang ['p', 'y', 't', 'h', 'o', 'n']
# print(arary_test)

# -----------------------disctionary-----------------------
# dict1 = {
#     "name":"Nguyen Van A",
#     "age":20, 
#     "address":"Hanoi"
#     }    
#print(dict1) # In ra toan bo dictionary {'name': 'Nguyen Van A', 'age': 20, 'address': 'Hanoi'}
#print(dict1["name"]) # In ra gia tri cua KEY name: Nguyen Van A

#print(dict1.keys()) # In ra tat ca cac KEY trong dictionary) dict_keys(['name', 'age', 'address'])
#print(dict1.values()) # In ra tat ca cac Values trong dictionary dict_values(['Nguyen Van A', 20, 'Hanoi'])


#print("name" in dict1) # Kiem tra KEY name co trong dictionary khong? True
#print("ga " in dict1)# Kiem tra KEY name co trong dictionary khong? False


# dict1.update({
#     "name": "Tran Thi B",
# })

# print(dict1.get("name")) # In ra gia tri cua KEY name: Tran Thi B
# print(dict1["age"]) # In ra gia tri cua KEY age: 20

# for value in dict1.items():
#     print(value)


# items = []

# quality = int(input("input quality of product: "))

# for i in range(quality):
#     name = input("Nhap ten san pham: ")
#     price = int(input("Nhap gia san pham: "))
#     quantity = int(input("Nhap so luong san pham: "))
#     details = {
#         "product_name": name,
#         "price": price,
#         "quantity": quantity,
#         "total_price": price * quantity
#         }
#     items.append(details)

# for i in items:
#     print(f' Procduct name: {i["product_name"]}  Price: {i["price"]}  Quality: {i["quantity"]}  Total: {i["total_price"]} ')


#for i in range(quality):
    #print (f'-Product {i+1}: {items[i]["product_name"]}    Price: {items[i]["price"]}     Quantity: {items[i]["quantity"]} Total price: {items[i]["total_price"]}')
    
#print(f"Ten san pham: {name} "f"Gia: {price} " f"So luong: {quantity}")
#print (f'Ten san pham: {items[0]} ' f'Gia: {items[0]} ' f'So luong: {items[0]}')
#print (f'Ten san pham: {items[0]["product_name"]}    ' f'Gia: {items[0]["price"]} ' f'So luong: {items[0]["quantity"]} ' f'Tong tien: {items[0]["total_price"]}')
#print (f'Ten san pham: {items[1]["product_name"]}    ' f'Gia: {items[1]["price"]} ' f'So luong: {items[1]["quantity"]} ' f'Tong tien: {items[1]["total_price"]}')    

print("Ket thuc chuong trinh")