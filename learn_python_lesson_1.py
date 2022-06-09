import random

lst = ["banana", "apple", "avocado"]

x, y, z = lst

print(x)
print(y)
print(z)

def tester():
    x = "plum"
    print("The other fruit: ", x)

tester()

print("The other fruit: ", x)

print(random.randrange(1, 10))

quantity = 3
price_each_IP = 500

online_order = "I want to pay {0} $ for {1} pieces of item."

print(online_order.format(quantity * price_each_IP, quantity))

dict_1 = {
    "brand": "Honda",
    "model": "CR-V",
    "year" : 2011
}

x = dict_1.items()
print(x)

i = 1
while i < 10:
    print(i)
    i += 1
else:
    print("i is no longer in range 1 to 9")

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

myit = iter(lst)

print(next(myit))
print(next(myit))
print(next(myit))
