from collections import defaultdict
def reduce(lst):
	res = defaultdict(list)
	for k,v in lst: res[k].append(v)
	return dict(res)
