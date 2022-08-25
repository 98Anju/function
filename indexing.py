# a="1,2,3,4,5,6,7,8,9,10,11,12,13,23"

#variable name[starting index:last index+1:step]
# print(a[16:3:-4])# 1,4,7
# 2,4,6,8
#3,6,9
#odd 1 ,3,5,7,9
# 9,7,5,3
# print(a[0:len(a):2])
#a[0starting value ka index hai:last index+1 lenth barabar hota hai]
# a=int(input("enter roman no."))
# i=0
# while i<a:
#     if a>i:
#         i=i+1
#     print()

# a="i hate you coding 1,3, 8,9" 
# print(a[len(a)-1:0:-1]) 
# print(a[16:1:-2])
#nut
#coeh
#uoy
#etah
# step 1  g
# step 2 16-2=14  i
# step 3 14-2=12                                                                                                                                                         
#coding
#cdn
#gnidoc uoy
# 16 index g uske baad 16 index step ke baad jayega step se + ho jayega (16+-1)
# a=input(":enter any thing")
# b=a[len(a)-6:len(a):1]
# # c=len("anju")
# user=input("enter")
# c=len(user)
# # b=a[len(a)-1]#a[anju(a)]
# print(c)
# print(a[len(a)-4:len(a)])

# a=5
# b=complex(a)
# print(b)


# def fun(**a):
#     print(a)
# fun(a=2,b=3,c=4,d=5,e=6)

# def fun(*a):
#     print(a)
# # fun(2,3,4,5,6,7,8)
# def fun(a,b,c=9):
#     print(a,b,c)
# fun(6,7)



# a= int(input("enter any number"))
# b=int(input("enter any number"))
# y=1
# while y<=10:
#         print(a,"*",y,"=",a*y)
#         print(b,"*",y,"=",b*y)
#         y=y+1
        
#     # print(a)
#     # print(b)

# i=1
# e=''
# o=''
# while i<10:
# 	if i%2==0:
# 		e+=str(i)
# 		e+='\n'
# 	else:
# 		o+=str(i)
# 		o+='\n'
# 	i+=1
# print('even')
# print(e)
# print('odd')
# print(o)



# a=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# b=0
# for i in a:
# 	b=b+1
# print(b)


# a=[2,3,4,5,67,1,9]
# i=0
# min=0
# while i<=a:
# 	if a[i]<min:
# 		min=a[i]
# 	i=i+1
# print(min)


# a=[5,78,90,548]
# i=0
# m=0
# mini=a[i]
# while i<len(a):
#     if a[i]<mini:
#         m=a[i]
#         t=i
#     i=i+1
# print(m,t)


def mini_num():
    a=[4,78,1,90,548]
    i=0
    m=0
    mini=a[i]
    while i<len(a):
        if a[i]<mini:
            m=a[i]
            t=i
        i=i+1
    print(m,t)
mini_num()

# a=[4,78,60,90,548]
# i=0
# m=0
# t=0
# mini=a[i]
# while i<len(a):
#     if a[i]<mini:
#         m=a[i]
#         t=i
#     i=i+1
# print(m,t)


