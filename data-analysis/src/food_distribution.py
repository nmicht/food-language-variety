def get_food_keys(filenames):
	distribution = {}
	for filename in filenames:

		with open(filename, 'r') as f:
			lines = f.readlines()

		i = 0
		while i < len(lines):
			key = lines[i].strip().lower()
			distribution[key] = None
			i += 5

	return distribution





def get_places_with_food_from_file(filepaths):
	places_objs = []

	for filename in filepaths:
		with open(filename, 'r') as f:
			obj_strings = f.read().split('\n\n\n')

			for obj in obj_strings:
				#print(obj)
				new = Place(obj)
				if new.name:
					places_objs.append(new)
				#print(len(places_objs))

	return places_objs

class Place(object):
	def __init__(self, data):
		lines = data.split('\n')
		if len(lines) > 2:
			self.name = lines[0].strip().lower()
			self.coords = lines[1]
			self.foods = []

			for food in lines[2:]:
				key, synonyms = food.lower().split('\t')

				self.foods.append((key, synonyms))
		else:
			self.name = None
			self.coords = None
			self.foods = []

	def __str__(self):
		return 'name: ' + self.name + '\n' + 'coords: ' + self.coords + '\n' + 'foods: ' + str(len(self.foods)) + '\n' + "\n\t".join([k for k,s in self.food])


def build_distribution(food_keys, places_objs):
	print(food_keys)
	distribution = {k: [] for k in food_keys} # main_key --> [ (coord, names), (coord, names) ...]
	for place in places_objs:
		for key, synonyms in place.foods:
			print(key)
			key = key.lower()
			if key in distribution:
				distribution[key].append((place.name, place.coords, synonyms))

	return distribution


def write_distribution_to_file(dist, savepath):
	with open(savepath, 'w') as f:
		for k, v in dist.items():
			if len(v) >= 3 and len(v[2]) > 0:
				f.write(k.upper() + '\n')
				for name, coords, synonyms in v:
					f.write(name + '\n')
					f.write(coords + '\n')
					f.write(', '.join(synonyms.split(', ')) + '\n')
				f.write('\n\n')

if __name__ == '__main__':
	x = get_food_keys(['./data/all_fruit_synonyms.txt','./data/all_vegetables_synonyms.txt']).keys()
	# print(len(x))
	
	places_objs = get_places_with_food_from_file([
		'./data/fruits_in_us_counties.txt',
		'./data/fruits_in_es_counties.txt',
		'./data/fruits_in_mx_counties.txt',
		'./data/fruits_in_uk_counties.txt',
		'./data/veggies_in_us_counties.txt',
		'./data/veggies_in_es_counties.txt',
		'./data/veggies_in_uk_counties.txt',
		'./data/veggies_in_mx_counties.txt'
	])

	print(len(places_objs))

	pobjs = build_distribution(x, places_objs)

	write_distribution_to_file(pobjs, './data/distribution.txt')
	#print(len(pobjs))

	#print(pobjs['apple'])
	#print(pobjs['manoao'])