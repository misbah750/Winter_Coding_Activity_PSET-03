from collections import Counter
def find_anagrams(s, p):
  if not p:
      return []
  res = []
  p_count = Counter(p)
  s_count = Counter()
  for i in range(len(s)):
      s_count[s[i]] += 1
      if i >= len(p):
          if s_count[s[i-len(p)]] == 1:
              del s_count[s[i-len(p)]]
          else:
              s_count[s[i-len(p)]] -= 1
      if i >= len(p) - 1 and s_count == p_count:
          res.append(i-len(p)+1)
  return res    
# Test cases
print(find_anagrams("cbaebabacd","abc"))
print(find_anagrams("abab","ab"))
print(find_anagrams("aaaaa","aa"))