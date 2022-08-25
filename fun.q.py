# def employee(name,salary=20000):
#     print(name,"your salary is:-",salary)
# employee("kartik",30000)
# employee("deepak")

# def primeorNot(num):
#     if num > 1:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 print(num,"is not a prime number")
#                 print(i,"times",num//i,"is",num)
#                 break
#             else:
#                 print(num,"is a prime number")
#     else:
#         print(num,"is not a prime number")
# primeorNot(406)

# def greet(*names):
#     for name in names:
#         print("Hello", name)
# greet("sonu", "kartik", "umesh", "bijender")

# def sumofdigits(number):
#     sum = 0
#     modulus = 0
#     while number!=0 :
#         modulus = number%10
#         sum+=modulus
#         number/=10
#         return sum
# print(sumofdigits(123))




# def  meal(day,time):
#     if day=="sunday":
#         if time=="breakfast":
#             return "dosa"
#         elif time=="lunch":
#             return "dal rice"
#         elif time=="dinner":
#             return "paneer and  chapati"
#         else :
#             return "time not found"
#     elif day=="monday":
#         if time=="breakfast":
#             return "fried rice"
#         elif time=="lunch":
#             return "aloo rice"
#         elif time=="dinner":
#             return "chhole bhature"
#         else :
#             return "time not found"
#     elif day=="other":
#         if time=="breakfast":
#             return "aloo"
#         elif time=="lunch":
#             return "rajma rice"
#         elif time=="dinner":
#             return "veg-chapati"
#         else :
#             return "time not found"
# print(meal("sunday","lunch"))
# print(meal("monday","dinner"))




# def checkKey():
#     car = {"brand":  "ford","model":  "mustang","year" :1996  }
#     if "model" in car:
#         print("Yes, 'model' is one of the keys in the thisdict dictionary.")
#     else:
#         print("No, 'model' key dictionary mai nahi hai.")

# checkKey()



# def calculate_sum(a,b):
#     sum = a+b
#     print(sum)
# calculate_sum(4,5)


# def function_multi(a,b):
#     multiply=a*b
#     return multiply
# print(function_multi(3,5))


# def Avg(number1,number2,number3):
#     avg=number1+number2+number3/3
#     print(sum)
# Avg(1,3,2)


# def voter(age):
#     if age < 18:
#         print("eligible")
#     else:
#         print("not eligible")
# voter(20)


# def distance(kms):
#     if kms < 20:
#         print("close")
#     elif kms < 50:
#         print("median")
#     else:
#         print("far")
# distance(20)

# a=int(input("enter any no."))
# i=1
# while i<=a:
#     if i%7==0 and i%3==0:
#         print(i,"navgurukul")
#     elif i%7==0:
#         print(i,"gurukul")
#     elif i%3==0:
#         print(i,"nav")
#     i=i+1
