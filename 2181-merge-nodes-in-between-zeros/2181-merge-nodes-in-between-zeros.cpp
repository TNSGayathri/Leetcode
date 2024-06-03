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
    ListNode* mergeNodes(ListNode* head) {
        ListNode *t=head->next;
        int s=0;
        vector<int> v;
        while(t){
            if(t->val==0){
                v.push_back(s);
                s=0;
            }
            else s=s+t->val;
            t=t->next;
        }
        ListNode *t1=new ListNode(v[0]);
        ListNode *k=t1;
        int i=1;
        while(i<v.size()){
            ListNode *m=new ListNode(v[i]);
            t1->next=m;
            t1=t1->next;
            i+=1;
        }
        return k;
    }
    
};