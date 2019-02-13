



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
    while i < len(lines):
        key = lines[i].strip()
        synonyms_en = lines[i+1].strip().split(', ')
        synonyms_es = lines[i+2].strip().split(', ')
        img_link = lines[i+3]
        i += 5
        if len(synonyms_en) < 2 and len(synonyms_es) < 2:
        	pass
        else:
        	

        entries[key] = (synonyms_en, synonyms_es, img_link)

    return entries


clean_file_list([
	'./data/fruits_in_es_counties.txt',
	'./data/fruits_in_mx_counties.txt',
	'./data/fruits_in_uk_counties.txt',
	], 
	[
	'asia',
	'africa',
	'cuisine', 
	'americas', 
	'family (biology)',
	'Mediterranean',
	'Neolithic',
	'Vegetable',
	'List of',
	'West Indies',
	'Colombia',

	])