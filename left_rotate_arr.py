
def array_left_rotation(a,k):
    alist = list(a)
    print(alist[k:])
    print(alist[:k])
    b = alist[k:] + alist[:k]
    return b


arr = [1, 2, 3, 4]
K= 1
ar=array_left_rotation(arr,K)
    
print("Array after left rotation: ")
for i in range(0, len(ar)):
    print(ar[i])