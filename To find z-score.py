from statistics import NormalDist
m = int(input("Enter the mu"))
s = int(input("Enter the sigma"))
dis = NormalDist(mu = m,sigma=s)
print("Select the distribution \n1.Probability distribution function\n2.Cumulative distribution function")
sel= int(input())
if(sel ==1):
    print("If u need from infinity to Particular value give -1")
    data1 = int(input("Enter the data 1 :"))
    data2 = int(input("Enter the data 2 :"))
    if(data1 == -1 or data2 == -1):
        if data1==-1:
            print(0-dis.pdf(data2))
        else:
            print(dis.pdf(data1))
            
    else:
        print(dis.pdf(data2)-dis.pdf(data1))
    
if(sel ==2):
    print("If u need from infinity to Particular value give -1")
    data1 = int(input("Enter the data 1 :"))
    data2 = int(input("Enter the data 2 :"))
    if(data1 == -1 or data2 == -1):
        if data1==-1:
            print(0-dis.cdf(data2))
        else:
            print(dis.cdf(data1))
    else:
        print(dis.cdf(data2)-dis.cdf(data1))
