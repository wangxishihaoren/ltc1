arr = [2,7,11,15]
target = 9
def fun(numbers,target):
    out=[]
    for i in range(0,len(numbers)):
        for  j in range(i+1,len(numbers)):
            if(arr[i] + arr[j] == target):
                out.append(i+1)
                out.append(j+1)
        else:
            break
    print(out)
fun(arr,target)

