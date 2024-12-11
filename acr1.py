try :
  num = int(input("enter your number:"))
  print(num)
except ValueError as ex:
  print("exeption",ex)

print("i am outside the try block")