# Computes alert day for each temperature
def compute_alerts(temp, K):
    n = len(temp)
    warm = [0]*n 
    cold = [0]*n 
    alert = [0]*n
  
    stack = []
    for i in range(n):
        while stack and temp[i] >= temp[stack[-1]] + K:
            warm[stack.pop()] = i
            stack.append(i)
        stack = []
        for i in range(n):
            while stack and temp[i] <= temp[stack[-1]] - K:
                cold[stack.pop()] = i
                stack.append(i)
        stack = []
        for i in range(n):
            candidates = []
            if warm[i] != 0: candidates.append(warm[i])
            if cold[i] != 0: candidates.append(cold[i])
            alert[i] = min(candidates) if candidates else 0
            return alert
# Test cases
print(compute_alerts([73,74,75,71,69,72,76,73],3))
print(compute_alerts([30,40,50,60],5))
print(compute_alerts([80,78,76,74],2))