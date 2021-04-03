words = "All the best for your exam"
arr_words=words.split(" ")
Str=[]

for i in range(len(arr_words)):
	if (i==0 or i==len(arr_words)-1):
		Str.insert(i, arr_words[i])
	else:
		Str.insert(i, "".join(reversed(arr_words[i])))

print(" ".join(Str))


