shoplist = ["apple", "banana", "pear", "mango"]

print("i hava", len(shoplist), "item to purchase")

print("this item are:", end=" ")
for item in shoplist:
    print(item, end=" ")


print("\nI also have to buy rice.")
shoplist.append("rice")
print('My shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)