# WAP to find the area and perimetre of the following figure(Accept the length,breadth and radius from user:)

length = int(input("Enter length:"))
breadth = int(input("Enter breadth:"))

radius = breadth / 2
area_rectangle = length * breadth
area_half_circle = (3.14 * radius * radius / 2)
area_figure = area_rectangle + area_half_circle
perimeter = (2 * 3.14 * radius / 2)
perimeter_figure = perimeter + breadth + length * 2

print("Area of given Figure is:",area_figure)
print("Perimeter of given figure is:",perimeter_figure)

