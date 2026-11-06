a=open("C:/Users/user/Downloads/Dannye_dlya_testovogo_zadania.csv",encoding="utf-8")
lines=a.readlines()
a.close()
header = lines[0].strip().split(",")
i_id     = header.index("order_id")
i_date   = header.index("order_date")
i_sku    = header.index("sku")
i_qty    = header.index("quantity")
i_price  = header.index("price")
i_status = header.index("status")
seen_orders = []          
orders = {}               
revenue = {}
for line in lines[1:]:
    line = line.strip()
    if line == "":
        continue

    parts = line.split(",")
    order_id = parts[i_id].strip()  
    if order_id in seen_orders:
        continue
    seen_orders.append(order_id)  
    quantity = parts[i_qty].strip()
    if quantity == "":
        continue
    sku   = parts[i_sku].strip()
    date   = parts[i_date].strip()
    price  = int(parts[i_price].strip())
    status = parts[i_status].strip().lower()
    if status == "canceled":
            status = "cancelled"

        
    key = (sku, date)

        
    if key in orders:
        orders[key] = orders[key] + 1
    else:
        orders[key] = 1

        
    if status == "delivered":
        money = int(quantity) * price
        if key in revenue:
            revenue[key] = revenue[key] + money
        else:
            revenue[key] = money


keys = list(orders.keys())
keys.sort()


out = open("daily_by_sku.csv", "w", encoding="utf-8")
out.write("sku,order_date,orders,revenue\n")

for key in keys:
    sku = key[0]
    date = key[1]
    o = orders[key]

    if key in revenue:
        r = revenue[key]
    else:
        r = 0
    out.write(sku + "," + date + "," + str(o) + "," + str(r) + "\n")

out.close()

print("Готово! Результат в daily_by_sku.csv")