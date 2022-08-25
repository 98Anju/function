# def sort_num():
#     a=[6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
#     a.sort()
#     print(a)
# sort_num()


a=[2,5,20,22,32,12]
i=0
list=[]
while i<len(a):
    j=0
    while j<len(a):
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
        j=j+1
    i=i+1
print(a)




