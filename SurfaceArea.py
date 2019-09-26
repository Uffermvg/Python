
# Finds the surface area of a cylinder
# 
Diameter = int (input ("Diameter"))
Height = int (input ("Height"))
def SurfaceArea(Radius , Height):
    import math
    Radius = (Diameter / 2)
    SArea = (2 * math.pi * (Radius ** 2) ) + (2 * math.pi * Radius * Height)
    return (SArea)
    print ("The Surface Area of a cylinder is", SArea ,"for a given diameter of a", Diameter ,"cm and a height of", Height ,"cm")

	
