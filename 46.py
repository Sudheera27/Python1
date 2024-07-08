s1="Dear $1salutation $2name, You are kindly requested to make a payment of $3amount by $4date"
s2=s1.replace("$1salutation","Mr.").replace("$2name","James").replace("$3amount","1000").replace("$4date","01-Apr-2020")
print(s2)
