class Vehicle: 

    def __init__(self, make): 
        self.make = make 


    def move(self): 
        print(f"{self.make} moves") 


    def stop(self): 
        print(f"{self.make} stops")
        

    def __str__(self): 
        return f"Vehicle {self.make}" 


class Train(Vehicle): 
    def move(self): 
        print(f"{self.make} runs on rails")
        

class Plane(Vehicle): 
    def move(self): 
        print(f"{self.make} takes off")
        super().move()
        

    def __str__(self): 
        return f"Plane {self.make}"
    

class Glider(Plane): 
    def stop(self): 
        print(f"{self.make} lands silently")
        

t = Train("Eurostar") 
p = Plane("Airbus") 
g = Glider("Grob") 


t.move() 
t.stop() 
print(t)
p.move() 
print(p) 
g.move() 
g.stop() 
print(g)
print(isinstance(g, Vehicle))
print(isinstance(t, Plane))
print(issubclass(Glider, Train)) 


