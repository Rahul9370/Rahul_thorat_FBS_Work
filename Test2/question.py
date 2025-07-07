 """A farmer has a field which is half in circle share and rest rectangle. he needs to do fencing for entire field
using barbed wire 5 times. circular section has a radius of 20 meters and rectangular section length of 50 meters
and breadth of 40 meters. If cost of barbed wire is 35 rupees per meter, calculate the total cost of fencing the field."""

radius = 20  # Radius of the half circular section in meters
length = 50  # Length of the rectangular section in meters
breadth = 40  # Breadth of the rectangular section in meters
wire_cost = 35   # Cost per meter of barbed wire

circular_perimeter = (2 * 3.14 * radius)/2  # Circumference of the half circular section
rectangular_perimeter = 2 * (length + breadth)  # Perimeter of the rectangular section
total_perimeter = circular_perimeter + rectangular_perimeter  # Total perimeter to be fenced
total_cost = total_perimeter * wire_cost * 5  # Total cost for fencing 5 times

print("Total cost of fencing 5 times the field is: ", total_cost)
