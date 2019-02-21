

def clean_file_list(filenames, keys_to_remove):
	for filename in filenames:
		with open(filename, 'r+') as f:
			lines = f.readlines()
			lines_to_keep = lines

			print(len(lines_to_keep))

			for key in keys_to_remove:
				lines_to_keep = [line for line in lines_to_keep if no_listed_key_at_line_start(keys_to_remove, line)]

			print(len(lines_to_keep))

			f.seek(0)
			f.write("".join(lines_to_keep))
			f.truncate()


def no_listed_key_at_line_start(list_of_keys, line):
	for key in list_of_keys:
		if line[:len(key)].lower() == key.lower():
			return False
	return True


def remove_single_synonyms_from_file(filename):
	with open(filename, 'r+') as f:
		lines = f.readlines()

		lines_to_keep = lines
		i = 0
		while i < len(lines_to_keep):
			synonyms_en = lines_to_keep[i+1].strip().split(', ')
			synonyms_es = lines_to_keep[i+2].strip().split(', ')
			# print(synonyms_en)
			# print(synonyms_es)
			if len(synonyms_en) < 2 and len(synonyms_es) < 2:
				# print('about to remove ' + "".join(lines_to_keep[i:i+5]))
				lines_to_keep = lines_to_keep[:i] + lines_to_keep[i+5:]
			else:
				# print('about to keep ' + "".join(lines_to_keep[i:i+5]))
				i += 5

		f.seek(0)
		f.write("".join(lines_to_keep))
		f.truncate()


clean_file_list([
	'./data/fruits_in_us_counties.txt',
	'./data/fruits_in_mx_counties.txt',
	'./data/fruits_in_es_counties.txt',
	'./data/fruits_in_uk_counties.txt',
	'./data/veggies_in_us_counties.txt',
	'./data/veggies_in_es_counties.txt',
	'./data/veggies_in_uk_counties.txt',
	'./data/veggies_in_mx_counties.txt'
	],
	[
	'asia',
	'United States',
	'Santa Barbara County',
	'Genus',
	'africa',
	'cuisine',
	'americas',
	'family (biology)',
	'Mediterranean',
	'Neolithic',
	'Vegetable',
	'Botanical',
	'List of',
	'West Indies',
	'Colombia',
	'International Standard Book Number',
	'Plant',
	'Central America',
	'Temperate',
	'Mesoamerica',
	'Tropics',
	'Habitat',
	'Latin America',
	'India',
	'Eating',
	'Subarctic',
    'Central America',
    'Maypop',
	])


# remove_single_synonyms_from_file('./data/all_vegetables_synonyms.txt')
