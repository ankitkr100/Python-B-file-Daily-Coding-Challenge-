def first_non_repeating_charecter(str1):
	char_order = []
	ctr = {}
	for c in str1:
	    if c in ctr:
	        ctr[c] += 1
	    else:
	    	ctr[c] = 1
	    	char_order.append(c)
	for c in char_order:
		if ctr[c] == 1:
			return c 
	return None 

print(first_non_repeating_charecter('abcdef'))
print(first_non_repeating_charecter('abcabcdef'))
print(first_non_repeating_charecter('aabbcc'))