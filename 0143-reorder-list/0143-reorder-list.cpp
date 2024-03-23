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
    void reorderList(ListNode* head) {
        ListNode *t=head;
        ListNode *t1=head;
        vector<int>v;
        vector<int>a;
        while (t){
            v.push_back(t->val);
            t=t->next;
        }
        int c=0;
        int i=0;
        int j=v.size()-1;
        int k=j;
        while(i!=j){
            if(c==0){
                c=1;
                a.push_back(v[i]);
                i+=1;
            }
            else{
                c=0;
                a.push_back(v[j]);
                j-=1;
            }
        }
        a.push_back(v[j]);
        i=0;
        while(t1)
        {
            t1->val=a[i];
            i+=1;
            t1=t1->next;
        }
    }
};