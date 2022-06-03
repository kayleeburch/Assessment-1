from optimal_change import optimal_change

print("1:", optimal_change(62.13, 100) == "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")
print("2:", optimal_change(31.51, 50) == "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")
print("3:", optimal_change(89.55, 100) == "The optimal change for an item that costs $89.55 with an amount paid of $100 is 1 $10 bill, 1 quarter, and 2 dimes.")
print("4:", optimal_change(2.00, 400) == "The optimal change for an item that costs $2.0 with an amount paid of $400 is 3 $100 bills, 1 $50 bill, 2 $20 bills, 1 $5 bill, and 3 $1 bills.")
print("5:", optimal_change(60.00, 60.00) == "The optimal change for an item that costs $60.0 with an amount paid of $60.0 is no change.")
print("6:", optimal_change(59.99, 60.0) == "The optimal change for an item that costs $59.99 with an amount paid of $60.0 is 1 penny.")
print("7:", optimal_change(70.57, 60) == "The optimal change for an item that costs $70.57 with an amount paid of $60 is not enough to pay for item. Customer still owes $10.57.")
