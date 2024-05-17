def format_list(items):
    if not items:
        return ''
    elif len(items) == 1:
        return items[0]
    else:
        return ', '.join(items[:-1]) + ' and ' + items[-1]

spam = ['apples', 'bananas', 'tofu', 'cats']
print(format_list(spam))

