class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        if(sorted(students)==sorted(sandwiches)):
            return 0
        oc=students.count(1)
        zc=students.count(0)
        l=len(sandwiches)
        for i in range(0,l):
            if sandwiches[i]==1:
                if oc==0:
                    return l-i
                else:
                    oc-=1
            elif sandwiches[i]==0:
                if zc==0:
                    return l-i
                else:
                    zc-=1
        return 0
                    
        
            
        