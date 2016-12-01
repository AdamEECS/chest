towns = [
    {'name': 'Manchester', 'population': 58241},
    {'name': 'Coventry', 'population': 12435},
    {'name': 'South Windsor', 'population': 25709},
]

print(list(zip(*[(t.get('name'), t.get('population')) for t in towns])))


def get_value(key, lists):
    return list(map(lambda t: t.get(key), lists))


print(get_value('name', towns))
print(get_value('population', towns))
