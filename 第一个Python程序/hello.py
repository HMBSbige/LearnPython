import hashlib

print("Hello,World!\n")

md5 = hashlib.md5()
str1 = input("输入字符串：")
md5.update(str1.encode("utf-8"))
print("md5("+str1+") = ", md5.hexdigest())

print("\nGoodbye")
