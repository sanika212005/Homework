ProductName=input("Name of the Product:")
MRP=float(input("Enter the MRP of the product:"))
Discount_in_percent=float(input("Enter thee Discount on the Product:"))
Discount_in_rupees=MRP*(Discount_in_percent/100)
Selling_price=MRP-Discount_in_rupees

#displaying the Product  data 
print("")
print("Name of the Product:",ProductName)
print("MRP of the Product:",MRP)
print("Discount on the Product",Discount_in_percent)
print("Selling price of the Product:",Selling_price)

 
