import json


def build_distribution_dict(foods, places_objs):
    distribution = {k: {'key': k, 'image': img, 'places': []} for k,img in foods.items()} # main_key --> [ (coord, names), (coord, names) ...]
    for place in places_objs:
        for key, synonyms in place.foods.items():
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
