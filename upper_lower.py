def sillycase(x):
	return x[:5].lower() + x[:-5].upper()
	
print sillycase(treehouse)