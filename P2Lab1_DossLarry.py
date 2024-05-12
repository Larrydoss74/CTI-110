"""
Larry Doss
3/3/24
P2Lab1
Driving Cost
"""

# Input: Gas mileage (miles/gallon) and cost of gas (dollars/gallon)
gas_mileage = float(input("Enter gas mileage (miles/gallon): "))
cost_of_gas = float(input("Enter cost of gas (dollars/gallon): "))

# Calculate gas cost for different distances
distance1 = 20
distance2 = 75
distance3 = 500

# Calculate cost for each distance
cost1 = distance1 / gas_mileage * cost_of_gas
cost2 = distance2 / gas_mileage * cost_of_gas
cost3 = distance3 / gas_mileage * cost_of_gas

# Output the results with two decimal places
print(f"{cost1:.2f} {cost2:.2f} {cost3:.2f}")
