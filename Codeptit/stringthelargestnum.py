s = input()
words = []
mp = {}
for i in range(len(s)):
    if(s[i] not in words):
        words.append(s[i])
        mp[s[i]] = 1
    else:
        mp[s[i]] += 1
words.sort(reverse= True)
idx = 0
for i in range(len(s)):
    if(s[i] == words[idx]):
        print(s[i], end="")
    mp[s[i]] -= 1
    while(idx < len(words) and mp[words[idx]] == 0):
        idx += 1

