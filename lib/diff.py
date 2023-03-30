def diff_list(new_data, old_data, key_func):
    output = {
        "add": [],
        "remove": [],
    }
    for new in new_data:
        for old in old_data:
            if key_func(new) == key_func(old):
                break
        else:
            output["add"].append(key_func(new))
    for old in old_data:
        for new in new_data:
            if key_func(new) == key_func(old):
                break
        else:
            output["remove"].append(key_func(old))
    return output


def diff_dict(new_data, old_data):
    output = {
        "add": [],
        "remove": [],
    }
    for new in new_data.keys():
        for old in old_data.keys():
            if new == old:
                break
        else:
            output["add"].append(new)
    for old in old_data.keys():
        for new in new_data.keys():
            if new == old:
                break
        else:
            output["remove"].append(old)
    return output
