foods = []
prices = []
total = 0

try:
  while True:
    items = input("Enter a Food you  want to add (press Q or No to quit): ")
    if items.capitalize() == "Q" or items.capitalize() == "No":
      break
    else:
      foods.append(items)
      price = input(f"Enter the price of {items} रु.")
      prices.append(price)

  for mulya in prices:
    total += float(mulya)

  print("—————Your Cart—————")
  for f in range(0, len(foods)):
    if f == (len(foods) -1):
      print(foods[f])
    else:
      print(foods[f], end=', ')
  

  print(f"Your Total = रु.{total:.2f}")

except:
  print('Something Went Wrong')
  
