def compute_order_total(order):
    total = 0
    for item in order["items"]:
        total += item["price"] * item["quantity"]
    return total

def compute_all_totals(orders):
    totals = []
    for order in orders:
        single_total = compute_order_total(order)
        totals.append(single_total)
    return totals

order_1 = {
    "customer_name": "Alex",
    "items": [
        {"name": "Pikachu Card", "price": 2.50, "quantity": 2},
        {"name": "Deck Sleeves", "price": 5.00, "quantity": 1}
    ]
}

order_2 = {
    "customer_name": "Sam",
    "items": [
        {"name": "Charizard Holo", "price": 180.00, "quantity": 1}
    ]
}

test_orders = [order_1, order_2]
print("All Order Totals:", compute_all_totals(test_orders))

# Empty list of orders
print("Empty:", compute_all_totals([]))

# One order with no items
empty_items_order = {"customer_name": "Taylor", "items": []}
print("One empty:", compute_all_totals([empty_items_order]))