s = "BANANA"


def minion_game(string):
	n = len(string)
	# string = string.lower()
	# kevin_substring = []
	# stuart_substring = []
	# for i in range(1,n+1):
	# 	for j in range(n - i +1):
	# 		substring = string[j:j+i]
	# 		if substring[0] in ["a","e","i","o","u"]:
	# 			kevin_substring.append(substring)
	# 		else:
	# 			stuart_substring.append(substring)
	# kevin_dict = {}
	# stuart_dict = dict()
	# for i in kevin_substring:
	# 	if i in kevin_dict:
	# 		kevin_dict[i] += 1
	# 	else:
	# 		kevin_dict[i] = 1
	# for i in stuart_substring:
	# 	if i in stuart_dict:
	# 		stuart_dict[i] += 1
	# 	else:
	# 		stuart_dict[i] = 1
	# kevein_score = 0
	# stuart_score = 0
	# for i in stuart_dict.values():
	# 	stuart_score += i
	# for i in kevin_dict.values():
	# 	kevein_score += i

	# if kevein_score > stuart_score:
	# 	print("Kevin {}".format(kevein_score))
	# elif kevein_score < stuart_score:
	# 	print("Stuart {}".format(stuart_score))
	# else:
	# 	print("Draw")
	kevein_score = 0
	stuart_score = 0
	vowel = "AEIOU"
	for i in range(n):
		
		if string[i] in vowel:
			kevein_score += len(string)-1
			print(kevein_score)
		else:
			stuart_score += len(string) -1
	if kevein_score > stuart_score:
		print("Kevin {}".format(kevein_score))
	elif kevein_score < stuart_score:
		print("Stuart {}".format(stuart_score))
	else:
		print("Draw")









minion_game(s)