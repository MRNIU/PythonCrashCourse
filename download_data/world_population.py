import json
from country_codes import get_country_code
import pygal_maps_world.maps
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population




cc_pop_1, cc_pop_2, cc_pop_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pop_1[cc] = pop
    elif pop < 1000000000:
        cc_pop_2[cc] = pop
    else:
        cc_pop_3[cc] = pop

print(len(cc_pop_1), len(cc_pop_2), len(cc_pop_3),)

wm_style = RS('#336699', base_style=LCS)
wm = pygal_maps_world.maps.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0 - 10m', cc_pop_1)
wm.add('10 - 1bn', cc_pop_2)
wm.add('> 1bn', cc_pop_3)
wm.render_to_file('world_population.svg')
