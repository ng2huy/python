# class phone:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = 190000 # Fixed price for all phones --> encapsulation of price attribute

#     def make_call(self, number):
#         return f"Calling {number} from {self.brand} {self.model}."

#     def send_message(self, number, message):
#         return f"Sending message to {number}: {message}"
    
# class phone1(phone):# Inheriting from phone class
#     def __init__(self, brand, model, price):
#         super().__init__(brand, model, price)
#         self.model = "Iphone"
#     def make_call(self, number): # Overriding make_call method
#         return f"Calling {number} from {self.brand} {self.model} - Special Edition."    
    

# # Example usage:
# my_phone = phone1("Samsung", "Galaxy S21", 799)
# print(f'Brand: {my_phone.brand} Model: {my_phone.model} Price: {my_phone.price}')  # Output: Samsung Galaxy S21
# print(my_phone.make_call("123-456-7890"))  # Output: Calling 123-456-7890 from Samsung Galaxy S21.
# print(my_phone.send_message("123-456-7890", "Hello!"))  # Output: Sending message to 123-456-7890: Hello!

class employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.__salary = salary  # Private attribute
        self.commission = 1

    def get_salary(self):  # Getter method for salary
        self.total_salary = self.__salary + self.commission*self.__salary

    def set_salary(self, salary):  # Setter method for salary
        if salary >= 0:
            self.__salary = salary
        else:
            return "Salary cannot be negative."
    def get_details(self): # New method specific to manager
        return f"Manager Name: {self.name}, Position: {self.position}, Salary: {self.total_salary}"
# Example usage:
class manager(employee): # Inheriting from employee class
    def __init__(self, name, position, salary):
        super().__init__(name, position, salary)
        self.commission = 0.1 * salary  # Additional attribute for manager
    
class normal_employee(employee): # Inheriting from employee class
    def __init__(self, name, position, salary):
        super().__init__(name, position, salary)
        self.commission = 0.2 * salary  # Additional attribute for manager
    


employee1 = manager("Alice", "Manager", 1)
employee1.get_salary()
employee2 = normal_employee("Bob", "Staff", 1)
employee2.get_salary()
print(employee1.get_details())  # Output: Manager Name: Alice, Position: Manager, Salary: 99000.0 
print(employee2.get_details())  # Output: Manager Name: Bob, Position: Manager, Salary: 72000.0         