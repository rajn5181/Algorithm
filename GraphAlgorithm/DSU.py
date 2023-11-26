class DSU:
    def __init__(self,n):
        self.Parent=list(range(n))
        self.Rank=[0]*n
    
    def FindParent(self,x):
        if(self.Parent[x]!=x):
            self.Parent[x]=self.FindParent(self.Parent[x])
        return self.Parent[x]


    def MakeUnion(self,x,y):
        p_x=self.FindParent(x)
        p_y=self.FindParent(y)
        if(p_x!=p_y):
            if(self.Rank[p_x]>self.Rank[p_y]):
                self.Parent[p_y]=p_x
            elif(self.Rank[p_y]>self.Rank[p_x]):
                self.Parent[p_x]=p_y
            else:
                self.Parent[p_x]=p_y
                self.Rank[p_y]+=1
       
    




        






        