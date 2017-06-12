# 8-12. Sandwiches

def make_sandwich(*ingredients):
	"""Print the ingredients in the sandwich"""
	print ("Making a sandwich with the following ingredients:")
	for ingredient in ingredients:
		print("\t- " + ingredient)
	print("\n")


make_sandwich("Flatbread", "American Cheese", "Green Peppers")
make_sandwich("Italian bread", "Swiss cheese", "Avocado", "Mustard")
make_sandwich("Carrots")
