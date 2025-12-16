# arr = [17,18,5,4,6,1]

# leng = len(arr)-1
# maxi = arr[-1]
# for i in range(leng-1,-1,-1):
#     temp = arr[i]
#     arr[i] = maxi
#     if temp>=maxi:
#         maxi = temp
# arr[-1] = -1
# print(arr)

# bills = [5,5,5,10,5,5,10,20,20,20]
# final_out = True
# lemonade = 5
# cash_register = {5:0,10:0}
# for i in bills:
#     change = i - lemonade
#     if change == 0 :
#         cash_register[i]+=1
#     elif change == 5 :
#         if cash_register[5]>=1:
#             cash_register[i]+=1
#             cash_register[5]-=1
#             final_out = True
#         else:
#             final_out = False
#             break
#     elif change >= 10:
#         if (cash_register[5]>0 and cash_register[10]>0):
#             cash_register[5]-=1
#             cash_register[10]-=1
#             final_out = True

#         elif (cash_register[5]>=3):
#             cash_register[5]-=3
#             final_out = True

#         else:
#             final_out = False
#             break
        
# print(final_out)

# import pandas as pd
# import numpy as np

# data = {'Sales_Person':[1,2,3,4,5],
#         'Product':[1,1,2,1,2],
#         'Regions':['US','IND','UK','IND','US'],
#         'Sales':[1000,500,1200,550,1100]}

# df= pd.DataFrame(data)
# print(df)
# group = df.groupby(['Product','Regions',]).agg({'Sales_Person':'unique','Sales':'sum'})
# print(group)

prices = [7,1,5,3,6,4]
min_price = float('inf')
max_profit = 0
for price in prices:
    if price < min_price:
        min_price = price
    elif price - min_price > max_profit:
        max_profit = price - min_price
print(max_profit)