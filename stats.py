def word_counter(file_content):
        """
	Counts number of words:
        Takes file_contents as str:argument,
        returns int:count
        """
        word_list = file_content.split()
        count = 0
        for word in word_list:
                count += 1
        return count


def character_counter(text_string):
	"""
	Counts characters in string:
	Takes text_string as str:argument,
	returns dictionary of {'char' : int} 
	where char is the character forced lower and int is the number of occurences
	"""
	char_count = {}
	char_str_lower = text_string.lower()
	for char in char_str_lower:
		if (char in char_count):
			char_count[char] += 1
		else:
			char_count[char] = 1
	return char_count

def sort_on(items):
	"""
	Takes a dictionary and returns the value of the "char" key
	"""
	output_list = []
	char_count_dict = {}
	for key, value in items.items():
		output_list.append({ "char" : key , "num" : value })
	return output_list
