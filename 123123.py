string1 = 'wtf'
string2 = 'brick quz jmpy veldt whangs fox'
w = string2.find(string1[0])
t = string2.find(string1[1])
f = string2.find(string1[2])
result = string2[min(w, t, f):max(w, t, f) + 1]
print(result)
