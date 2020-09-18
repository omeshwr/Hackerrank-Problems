n,m = map(int,input().split())
a=[0]*(n+1)
m_sum=temp=0
for _ in range(m):
    first,last,val=map(int,input().split())
    a[first-1]+=val
    if last<=n:
        a[last]-=val
for i in a:
    temp+=i
    if m_sum<temp:
        m_sum=temp
print(m_sum)
