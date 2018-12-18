print("Simple Assignment")
shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist 只是指向同一对象的另一种名称

mylist = shoplist

del shoplist[0]

print("shoplist:", shoplist)
print("mylist:", mylist)
# 注意到 shoplist 和 mylist 二者都
# 打印出了其中都没有 apple 的同样的列表，以此我们确认
# 它们指向的是同一个对象


print('Copy by making a full slice')
mylist = shoplist[:]
# 删除第一个项目
del mylist[0]
print("shoplist:", shoplist)
print("mylist:", mylist)
