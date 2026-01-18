def alert_basic(temp, K):
   n = len(temp)
   result = [0]*n
   for i in range(n):
        for j in range(i+1, n): 
            if temp[j] >= temp[i] + K or temp[j] <= temp[i] - K: 
                result[i] = j 
                break   
     return result