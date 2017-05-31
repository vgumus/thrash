def beverages (coke_amount = 0, tea_amount = 0, coffee_amount = 0, juice_amount = 0):
    coke_price = 2.5
    tea_price = 1.5
    coffee_price = 3.0
    juice_price = 2.0

    total_coke = coke_amount * coke_price
    total_tea = tea_amount * tea_price
    total_coffee = coke_amount * coffee_price
    total_juice = juice_amount * juice_price

    sum_all = total_juice + total_coffee + total_tea + total_coke

    print ("Coke =  {}".format(total_coke),
            "\nTea  = {}".format(total_tea),
           "\nCoffee  = {}".format(total_coffee),
           "\nJuice  = {}".format(total_juice),
           "\nTotal = {}".format(sum_all))

    return (total_coke , total_tea, total_coffee, total_juice, sum_all)

beverages(2,2,2,2)