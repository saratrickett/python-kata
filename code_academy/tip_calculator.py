# Cost of meal: $44.50
# Restaurant tax: 6.75%
# Tip: 15%

meal = 44.50
tax = 6.75 / 100
tip = 15.0 / 100

meal = meal + meal*tax
total = meal + meal*tip

print("%.2f" % total)