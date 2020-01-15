def cal_fact(number):
    if(number==1):
        return 1
    else:
        return(number*cal_fact(number-1))
num=5
print(cal_fact(num))
