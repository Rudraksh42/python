month = ("January" , "Feburary", "March" , "April" , "May" , "June" ,"July" , "August" , "september","October" , "November" , "December")
profit = (140000,30009,13324,89686,34668,97673,43782,16786,323452,85767,24245,65672)


max_profit = max(profit)
print(max_profit)
max_profit_index = profit.index(max_profit)
print(max_profit_index)

max_pr_month = month[max_profit_index]
print(max_pr_month)
print("maxium profit of " + str(max_profit) + " was recorded in " + str(max_pr_month) )


min_profit = min(profit)
print(min_profit)
min_profit_index = profit.index(min_profit)
print(min_profit_index)

min_pr_month = month[min_profit_index]
print(min_pr_month)
print("minimum profit of " + str(min_profit) + " was recorded in " + str(min_pr_month))
