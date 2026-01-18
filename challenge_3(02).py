def min_boats(weights, priority, limit):
   people = sorted(zip(weights, priority))
   left, right = 0, len(people)-1
   boats = 0
   while left <= right:
      if left != right and people[left][0] + people[right][0] <= limit and not (people[left][1] and people[right][1]):
         boats += 1
         left += 1
         right -= 1
      else:
         boats += 1
         right -= 1
   return boats
# Test cases
print(min_boats([30,50,60,40,70,80],[1,0,1,0,0,1],100))
print(min_boats([40,40,40],[0,0,0],80))
print(min_boats([90,20,20],[1,0,0],100))