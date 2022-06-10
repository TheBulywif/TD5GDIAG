def center(a, b):
    var = ""
    x = len(a)
    i = 0
    while i < ((b - x) / 2):
        var += " "
        i += 1
    i = 0
    var += a
    while i < ((b - x) / 2):
        var += " "
        i += 1
    while len(var) != b:
        if len(var) > b:
            var = var[:-1]
        if len(var) < b:
            var += " "
    return var
