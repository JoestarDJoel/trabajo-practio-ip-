items = []
n = 0
i = 0
j = 0
se_intercambio = False

def init(vals):
    global items, n, i, j, se_intercambio
    items = list(vals)
    n = len(items)
    i = 0
    j = 0
    se_intercambio = False

def step():
    global i, j, n, items,  se_intercambio
    if i >= n - 1:
        return {"done": True}
    if j >= n - 1 - i:
        if not se_intercambio:
            i = n - 1
            return {"done": True}
        i += 1
        j = 0
        se_intercambio = False

    a = j
    b = j + 1
    swap = False

    if b < n:
        if items[a] > items[b]:
            items[a], items[b] = items[b], items[a]
            swap = True
            se_intercambio = True

    j += 1

    return {"a": a, "b": b, "swap": swap, "done": False}