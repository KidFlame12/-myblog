class Vehicles:
    
   car_name1 = "Lamborghini Huracan STO"
   car_name2 = "Bugatti Chiron"
   car_name3 = "Tesla Cyber Truck"
   
   def main(self):
       print("I have the best car here. I have a", self.car_name1)
       print("Oh yeah? Well, I have a", self.car_name2)
       print("Well nine is better than both of your cars, it's a", self.car_name3)
       
       Vehicles_class_object = Vehicles()
       
       print("Your car is:", Vehicles_class_object.car_name2)
       Vehicles_class_object.main()