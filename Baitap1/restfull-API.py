import requests
Response = requests.get('https://api.restful-api.dev/objects')
data = Response.json()

def key (key_name):
    if key_name is None or key_name == "":
        return data 
    temp = []
    for i in data:
        if key_name.lower() in i['name'].lower():
            temp.append(i)
    return temp
key_name = input("Input product name to search (or press Enter to show all): ")
data = key (key_name)

print("------------List of products:------------")
#count = 0
id_temp = []
for i in data:
    print(f"{i['id']} - {i['name']}")
    id_temp.append(int(i['id']))
    #count += 1
#print(f"Total products: {count}")

while True:
    user_input = input("Input product ID to see details: ")
    if user_input.isdigit(): #check if input is a number
        product_id = int(user_input)
        if product_id in id_temp:
            break
        else:
            print("Invalid product ID. Please enter a number of the list above.")
    else:
        print("Please enter a valid number.")

# product_id = int(input("Input product ID to see details: "))
# if product_id <1 or product_id > count:
#     print("Invalid product ID")
#     exit()
Response = requests.get('https://api.restful-api.dev/objects/'+ str(product_id))
#Response = requests.get('https://api.restful-api.dev/objects/2')
data = Response.json()
# #print("ID   Name         Color      Capacity")
# #print(f" {data["id"]} {data["name"]}        {data["data"]["color"]}        {data["data"]["capacity"]} ")  
data_details = []
if data["data"] is  None:
    print(f" {data["id"]} {data["name"]} Empty " )  
else :
    for obj in data["data"]:
        data_details.append(data["data"][obj])
    #print(f"{data["data"][obj]}")  
    print("ID   Name                           Detail")
    print(f"{data["id"]}    {data["name"]}     {data_details[0]}     {data_details[1]}  ")  

print("------------End of the program------------")