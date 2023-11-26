import heapq
for _ in range(int(input())):
    n=int(input())
    st=input()
    hq=[]
    for c in st:
        heapq.heappush(hq,-ord(c))
    while(hq):
        val=heapq.heappop(hq)
        print(chr(-val))
    