total_cost = 0
item_count = 0

for _ in iter(input, ""):
    try:
        price_in_cents = int(float(_) * 100)
        total_cost += price_in_cents
        item_count += 1

    except ValueError:
        print("Invalid input. Please enter a valid price.")

total_cost_dollars = total_cost // 100
total_cost_cents = total_cost % 100

remainder = total_cost % 5
if remainder < 2.5: 
  adjusted_total = total_cost - remainder 
else:
  total_cost + (5 - remainder)

amount_due_dollars = adjusted_total // 100
amount_due_cents = adjusted_total % 100

print("Total cost for" ,item_count, " items: $", total_cost_dollars, ".", round(total_cost_cents,2), sep="")
print("Amount due (cash): $", amount_due_dollars, ".", round(amount_due_cents,2), sep="")
