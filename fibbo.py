a=eval(input("enter  the range"))
i=0
first_value=0
second_value=1
while(i<a):
    if(i<=1):
        next=i
    else:
        next=first_value+second_value
        first_value=second_value
        second_value=next
        print(next)
    i=i+1
