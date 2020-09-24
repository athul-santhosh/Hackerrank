# forming a magic sqaure 

l = [[5 ,3 ,4],[1,5,8],[6,4,2]]
l1 = [] 
for i in l:
	l1 = l1 + i
print(l1)


# get all matrics in the magic square format

"""
 a.   b.    c
 d.    e.    f 
 g.     h.    i

""" 
p = 15
# l2 = [[a,b,c,d,e,f,g,h,i] for a in range(1,10) for b in range(1,10) for c in range(1,10) for d in range(1,10) 
# 		for e in range(1,10) for f in range(1,10) for g in range(1,10) for h in range(1,10) for i in range(1,10)
# 		if a + b + c == p and d + e + f == p  and g + h + i == p and a + d + g == p  and b + e + h == p and c + f + i == p 
# 		and a + e + i == p and c + e + g == p and len(set([a,b,c,d,e,f,g,h,i])) == 9] 

l3 = [[2, 7, 6, 9, 5, 1, 4, 3, 8], [2, 9, 4, 7, 5, 3, 6, 1, 8], [4, 3, 8, 9, 5, 1, 2, 7, 6], [4, 9, 2, 3, 5, 7, 8, 1, 6], [6, 1, 8, 7, 5, 3, 2, 9, 4], [6, 7, 2, 1, 5, 9, 8, 3, 4], [8, 1, 6, 3, 5, 7, 4, 9, 2], [8, 3, 4, 1, 5, 9, 6, 7, 2]]
p = []
for i in l3:
	a = [abs(i[j] - l1[j]) for j in range(9)]
	p.append(sum(a))
print(p)
print(min(p))


