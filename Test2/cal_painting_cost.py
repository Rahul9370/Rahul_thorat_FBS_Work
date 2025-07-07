#

side = int(input("Enter side length of interior wall :"))
cost = int(input("Enter cost of painting per meter :"))

area = side * side 
cost_of_one_wall = area * cost
total_cost = cost_of_one_wall * 4

print("Total cost of painting the interior wall is: ", total_cost)