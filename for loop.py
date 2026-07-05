raw_scores = [" Alice : 10 ", "bob:7", "  CHARLIE:  3"]

#helper function to clean the data
def clean_score(raw):
    name_part, score_part = raw.split(":")
    name = name_part.strip().lower()
    score = int(score_part.strip())
    return name, score
#empty list
cleaned_scores = []
#for loop to call the function and add the cleaned data to the empty list
for raw in raw_scores:
    cleaned_result = clean_score(raw)
    cleaned_scores.append(cleaned_result)
print(cleaned_scores)
#loop outside the function
def apply_discount(price):
    return int(price * 0.8)

prices = [100, 250, 50]

discounted_prices = []

for price in prices:
    discount = apply_discount(price)
    discounted_prices.append(discount)

print(discounted_prices)

#loop inside the function
def apply_discount(price):
    return int(price * 0.8)


# 1. Create the new function that accepts a list
def apply_discount_list(prices):
    # 2. Inside here, build the empty list and run the loop
    discounted_prices = []
    for price in prices:
        discount = apply_discount(price)
        discounted_prices.append(discount)

    # 3. Return the final list back to the caller
    return discounted_prices


# 4. Outside the functions, set up your data and call it
prices = [100, 250, 50]
discounted_prices = apply_discount_list(prices)
print(discounted_prices)