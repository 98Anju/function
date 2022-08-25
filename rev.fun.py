# def max_num():
#     a=[12,34,506,67,69,9]
#     i=0
#     max=0
#     while i<len(a):#o<6 1<6 2<6 3<6 4<6 5<6
#         b=a[i]# b=a[0]==12 34 56 67 69 9
#         if b>max: # 12>0 true 34>12 56>34 67>56 69>56 969
#             max=b # max=12 34 56 67 69
#         # print(b)#12 34 56 67 69
#         i+=1
#     return max    # 0+=1 1+=1 1+=2  1+=3 1+=4

# print(max_num())


# def max_num():
#     if len(a)==1:
#         return a[0]
#     max=max(a[1:])
#     if a[0] >max:
#         return a[0]  
#     else:
#         return max
# a=[12,34,506,67,68,9]
# print(max_num())

# question set 2
# Write function here
# def function_name():
#     def function_name():
#         print("sonu","monu")
#         function_name()
# function_name()
# print("welcome")
# print("sonu")
# print("monu")



def add(a,b):
    c=a+b
    return c
def sub(s,g):
    d=s-add(10,5)
    return d
def mult(m,h):
    e=m*h
    return e
def div(v,y):
    k=v%y
    return k
def main(a,b):
    return mult(5,6)
j=main(5,6)
print(j)