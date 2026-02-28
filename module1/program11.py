def calculate_area(shape = 'triangle' , radius = 0 , length= 0 ,width = 0, base = 0, height = 0):

    if shape == 'circle':
        return 3.14 *radius * radius
    elif shape == 'rectangle':
        return length * width
    elif shape == 'triangle':
        return 0.5 * base * height
    



print('area of circle: ',calculate_area(radius=5))
print('area of rectangle: ',calculate_area(length=5,width=4))
print('area of triangle: ',calculate_area(base=6,height=5))