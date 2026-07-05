def add_tax(amount):
    total_with_tax = amount * 1.10
    return total_with_tax


def add_tip(amount):
    tip_added = amount * 1.15
    return tip_added


def format_total(amount):
    total_formatted = f"Your total is ${amount:.2f}"
    return total_formatted


def main():
    base_price = 50
    price_after_tax = add_tax(base_price)
    final_total = add_tip(price_after_tax)
    formatted_total = format_total(final_total)
    print(formatted_total)


main()