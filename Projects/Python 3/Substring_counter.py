def count_substring(user, sub_string):
	count = 0
	for i in range(0,15,3):
           if sub_string in user:
           	count += 1
	print (count)
	
count_substring("azcbobobegghakl", "bob")