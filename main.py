import matplotlib.pyplot as pt
from matplotlib import style 
from mpl_toolkits import mplot3d
import numpy as np
fig=pt.figure()
pt.style.use("dark_background")
ax = fig.add_subplot(111, projection='3d')

class Vector:
    def __init__(self, x,y,z ,b_x=[1,0,0],b_y=[0,1,0],b_z=[0,0,1]):
        self.b_x=b_x;
        self.b_y=b_y;
        self.b_z=b_z;
        self.basis_matrice=np.array([b_x,b_y,b_z])
        self.vector_matrice=np.array([[x],[y],[z]])
        self.transformed_matrices=np.dot(self.basis_matrice,self.vector_matrice)
        self.origin=[0,0,0]
        
        
    def give_ordinates(self):
        vec_ordinate=[self.x, self.y, self.z]
        return vec_ordinate
    def plot_vector(self):
            ax.quiver(*self.origin ,*self.transformed_matrices, 
                color='w', arrow_length_ratio=0.1)
    def plot_basis(self):
        
        ax.quiver(*self.origin, *self.basis_matrice,color="r",arrow_length_ratio=0.1)
        
       
        

        
        
        
    def __mul__(self,other):
        axes={"x":self.x*other.x,"y":self.y*other.y,"z":self.z*other.z}
        result= int(axes["x"])+int(axes["y"])+int(axes["z"])
        
        print(result)


v1= Vector(2,3,4,[0,2,0],[3,0,0],[0,5,4])
v2= Vector(4,5,6)

v1.plot_basis();
# v2.plot_basis();
v1.plot_vector();
# v2.plot_vector();
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
ax.set_zlim([0, 10])


pt.show()