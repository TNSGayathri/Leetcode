class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        if len(deck)<=2:
            deck.sort()
            return deck
        deck.sort()
        t=[0]*len(deck)
        l=[]
        for i in range(len(deck)):
            l.append(i)
        # print(l)
        i=0
        while len(l)>0:
            # print(1)
            t[l[0]]=deck[i]
            i+=1
            l.pop(0)
            if(len(l)>1):
                l.append(l[0])
                l.pop(0)
            # print(t,l)
        return t
            