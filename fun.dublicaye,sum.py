def dublicate():
    a=[2,4,8,8,7,8,2,3]
    i=0
    b=[]
    while i<len(a):
        if i not in b:
            b.append(a[i])
        i=i+1
    def sum(b2):
        j=0
        sum=0
        while j<len(b2):
            sum=sum+b2[j]
            j=j+1
        print(sum)
    sum(b)
dublicate()



# # a=["geetu","neetu","geeta","seeta",]
# # i=0
# # while i<len(a):
# #     j=0
# #     while j<i:
# #         if a[i]:
# #             j=j+1
# #         i=i+1
# # print(i)

# a="One two double three"
# x = a.split()
# print(x)
 
# # i=1
# # while i<=10:
# #     if i%2==0 or i%2!=0:
# #         print(i)
# #     i=i+1





# # a="one,two dubble three"
# #  .spilit(a)




# a=["geetu","neetu","geeta","geethu"]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     while j<len(a):
#         if a[i]==a[j]and a[j]==a[i]:
#             b.append(a[i][j])
#             j+=1
#         i+=1
#     print(b)



b="ayushi parmaan"
i=0
c=[]
while i<len(b):
    j=0
    while j<len(b):
        if b[i]==b[j]and b[j]==b[i]:
            c.append(b[i][i])
            j+=1
        i+=1
print(c)
            


        





    





















   







        

        






    
