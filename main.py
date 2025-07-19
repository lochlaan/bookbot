# Killian 7/19/2025
#
# Python Bookbot w/ Boot.dev
from stats import word_counter, character_counter, sort_on
import sys

def get_book_text(path_to_file):
	"""
	Takes file path as str:argument,
	returns str:file_contents
	"""
	with open(path_to_file) as f:
		file_content = f.read()
		return file_content

def main():
	# Checks if sys.argv does not have 2 entries, inform proper usage and exit w/ status code: 1
	if (len(sys.argv) != 2):
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	book_dir = sys.argv[1]
	book_text = get_book_text(book_dir)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_dir}")
	print("----------- Word Count ----------")
	print(f"Found {word_counter(book_text)} total words")
	print("--------- Character Count -------")
	sorted_list = sorted(character_counter(book_text).items(), key=lambda x: x[1], reverse=True)


	for char, count in sorted_list:
		if (char.isalpha()):
			print(f"{char}: {count}")

	print("============= END ===============")
main()
