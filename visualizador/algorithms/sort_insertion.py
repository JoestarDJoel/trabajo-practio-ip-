# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}
items = []
n = 0
i = 0
j = None
def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1
    j = None

def step():
    global i, j, n, items
    if i >= n:
        return {"done": True}
    if j is None:
        j = i
        return {"a": j, "b": j, "swap": False, "done": False}
    elif j > 0 and items[j-1] > items[j]:
        a = j - 1
        b = j
        items[a], items[b] = items[b], items[a]
        j -= 1
        return {"a": a, "b": b, "swap": True, "done": False}
    else:
        i += 1
        j = None
        if i < n:
            j = i
            return {"a": j, "b": j, "swap": False, "done": False}
        else:
            return {"done": True}