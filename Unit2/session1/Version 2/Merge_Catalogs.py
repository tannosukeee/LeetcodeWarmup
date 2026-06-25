def merge_catalogs(catalog1, catalog2):
    for key in catalog2:
        catalog1[key] = catalog2[key]
    return catalog1

catalog1 = {"apple": 1.0, "banana": 0.5}
catalog2 = {"banana": 0.75, "cherry": 1.25}
print(merge_catalogs(catalog1, catalog2))