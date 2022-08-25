
# def rev_num():
    # a= ["A", "N", "N", "U", "F", "R", "O", "M", "D","E","L","H","I"]
    # i=0
    # while i<len(a):
    #     i+=1
    # print(a[-1::-1])
# rev_nu

# def subject(dic,i):
# 	for value in dic.values():
# 		i=0
# 		sum=0
# 		while i<len(value):
# 			if i==0:
# 				print(value[i])
# 			i=i+1
# subject({"a":[20,25,30],"b":[95,100,80],"c":[30,40,50]},0)
que_list=["Who Invented computer","Who invented Internet","When was python developed","what is the fullform of www."]
opt_list=[["Vint cerf","Mark Jukerberg","Charls babbage","Robert Vintage"],["Vint cerf","vinton cerf", "Guido","John babbage"],["21 feb","20 feb","20 march","19 jan"],["world web wide","world wide web","world web webside","world wide webside"]]
ans_list=[3,1,2,2]
fifty_list=[["Charls babbage","Robert Vintage"],["vint cef","guido"],["21 feb","20 feb"],["world web wide","world wide web"]]
sol_list=[1,1,2,2]  
lifelinecount = 0
def lifeline(index):  
    global lifelinecount
    j=0 
    if(lifelinecount==0): 
        while j<len(fifty_list[index]):
            print(j+1,fifty_list[index][j])
            j=j+1
        user_ans = int(input('.....'))
        lifelinecount+=1
        if user_ans==sol_list[index]:
            return True
        else:
            return False
    else:
        print('you Already used 5050')
        return "no"
def option(index):
    j=0
    while j<len(opt_list[index]):
        print(j+1,opt_list[index][j])
        j=j+1
    user_ans = int(input('.....'))
    if user_ans==ans_list[index]:
        return True
    if user_ans == 5050:
        return(lifeline(index))
    else:
        return False
def que():
    index=0
    while index<len(que_list):
        print("Q.",index+1,que_list[index],"?")
        result=option(index)
        if result == "no":
            index-=1
        elif result==True:
            print("Congractualtion")
        else:
            print("you Losse !")
            break 
        index+=1
def main():
    que()
main()