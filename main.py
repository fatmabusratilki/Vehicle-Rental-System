"""
Author: Fatma Büşra Tilki
Year: 2022 
Project Name: Vehicle Rental System Simulation
"""

from random import choice
from rent_vehicle import CarRent, BikeRent, Customer

print("hello world")
bike = BikeRent(100)
car = CarRent(10)
customer = Customer()

main_menu = True

while main_menu == True :
    if main_menu :
        print("""
              ***** Vehicle Rental Shop*****
              A. Bike Menu
              B. Car Menu 
              Q. EXIT
              """)
        main_menu = False

        choice = input("Enter Choice : ")

        if choice== "A" or choice == "a":
            print("""
                  *****Bike Menu*****
                  1.Display available bikes
                  2.Request a bike on hourly basis $5
                  3.Request a bike on daily basis $84
                  4.Return a bike 
                  5.Main Menu
                  6.EXIT
                  """)
            choice = input("Enter Choice : ")

            try:
                choice = int(choice)
            except ValueError:
                print("It's not integer")
                continue

            if choice == 1:
                bike.DisplayStock()
                choice = "A"

            elif choice == 2:
                customer.rentalTime_b = bike.RentHourly(customer.RequestVehicle("bike"))
                customer.rentalBasis_b = 1
                main_menu = True
                print("-----------------------------------")
            elif choice == 3:
                customer.rentalTime_b = bike.RentDaily(customer.RequestVehicle("bike"))
                customer.rentalBasis_b = 2
                main_menu = True               
                print("-----------------------------------")
            elif choice == 4:
                customer.bill = bike.ReturnVehicle(customer.ReturnVehicle("bike"),"bike")
                customer.rentalBasis_b, customer.rentalTime_b, customer.bikes = 0,0,0
                main_menu = True
                
            elif choice == 5:
                main_menu = True 

            elif choice == 6:
                break

            else:
                print("Invalid value. Please enter a number 1-6 ")
                main_menu = True

        elif choice == "B" or choice == "b":
            print("""
                  ***** CAR Menu *****
                  1.Display available cars
                  2.Request a car on hourly basis $10
                  3.Request a car on daily basis $192
                  4.Return a car 
                  5.Main Menu
                  6.EXIT
                  """)
            choice = input("Enter Choice : ")

            try:
                choice = int(choice)
            except ValueError:
                print("It's not integer")
                continue

            if choice == 1:
                car.DisplayStock()
                choice == "B"
            elif choice == 2:
                customer.rentalTime_c = car.RentHourly(customer.RequestVehicle("car"))
                customer.rentalBasis_c = 1
                main_menu = True
                print("-----------------------------------")
            
            elif choice == 3:
                customer.rentalTime_c = car.RentDaily(customer.RequestVehicle("car"))
                customer.rentalBasis_c = 2 
                main_menu = True
                print("-----------------------------------")

            elif choice == 4:
                customer.bill = car.ReturnVehicle(customer.ReturnVehicle("car"),"car")
                customer.rentalBasis_c , customer.rentalTime_c , customer.cars == 0,0,0
                main_menu = True

            elif choice == 5:
                main_menu = True

            elif choice == 6:
                break
            
            else:
                print("Invalid value. Please enter a number 1-6 ")
                main_menu = True

        elif choice == "Q" or choice == "q":
            break
        else:
            print("Invalid value. Please enter A or B or Q")
            main_menu = True

        print("Thank You For Using The Vehicle Rental Shop :)")
               