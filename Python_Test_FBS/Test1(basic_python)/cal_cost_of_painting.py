# cal the cost of painting  the following building wall's both (interior and exterior). 
# you need to accepth the area and cost of both interior and exterior wall.

length = int(input("Enter length of building wall:"))
cost_per_meter_inner = int(input("Enter cost of inner wall painting per meter:"))
cost_per_meter_outer = int(input("Enter cost of outer wall painting per meter:"))

total_area = 4 * length * length           # to find both wall area
total_cost = total_area * cost_per_meter_inner + total_area * cost_per_meter_outer     # to find cost of both walls
overall_cost = 2 * total_cost

print("Cost of painting is:",overall_cost)


