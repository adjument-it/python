import os
os.system('cls')
import sys


class Employee:
    employees = []
    
    def __init__(self, name, position, telephone, email):
        self.name = name
        self.position = position
        self.telephone = telephone
        self.email = email
        
    @classmethod
    def add_employee(cls, employee):
        cls.employees.append(employee)

    @classmethod
    def remove_employee(cls, employee):
        cls.employees.remove(employee)
    
    @classmethod    
    def print_employee_data(cls, employee, output_file=None):
        data = f"Employee Data:\nName: {employee.name}\nPosition: {employee.position}\nTelephone: {employee.telephone}\nEmail: {employee.email}"

        if output_file:
            with open(output_file, 'w') as file:
                file.write(data)
        else:
            print(data)
            
    
    @classmethod
    def load_employees_from_file(cls, file_name):
        with open(file_name, 'r') as file:
            for line in file:
                name, position, telephone, email = line.strip().split(',')
                cls.add_employee(Employee(name, position, telephone, email))

    @classmethod
    def print_all_employees(cls):
        for employee in Employee.employees:
            Employee.print_employee_data(employee)
            print()

#############################CLASS DELIMITER #############################

class Vehicle:
    vehicles = []
    def __init__(self, producer, year_of_production, model, cost, pot_selling_price):
        self.producer = producer
        self.year_of_production = year_of_production
        self.model = model
        self.cost = cost
        self.pot_selling_price = pot_selling_price
        
    @classmethod
    def add_vehicle(cls, vehicle):
        cls.vehicles.append(vehicle)

    @classmethod
    def remove_vehicle(cls, vehicle):
        cls.vehicles.remove(vehicle)

    @classmethod    
    def print_vehicle_data(cls, vehicle, output_file=None):
        
        data = f"Vehicle Data:\nProducer: {vehicle.producer}\nYear of production: {vehicle.year_of_production}\nModel: {vehicle.model}\nCost: {vehicle.cost} \nPotential selling price: {vehicle.pot_selling_price}"

        if output_file:
                with open(output_file, 'w') as file:
                    file.write(data)
        else:
            print(data)

    @classmethod
    def load_vehicles_from_file(cls, file_name):
        with open(file_name, 'r') as file:
            for line in file:
                producer, year_of_production, model, cost, selling_price = line.strip().split(',')
                cls.add_vehicle(Vehicle(producer, int(year_of_production), model, int(cost), int(selling_price)))

    @classmethod
    def print_all_vehicles(cls):
        for vehicle in Vehicle.vehicles:
            Vehicle.print_vehicle_data(vehicle)
            print()

#############################CLASS DELIMITER #############################

class Sales:
    saleslist = []
    def __init__(self, employee, vehicle, date_of_selling, real_selling_price):
        self.employee = employee
        self.vehicle = vehicle
        self.date_of_selling = date_of_selling
        self.real_selling_price = real_selling_price


    @classmethod
    def add_sale(cls, sale):
        cls.saleslist.append(sale)

    @classmethod
    def remove_sale(cls, sale):
        cls.saleslist.remove(sale)


    @classmethod
    def print_sales_data(cls, sale, output_file=None):
        data = f"Sales Data:\nEmployee: {sale.employee.name}\nSold vehicle: {sale.vehicle.model}\nSold model: {sale.model}\nDate of selling: {sale.date_of_selling} \nReal selling price: {sale.real_selling_price}"

        if output_file:
            with open(output_file, 'w') as file:
                file.write(data)
        else:
            print(data)


    @classmethod
    def load_sales_from_file(cls, file_name):
        with open(file_name, 'r') as file:
            for line in file:
                employee_name, vehicle_model, date_of_selling, real_selling_price = line.strip().split(',')
                employee = next((e for e in Employee.employees if e.name == employee_name), None)
                vehicle = next((v for v in Vehicle.vehicles if v.model == vehicle_model), None)
                if employee and vehicle:
                    cls.add_sale(Sales(employee, vehicle, date_of_selling, int(real_selling_price)))

    @classmethod
    def print_all_sales(cls):
        for sale in Sales.saleslist:
            Sales.print_sales_data(sale)
            print()




'''
############################# SOLUTION #############################

'''

def main():
	print()


# Loading data from files
Employee.load_employees_from_file('employees.txt')
Vehicle.load_vehicles_from_file('vehicles.txt')
Sales.load_sales_from_file('sales.txt')


# Adding and Removing Records

print()

employee001 = Employee("Elcs Eszter", "igazgató", "06901234567", "admin@hungary.com")
employee002 = Employee("Beviz Elek", "mérnök", "06907654321", "info@hungary.com")

Employee.print_employee_data(employee001)
print()
employee_data_file_name = "employee_data.txt"
Employee.print_employee_data(employee002, output_file=employee_data_file_name)
print(f"Employee data saved to {employee_data_file_name}")
# Employee.remove_employee(employee002)
print()


vehicle1 = Vehicle("Honda", 2021, "Accord", 3600000, 4500000)
Vehicle.add_vehicle(vehicle1)
sale2 = Sales(employee002, vehicle1, "2023-01-21", 21000)
# Sales.remove_sale(sale2)
print("-" * 60)
Employee.print_all_employees()
print("-" * 60)
Vehicle.print_all_vehicles()
print("-" * 60)
Sales.print_all_sales()


if __name__ == '__main__':
    sys.exit(main())