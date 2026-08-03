"""Flatten Array"""
def flatten(iterable):
    """Take a nested array and return a flattened array"""
    output = []
    for item in iterable:
        if isinstance(item, list):
            output.extend(flatten(item))
        else:
            output.append(item)

    return [item for item in output if item is not None]
            