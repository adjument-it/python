import os
os.system('cls')
import sys
from datetime import datetime


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


    @classmethod
    def all_sale_of_date(cls, specific_date):
        count_per_date = 0
        for sale in cls.saleslist:
            if sale.date_of_selling == specific_date:
                count_per_date += 1
        return count_per_date
    
    # to_day = datetime.now().day
    # to_month = datetime.now().month
    # to_year = datetime.now().year

    @classmethod
    def get_date_components(cls, date_string):
        year, month, day = map(int, date_string.split('-'))
        return year, month, day


    @classmethod
    def sales_in_timeframe(cls, start_date, end_date):
        start_year, start_month, start_day = cls.get_date_components(start_date)
        end_year, end_month, end_day = cls.get_date_components(end_date)

        count_per_timeframe = 0
        for sale in cls.saleslist:
            sale_year, sale_month, sale_day = cls.get_date_components(sale.date_of_selling)
            if (
                start_year <= sale_year <= end_year and
                start_month <= sale_month <= end_month and
                start_day <= sale_day <= end_day
            ):
                count_per_timeframe += 1

        return count_per_timeframe
    

    @classmethod
    def full_profit(cls, start_date, end_date):
        count_in_timeframe = cls.sales_in_timeframe(start_date, end_date)
        
        total_profit  = 0
        for sale in cls.saleslist:
            sale_year, sale_month, sale_day = cls.get_date_components(sale.date_of_selling)
            if (
                start_year <= sale_year <= end_year and
                start_month <= sale_month <= end_month and
                start_day <= sale_day <= end_day
            ):
                total_profit += 1 (sale.real_selling_price - sale.vehicle.cost)
            
        return count_in_timeframe * total_profit

   
    # @classmethod
    # def most_demanded_vehicle(cls, start_date, end_date):
    #     vehicle_counts = {}
        
    #     for sale in cls.saleslist:
    #         sale_year, sale_month, sale_day = cls.get_date_components(sale.date_of_selling)
    #         if (
    #             start_date <= sale.date_of_selling <= end_date
    #         ):
    #             vehicle_model = sale.vehicle.model
    #             vehicle_counts[vehicle_model] = vehicle_counts.get(vehicle_model, 0) + 1

    #     most_demanded_vehicle = max(vehicle_counts, key=vehicle_counts.get)
    #     return most_demanded_vehicle


'''
############################# SOLUTION #############################
'''

def main():
    print("############################# SOLUTION #############################")
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



    # Count all vehicle sales for a specific date
    print("Count all vehicle sales for a specific date")
    input_date = '2023-08-31'
    counter = Sales.all_sale_of_date(input_date)
    print(f"Total vehicle sales on {input_date} is: {counter}")

    print("-" * 60)
    
    # Count sales within a specific timeframe
    print("Count sales within a specific timeframe:")
    date_a = '2023-03-01'
    date_z = '2023-03-31'
    count_in_timeframe = Sales.sales_in_timeframe(date_a, date_z)
    print(f"Total vehicle sales between {date_a} and {date_z} is: {count_in_timeframe}")
    print("-" * 60)

    # Calculate profit within a specific timeframe
    print("Calculate profit within a specific timeframe:")
    date_1 = '2023-03-01'
    date_n = '2023-03-31'
    profit = Sales.full_profit(date_1, date_n)
    print(f"Total profit between {date_1} and {date_n} is: {profit}")
    print("-" * 60)

    # print("The most demanded vehicle within a specific timeframe:")
    # # The most demanded vehicle within a specific timeframe

    # most_demanded = Sales.most_demanded_vehicle(date_1, date_n)
    # print(f"Most demanded vehicle between { date_1} and {date_n} is: {most_demanded}")
    # print("-" * 60)


if __name__ == '__main__':
    sys.exit(main())