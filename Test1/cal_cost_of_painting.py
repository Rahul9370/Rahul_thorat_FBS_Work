# cal the cost of painting  the following building wall's both (interior and exterior). 
# you need to accepth the area and cost of both interior and exterior wall.

length = int(input("Enter length of building wall:"))
cost_per_meter = int(input("Enter cost of painting per meter:"))

area = 2 * length * length           # to find both wall area
cost = 2 * cost_per_meter * area        # to find cost of both walls

print("Cost of painting is:",cost)


