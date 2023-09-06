import json

with open('dict.json', encoding='utf-8') as json_file:
    ghosts_dict = json.load(json_file)

def f_comma(my_str, group=3, char=','):
    my_str = str(my_str)
    return char.join(my_str[i:i+group] for i in range(0, len(my_str), group))

def edit(name):
    behavior = ghosts_dict.get(name).get("behavior")
    advantages = ghosts_dict.get(name).get("advantages")
    strategy = ghosts_dict.get(name).get("strategy")
    
    behavior = f_comma(behavior, group = 125, char = '\n')
    advantages = f_comma(advantages, group = 125, char = '\n')
    strategy = f_comma(strategy, group = 125, char = '\n')

    
    