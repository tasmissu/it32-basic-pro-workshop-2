quantity =  int(input("จำนวนปืนที่รับมาขาย : "))
cost_price = float(input("ต้นทุนปืนที่รับมา : "))
sell_price = float(input("ราคาที่จะนำไปขายต่อ: "))
team_members = int(input("จำนวนลูกน้องในทีมที่ไปทำงาน: "))

profit = quantity * (sell_price - cost_price)
total_income = sell_price * quantity
boss = profit * 0.2
team_shere = (profit - boss) / team_members
print(f"ได้กำไรรวม: {profit}")
print(f"บอสได้: {boss}")
print(f"ลูกน้องที่เข้าร่วมปฎิบัติการได้: {team_shere}")