class Vector:
    def __init__(self, x,y,z):
        self.x=x;
        self.y=y;
        self.z=z;
    def display(self):
        print(f"x:{self.x},y:{self.y},z:{self.z}")
    def __mul__(self,other):
        axes={"x":f"{self.x*other.x}","y":f"{self.y*other.y}","z":f"{self.z*other.z}"}
        result= int(axes["x"])+int(axes["y"])+int(axes["z"])
        
        print(result)
            


v1= Vector(2,3,4)
v2= Vector(4,5,6)
v1*v2
