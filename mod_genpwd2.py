def genpwd2(size):
    import random as rd
    num1=rd.randint(0,25)
    num2=rd.randint(0,25)
    num3=rd.randint(0,9)
    password=""
    upperCase=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    lowerCase=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    numbers=[0,1,2,3,4,5,6,7,8,9]
    all_characters=upperCase+lowerCase+numbers
    password=password+upperCase[num1]
    password=password+lowerCase[num2]
    password=password+str(numbers[num3])
    for i in range(0,size-3,1):
        num4=rd.randint(0,61)
        password=password+str(all_characters[num4])
        list1=list(password)
        rd.shuffle(list1)
        pwd="".join(list1)
    print("Your password is:",pwd)
