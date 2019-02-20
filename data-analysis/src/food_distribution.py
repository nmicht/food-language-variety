import json

def get_food_keys(filenames):
	distribution = {}
	for filename in filenames:

		with open(filename, 'r') as f:
			lines = f.readlines()

		i = 0
		while i < len(lines):
			key = lines[i].strip().lower()
			distribution[key] = lines[i+3].strip()
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


def build_distribution(foods, places_objs):
	distribution = {k: {'key': k, 'image': img, 'places': []} for k,img in foods.items()} # main_key --> [ (coord, names), (coord, names) ...]
	for place in places_objs:
		for key, synonyms in place.foods:
			if len(synonyms) > 0:
				synonyms = json.loads(synonyms)
			key = key.lower()
			if key in distribution:
				if len(place.coords.split(', ')) < 2:
					place.coords = 'None, None'
				distribution[key]['places'].append({'name': place.name, 'lat': place.coords.split(', ')[0],
					'lng': place.coords.split(', ')[1], 'synonyms': synonyms})

	return distribution


def write_distribution_to_file(dist, savepath):
	with open(savepath, 'w') as f:
		for k, v in dist.items():
			if len(v['places']) >= 3 and len(v['places'][2]) > 0:
				f.write(k.upper() + '\n')
				f.write(v['image'] + '\n')
				for name, coords, synonyms in v['places']:
					f.write(name + '\n')
					f.write(coords + '\n')
					f.write(', '.join(synonyms.split(', ')) + '\n')
				f.write('\n\n')

def write_distribution_to_json_file(dist, savepath):
	with open(savepath, 'w') as outfile:
		s = json.dumps(dist, indent=4, sort_keys=True)
		outfile.write(s)

if __name__ == '__main__':
	x = get_food_keys(['./data/all_fruit_synonyms.txt','./data/all_vegetables_synonyms.txt'])
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

	write_distribution_to_json_file(pobjs, './data/distribution.json')
	#print(len(pobjs))

	#print(pobjs['apple'])
	#print(pobjs['manoao'])