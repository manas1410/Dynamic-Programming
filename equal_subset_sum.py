'''
problem url - https://www.geeksforgeeks.org/partition-problem-dp-18/
'''
t=[[]]
arr=[1,5,6,11]
sums = sum(arr)
if sums%2!=0:
    print(False)
else:
    
    t = [[False for j in range(sums+1)] for j in range(len(arr)+1)]
    
    for i in range(len(arr)+1):
        for j in range(sums+1):
            if i ==0:
                t[i][j]=False
            if j == 0:
                t[i][j]=True
                
    def subsetsum(arr,sums):
        for i in range(len(arr)+1):
            for j in range(sums+1):
                if arr[i-1]>j:
                    t[i][j] = t[i-1][j]
                else:
                    t[i][j] =  t[i-1][j-arr[i-1]] or t[i-1][j]
        return t[len(arr)][sums] 
      
        
    print(subsetsum(arr,sums))
