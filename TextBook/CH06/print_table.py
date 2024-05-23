def print_table(table_data):
    max_length = 0
    for table in table_data:
        for item in table:
            max_length = max(max_length, len(item))

    for table in table_data:
        for item in table:
            print(item.rjust(max_length), end=' ')
        print()  


table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)
