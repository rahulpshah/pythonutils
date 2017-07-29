from collections import defaultdict


'''
lst: List of tuples of the form [(k, v1), (k, v2)]. The reduce changes to {k:[v1, v2]}
'''
def reduce(lst):
        res = defaultdict(list)
        for k,v in lst: res[k].append(v)
        return dict(res)

'''
Gets the freq_count of all the items in the list
'''
def freq_count(lst):
        dct = defaultdict(int)
        for item in lst:
                dct[item] += 1
        return dict(dct)
