def calc1(num1,num2):
    sum1=num1+num2
    dif1=num1-num2
    prd1=num1*num2
    div1=num1/num2
    div2=num1//num2
    rem1=num1%num2
    exp1=num1**num2
    return (sum1,dif1,prd1,div1,div2,rem1,exp1)
    
result=calc1(8,4)
print(result)
