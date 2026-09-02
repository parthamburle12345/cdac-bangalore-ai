# def calculate_cafeteria_bill(base_price, *items, tax_rate=0.05, discount=0.0, delivery_fee=0.0):
#     total_price = sum((base_price,*items))
#     total_price*=(1-(discount/100)) #formula given 
#     total_price+=(total_price*tax_rate)
#     total_price+=delivery_fee
#     return f"{total_price:.2f}"


# total1 = calculate_cafeteria_bill(100.00)
# total2 = calculate_cafeteria_bill(100.0, 20.0, 30.0, tax_rate=0.08, discount=10.0, delivery_fee=15.0)
# print(total1)
# print(total2)

def calculate_cafeteria_bill(base_price, *items, tax_rate=0.05, discount=0.0, delivery_fee=0.0):
    subtotal = sum((base_price,*items))
    subtotal = (subtotal*(1-(discount/100)))
    subtotal+=(tax_rate*subtotal)
    subtotal = subtotal + delivery_fee
    return f"{subtotal: .2f}"

total1 = calculate_cafeteria_bill(100.00)
total2 = calculate_cafeteria_bill(100.0, 20.0, 30.0, tax_rate=0.08, discount=10.0, delivery_fee=15.0)
print(total1)
print(total2)