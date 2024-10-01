import matplotlib.pyplot as pt
from matplotlib import style 
from mpl_toolkits import mplot3d
class Vector:
    def __init__(self, x,y,z):
        self.x=x;
        self.y=y;
        self.z=z;
    def give_ordinates(self):
        vec_ordinate=[self.x, self.y, self.z]
        return vec_ordinate
    def __mul__(self,other):
        axes={"x":self.x*other.x,"y":self.y*other.y,"z":self.z*other.z}
        result= int(axes["x"])+int(axes["y"])+int(axes["z"])
        
        print(result)
fig=pt.figure()
pt.style.use("dark_background")
ax = fig.add_subplot(111, projection='3d')

origin=Vector(0,0,0)
v1= Vector(2,3,4)
v2= Vector(4,5,6)
def plot_vector( vls):
    for v in vls:
        ax.quiver(*origin.give_ordinates() ,*v.give_ordinates(), 
            color='r', arrow_length_ratio=0.1)
        
plot_vector([v1,v2])
print(*origin.give_ordinates())
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
ax.set_zlim([0, 10])


pt.show()