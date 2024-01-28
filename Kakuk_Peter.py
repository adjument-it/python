'''
Vizsga feladat1:

Létre kell hozni egy alkalmazást autók eladásának rögzítéséhez egy autókereskedésben.
A fő feladat: számbavenni az autók eladásának folyamatát,
rögzíteni az eladást végrehajtó munkatársat, kiszámolni a bevételt.
A következő információ tárolása szükséges:

Munkatárs:
 NÉV
 Beosztás
 Telefon
 Email

Gépjármű:
 Gyártó neve
 Gyártás éve
 Modell
 Önköltségi ár
 Potenciális eladási ár

Értékesítés:
 Munkatárs
 Gépjármű
 Értékesítés dátuma
 Tényleges eladási ár

A következő funkciókat (függvényeket) kell megírni:

 Hozzáadás, törlés, munkavállalói információk
 Hozzáadás, törlés, gépjármű információk
 Hozzáadás, törlés, értékesítési információk
 Jelentések.


Az adatok a képernyőn vagy egy fájlban jeleníthetők meg,
a felhasználó választásának függvényében.
o Teljes körű információ a cég alkalmazottairól
o Teljes körű információ a gépjárművekről
o Teljes körű információ az értékesítésről
o Egy bizonyos dátum összes értékesítése
o Összes értékesítés egy bizonyos időszakban
o Egy adott alkalmazott összes értékesítése
o A legkeresettebb autó neve az adott időszakban
o Információ a legsikeresebb kereskedőről az adott időszakban
o Teljes nyereség az adott időszakban
 Adatok mentése fájlba
 Adatok betöltése fájlból

A feladat megoldható mind függvénnyekkel, mind objektum-orientáltan.
A hallgató választhat.
'''


'''
 


 
'''



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



'''

'''

def main():
	print()


# Adding and Removing Records

employee001 = Employee("Elcs Eszter", "igazgató", "06901234567", "admin@hungary.com")
employee002 = Employee("Beviz Elek", "mérnök", "06907654321", "info@hungary.com")

Employee.print_employee_data(employee001)
file_name = "employee_data.txt"
Employee.print_employee_data(employee002, output_file=file_name)
print(f"Employee data saved to {file_name}")

# Employee.remove_employee(employee002)

vehicle2 = Vehicle("Honda", 2021, "Accord", 18000, 22000)
Vehicle.add_vehicle(vehicle2)
sale2 = Sales(employee002, vehicle2, "2023-01-21", 21000)
# Sales.remove_sale(sale2)



if __name__ == '__main__':
    sys.exit(main())