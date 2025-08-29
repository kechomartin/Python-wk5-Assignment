# classes for moving things 
class Mover:
    def move(self):
        
        return "Moving in some way"

# Animal classes
class Dog(Mover):
    def move(self):
        return "Running on four legs"

class Bird(Mover):
    def move(self):
        return "Flying through the air"

class Fish(Mover):
    def move(self):
        return "Swimming in water"

# Vehicle classes
class Car(Mover):
    def move(self):
        return "Driving on the road"

class Plane(Mover):
    def move(self):
        return "Flying at high altitude"

class Boat(Mover):
    def move(self):
        return "Sailing on water"

# Demonstration
if __name__ == "__main__":
    # Create objects from each class
    movers = [
        Dog(),
        Bird(), 
        Fish(),
        Car(),
        Plane(),
        Boat()
    ]
    
    print("=== HOW THINGS MOVE ===")
    for mover in movers:
        # Same method calls different results
        print(f"{mover.__class__.__name__}: {mover.move()}")