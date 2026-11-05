import random

def merge(a,b):
    i= j =0
    out =[]
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    out.extend(a[i:])
    out.extend(b[j:])
    return out        

def merge_sort(a):
    if len(a) <=1: return a
    m = len(a)//2
    return merge(merge_sort(a[:m]), merge_sort(a[m:]))

productos = [("prod_%03d" % i, random.uniform(0,100)) for i in range(1,101)]
transform = [(pid,-score)for (pid,score) in productos]
ordenados = merge_sort(transform)
top5 = [(pid,-neg) for (pid,neg) in ordenados[:5]]
print("Top 5 productos con mejor puntuación:", top5)