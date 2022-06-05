def compare(s1,s2):
    if(s1+s2>s2+s1):
        return 1
    else:
        return 0


def solve(a):
    l=0
    h=len(a)-1
    x=list(map(str,a))
    ms(l,h,x)
    print(x)

def ms(low,high,arr):
    if low==high:
        return
    mid=(low+high)//2
    ms(low,mid,arr)
    ms(mid+1,high,arr)
    merge(low,mid,high,arr)

def merge(low,mid,high,arr):
    p1=low
    p2=mid+1
    tmp=[]
    while(p1<=mid and p2<=high):
        if(compare(arr[p1],arr[p2])):
            tmp.append(arr[p1])
            p1=p1+1
        else:
            tmp.append(arr[p2])
            p2=p2+1
    while p1<=mid:
        tmp.append(arr[p1])
        p1=p1+1
    while p2<=high:
        tmp.append(arr[p2])
        p2=p2+1
    for i in range(low,high+1):
        arr[i]=tmp[i-low]


#main
a=[4,6,2,8,7,9,1,3,90]
solve(a)
#print(a)
