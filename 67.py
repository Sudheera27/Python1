def quiz1(fname):
    score=[]
    feedback=""
    s1="What is the capital of "
    s2="? "
    s3="You have scored marks of "
    f1=open(fname,"r")
    for i in range(0,5,1):
        str1=f1.readline().replace("\n","")
        list1=str1.split(",")
        question=s1+list1[0]+s2
        answer=list1[1]
        response=input(question)
        if response.lower() == answer.lower():
            score.append(10)
        else:
            score.append(0)
            feedback=feedback+question+"- "+answer+"\n"
    feedback="\n"+s3+str(sum(score))+"\n"+feedback
    return feedback
print(quiz1("Capitals.txt"))

