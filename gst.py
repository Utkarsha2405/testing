leather_wallet = {
  "name":"leather wallet",
  "unit_price" : 1100,
  "GST" : 18,
  "Quantity": 1
}
Umbrella = {
"name":"Umbrella",
  "unit_price" : 900,
  "GST" : 12,
  "Quantity": 2
}
Cigarette = {
"name":"cigarette",
  "unit_price" : 200,
  "GST" : 28,
  "Quantity": 3
}

Honey = {
"name":"honey",
  "unit_price" : 100,
  "GST" : 0,
  "Quantity": 4
}

shopping_cart={
	"product1":leather_wallet,
    "product2":Umbrella,
    "product3":Cigarette,
    "product4":Honey
    }
    
print(shopping_cart)


#count total price to be paid 
total_price = sum(d['unit_price'] for d in shopping_cart.values() if d)
print(total_price)

#minimum GST
min_gst= min(shopping_cart, key=lambda x: shopping_cart[x]['GST'])
print(shopping_cart[min_gst]["name"])
