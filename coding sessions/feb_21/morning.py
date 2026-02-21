
# * prime no. between 500
def Q1() :
    listt = []
    for i in range(2,500):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            listt.append(i)
    print(listt)

# Q1()


# * DYNAMIC list of prime no...
def Q2() :
    la = int(input("what is the max len of prime in between you want :"))
    listt = []
    for i in range(2,la):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            listt.append(i)
    print(listt)

# Q2()



# *  Armstrong no.:

def Q3():
    num = int(input("give a no. to check wether it is a armstrong no.. :"))
    snum = str(num)
    lnum = len(snum)
    sum = 0
    for i in snum :
        inum = int(i)
        sum =  sum+(inum **lnum)
        
    if sum == num :
        print("True")
    else :
        print("false")
    


# Q3()


# * WAP list of ARM number from given range:
def Q4():
    listt = []
    num1,num2 =map( int , input("give a no. to check wether it is a armstrong no.. :").split())
    for j in range(num1,num2):
        snum = str(j)
        lnum = len(snum)
        sum = 0
        for i in snum :
            inum = int(i)
            sum =  sum+(inum **lnum)
            
        if sum == j :
            listt.append(j)
        else:
            continue
    print(listt)


Q4()

