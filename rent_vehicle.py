import datetime

class VehicleRent:
    def __init__(self, stock): 
    
        self.stock = stock
        self.now = 0

    def DisplayStock(self): 

        print("{} vehicle available to rent".format(self.stock))
        return self.stock

    def RentHourly(self, n): 

        if n <= 0:
            print("Number should be positive")
            return None

        elif n > self.stock:
            print("Sorry {} vehicle available to rent".format(self.stock))
            return None
        else:
            self.now = datetime.datetime.now()
            print("Rented a {} vehicle for hourly at {} hours ".format(n, self.now.hour))

            self.stock -= n
            return self.now

    def RentDaily(self, n):

         if n <= 0:
            print("Number should be positive")
            return None

         elif n > self.stock:
            print("Sorry {} vehicle available to rent".format(self.stock))
            return None
 
         else:
            self.now = datetime.datetime.now()
            print("Rented a {} vehicle for daily at {} hours ".format(n, self.now.hour))

            self.stock -= n
            return self.now


    def ReturnVehicle(self, request, brand): 
        """
            return a bill
        """
        car_h_price = 10
        car_d_price = car_h_price * 8 /10 *24
        bike_h_price = 5
        bike_d_price = bike_h_price * 7 / 10 *24

        rentalTime , rentalBasis , numOfVehicle = request
        bill = 0

        if brand == "car":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime

                if rentalBasis == 1 : #hourly 
                    bill = rentalPeriod.seconds/ 3600 * car_d_price * numOfVehicle
                elif rentalBasis == 2 : #daily
                    bill = rentalPeriod.seconds/ (3600*24) * car_d_price * numOfVehicle

                if (2 <= numOfVehicle):
                    print("You have extra %20 discount ")
                    bill = bill * 0.8

                print("Thank you for returning your car")
                print("Price: $ {} ".format(bill))
                return bill
        elif brand == "bike":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime

                if rentalBasis == 1 : #hourly 
                    bill = rentalPeriod.seconds/ 3600 * bike_d_price * numOfVehicle
                elif rentalBasis == 2 : #daily
                    bill = rentalPeriod.seconds/ (3600*24) * bike_d_price * numOfVehicle

                if (4 <= numOfVehicle):
                    print("You have extra %20 discount ")
                    bill = bill * 0.8

                print("Thank you for returning your bike")
                print("Price: $ {} ".format(bill))
                return bill
        else:
            print("You do not  rent a vehicle")
            return None 
        
        self.car = 0
        self.rentalBasis_c = 0 
        self.rentalTime_c = 0


    def RequestVehicle(self , brand):
        """
            take a request  bike or car from customer
        """

        if brand == "bike":
            bikes = input("How many bikes would you like to rent ? ")
            
            try:
                bikes = int(bikes)
            except ValueError:
                print("Number should be Number")
                return -1
            if bikes < 1:
                print("Number of Bikes should be greater than zero !!")
                return -1
            else :
                self.bikes = bikes
            return self.bikes

        elif brand == "car":
            cars = input("How many cars would you like to rent ?")

            try:
                cars = int(cars)
            except ValueError:
                print("Number should be Number ")
                return -1

            if cars < 1 :
                print("Number of cars should be greater than zero !!")
                return -1
            else:
                self.cars = cars
            return self.cars
          
        else:
            print("Request vehicle ERROR")

    def ReturnVehicle(self , brand):
        
        if brand == "bike":
            if self.rentalTime_b and self.rentalBasis_b and self.bikes:
                return self.rentalTime_b, self.rentalBasis_b, self.bikes
            else:
                return 0,0,0
        elif brand == "car":
            if self.rentalTime_c and self.rentalBasis_c and self.cars:
                return self.rentalTime_c, self.rentalBasis_c, self.cars
            else:
                return 0,0,0

        else:
            print("Return vehicle ERROR !!") 

class CarRent(VehicleRent):
    global discount_rate
    discount_rate = 15

    def __init__(self, stock):
        super().__init__(stock)
    def discount(self, b):
        bill = b - (b * discount_rate) / 100
        return bill

class BikeRent(VehicleRent):
    def __init__(self, stock):
        super().__init__(stock)

class Customer:
    def __init__(self):
        
        self.bikes = 0
        self.rentalBasis_b = 0
        self.rentalTime_b = 0

        self.cars = 0
        self.rentalBasis_c = 0
        self.rentalTime_c = 0


    def RequestVehicle(self, brand):

        if brand == "bike":
            bikes = input("How many bikes would you like to rent ? ")
            
            try:
                bikes = int(bikes)
            except ValueError:
                print("Number should be Number")
                return -1
            if bikes < 1:
                print("Number of Bikes should be greater than zero !!")
                return -1
            else :
                self.bikes = bikes
            return self.bikes

        elif brand == "car":
            cars = input("How many cars would you like to rent ?")

            try:
                cars = int(cars)
            except ValueError:
                print("Number should be Number ")
                return -1

            if cars < 1 :
                print("Number of cars should be greater than zero !!")
                return -1
            else:
                self.cars = cars
            return self.cars
          
        else:
            print("Request vehicle ERROR")

    def ReturnVehicle(self , brand):
        
        if brand == "bike":
            if self.rentalTime_b and self.rentalBasis_b and self.bikes:
                return self.rentalTime_b, self.rentalBasis_b, self.bikes
            else:
                return 0,0,0
        elif brand == "car":
            if self.rentalTime_c and self.rentalBasis_c and self.cars:
                return self.rentalTime_c, self.rentalBasis_c, self.cars
            else:
                return 0,0,0

        else:
            print("Return vehicle ERROR !!")
        