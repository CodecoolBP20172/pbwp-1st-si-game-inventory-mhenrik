# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification
import csv
import operator
# Displays the inventory.


def display_inventory(inventory):
    """Prints the inventory.
    Args:
        inventory in dicitionary format
    Returns:
        None
    """
    print("Inventory:")
    for k, v in inventory.items():  # iterate through the dictionary
        print(v, k)
    print("Total number of items:", sum(
        inventory.values()))  # print sum of values


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    """Add items to the given inventory.
    Args:
        param1: dicitionary representing the inventory
        param2: list of items to be added to the inventory
    Returns:
        The inventory with the added items.
    """
    added_set = set(added_items)  # create a set from the added items
    added_list = list(added_set)  # create a list from the set
    new_added_items = []  # create an empty list for the new items
    for item in added_list:  # iteration through the added list
        # append every unique new elements as a list
        new_added_items.append([item, added_items.count(item)])
    # create a dictionary from the added items
    new_added_items = dict(new_added_items)
    for k, v in new_added_items.items():
        if k in inventory:
            # add values to the keys if already exists
            inventory[k] = inventory[k] + new_added_items[k]
        else:
            inventory[k] = v  # create new dictionary items if not existed
    return inventory


# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    """Print the inventory table in an ordered way.
    Args:
        param1: inventory as a dictionary
        param2: string how the inventory should be sorted
    Returns:
        String right justified
    """
    max_length = []  # create an empty list to determine the max length of a key
    for k, v in inventory.items():
        max_length.append(len(k))  # by the length function
        max_length.append(len(str(v)))
    max_width = max(max_length)  # return the max length
    print("Inventory:")
    print(
        "count".rjust(max_width) +
        "item name".rjust(
            max_width *
            2))  # rjust with 3 times the max_length
    print("".rjust(max_width * 3, "-"))  # rjust with 3 times the max_length
    if order == "count,asc":
        sorted_inv = sorted(inventory.items(), key=operator.itemgetter(1))  # create a sorted list by the values
        for k, v in sorted_inv:  # print out the sorted values
            print(str(v).rjust(max_width) + k.rjust(max_width * 2))
        print("Total number of items:", sum(inv.values()))
    elif order == "count,desc":
        sorted_inv = sorted(
            inventory.items(),
            key=operator.itemgetter(1),
            reverse=True)  # same as above but reversed order
        for k, v in sorted_inv:
            print(str(v).rjust(max_width) + k.rjust(max_width * 2))
        print("Total number of items:", sum(inv.values()))
    else:
        for k, v in inv.items():  # no order
            print(str(v).rjust(max_width) + k.rjust(max_width * 2))
        print("Total number of items:", sum(inv.values()))


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="test_inventory.csv"):
    file = open(filename, newline='')  # open the file in read mode
    reader = csv.reader(file, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)  # load in csv module
    for row in reader:
        data = sorted(row)
    added_set = set(data)  # create a set from the added items
    added_list = list(added_set)  # create a list from the set
    new_added_items = []  # create an empty list for the new items
    for item in added_list:  # iteration through the added list
        inventory[item] = data.count(item)  # populate inventory
    file.close()
    return inventory  # returns the inventory in list


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    """Create a file where all inventory items are stored which could be used for imoporting.
    Args:
        param1: the inventory as a dictionary
        param2: the filename to be used
    Returns:
        None
    """
    file = open(filename, "w", newline='')  # open the file in write mode
    writer = csv.writer(file, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)  # load in writer module
    data = []
    for k, v in inventory.items():  # load in the dictionary
        data.extend([k] * v)
    writer.writerow(data)  # write every line as key+"," multiplied by the value
    file.close()
