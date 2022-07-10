arr=[0,1,2,3]

output=[]

def permutation(st, arr, res):
    if st >= len(arr):
        res.append(arr[:])
        return

    for jj in range(st, len(arr)):
        arr[st], arr[jj] = arr[jj], arr[st]
        permutation(st+1, arr[:], res)
        arr[st], arr[jj] = arr[jj], arr[st]

    return


permutation(0, arr, output)

print(output)
print(len(output))
