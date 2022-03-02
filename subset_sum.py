#this program will say true is subset sum is present and False if not pResent
#problem url -  https://www.geeksforgeeks.org/subset-sum-problem-dp-25/

# cook your dish here
t=[[]]
arr=[2,3,8,10]
sum = 5
t = [[False for j in range(sum+1)] for j in range(len(arr)+1)]

for i in range(len(arr)+1):
    for j in range(sum+1):
        if i ==0:
            t[i][j]=False
        if j == 0:
            t[i][j]=True
#print(t)            

for i in range(len(arr)+1):
    for j in range(sum+1):
        if arr[i-1]>j:
            t[i][j] = t[i-1][j]
        else:
            t[i][j] =  t[i-1][j-arr[i-1]] or t[i-1][j]
#print(t)
print(t[len(arr)][sum])
