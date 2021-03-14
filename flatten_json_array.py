from typing import List

input = {
    'a': [
        1,
        2,
        3
    ],
    'b': {
        'a': 1,
        'b': 2,
        'c': 3
    },
    'c': [
        {
            'a': 1,
            'b': 2,
            'c': 3
        },
        {
            'a': 1,
            'b': 2,
            'c': 3
        },
        {
            'a': 1,
            'b': 2,
            'c': 3
        }
    ]
}


def child(key, item):
    if item is None: return

    return_items = []
    if type(item) == list:
        for i, li in enumerate(item):
            new_key = str(i) if key == '' else key + '.' + str(i)
            return_items += child(new_key, li)
    elif type(item) == dict:
        for ckey in item.keys():
            new_key = ckey if key == '' else key + '.' + ckey
            return_items += child(new_key, item[ckey])
    else:
        return_items = [[key, item]]

    return return_items


items = child('', input)

print(items)
