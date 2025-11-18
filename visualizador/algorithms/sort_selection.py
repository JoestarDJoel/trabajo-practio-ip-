items = []
n = 0
i = 0
j = 0
min_indice = 0
fase = "buscar"
def init(vals):
    global items, n, i, j, min_indice, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_indice = i
    fase = "buscar"
def step():
    global i, j, n, items, min_indice, fase
    if i >= n:
        return {"done": True}
    if fase == "buscar":
        if j >= n:
            fase = "swap"
        else:
            a = min_indice
            b = j
            if items[j] < items[min_indice]:
                min_indice = j
            j += 1
            return {"a": a, "b": b, "swap": False, "done": False}
    if fase == "swap":
        idx1 = i
        idx2 = min_indice
        swap_hecho = False
        if min_indice != i:
            items[i], items[min_indice] = items[min_indice], items[i]
            swap_hecho = True
        i += 1
        if i < n:
            j = i + 1
            min_indice = i
            fase = "buscar"
        return {"a": idx1, "b": idx2, "swap": swap_hecho, "done": False}
    return {"done": True}