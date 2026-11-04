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