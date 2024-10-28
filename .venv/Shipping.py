GS_FlatCharge = 20.00
Premium_GS = 125.00
Drone_Shipping_FC = 0.00
weight = 41.5
#“Ground Shipping”
if weight <= 2.0:
  print( "Ground Shipping $" + str(weight * 1.50 + GS_FlatCharge))
elif weight > 2 and weight <= 6:
  print( "Ground Shipping $" + str(weight * 3.00 + GS_FlatCharge))
elif weight > 6 and weight <= 10:
  print( "Ground Shipping $" + str(weight * 4.00 + GS_FlatCharge))
elif weight > 10:
  print("Ground Shipping $" + str( weight * 4.75 + GS_FlatCharge))

#Ground Shipping Premium
print("Premium Ground shipping charges $"+ str(weight + Premium_GS))

#Drone Shipping
if weight <= 2.0:
  print( "Drone Shipping $" + str(weight * 4.50 + Drone_Shipping_FC))
elif weight > 2 and weight <= 6:
  print( "Drone Shipping $" + str(weight * 9.00 + Drone_Shipping_FC))
elif weight > 6 and weight <= 10:
  print( "Drone Shipping $" + str(weight * 12.00 + Drone_Shipping_FC))
elif weight > 10:
  print( "Drone Shipping $" + str(weight * 14.25 + Drone_Shipping_FC))