def add_item_bad(item, box=[]):
    box.append(item)
    return box

# print(add_item_bad("яблоко"))
# print(add_item_bad("банан"))


def add_item_good(item, box=None):

    if box is None:
        box = []

    box.append(item)
    return box


box_1 = ["арбуз"]

print(add_item_good("яблоко", box_1))
print(add_item_good("банан"))