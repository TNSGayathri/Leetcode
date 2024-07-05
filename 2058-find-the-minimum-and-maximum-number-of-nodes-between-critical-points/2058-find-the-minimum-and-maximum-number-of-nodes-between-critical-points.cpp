/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        int mi=INT_MAX;
       int ma=INT_MIN;
        int first=0;
        int last=0;
        int i=1;
        ListNode *t=head->next;
        ListNode *prev=head;
        while(t->next!=NULL){
            if(prev->val>t->val && t->val<t->next->val ||prev->val<t->val && t->val>t->next->val){
               
                            if (first == 0) {
                first= i;
            } else {
                mi = min(mi, i - last);
            }
            
            ma = max(ma, i- first);
            last = i;

            }
        prev=t;
        t=t->next;
        i=i+1;
    }
        if (first == last) {
        return {-1, -1};
    }

    
    return {mi,ma};
    }
};