#!/usr/bin/env python3

#Sal's Shipping

weight = 41.5
ground_cost = ""
ground_cost_premium = 125.00
drone_cost = ""

#Ground Shipping

if weight <= 2:
  ground_cost = weight * 1.5 + 20
elif weight <= 6:
  ground_cost = weight * 3 + 20
elif weight <= 10:
  ground_cost = weight * 4 + 20
else:
  ground_cost = weight * 4.75 + 20

print("Ground Shipping: $",ground_cost)

#Ground Shipping Premium
print("Ground Shipping Premium: $",ground_cost_premium)

#Drone Shipping

if weight <= 2: 
  drone_cost = weight * 4.5
elif weight <= 6:
  drone_cost = weight * 9
elif weight <= 10:
  drone_cost = weight * 12
else:
  drone_cost = weight * 14.25

print("Drone Shipping: $",drone_cost)



