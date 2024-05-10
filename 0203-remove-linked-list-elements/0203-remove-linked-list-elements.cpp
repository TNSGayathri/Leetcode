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
    ListNode* removeElements(ListNode* head, int val) {
        
        while(head!=NULL and head->val==val  ){
            head=head->next;
        }
        if(head==NULL)return head;
        ListNode* t=head;
        ListNode*p=NULL;
        while (t->next!=NULL)
        {
            if(t->val==val){
                p->next=t->next;
                t=p->next;
            }
            else{
                p=t;
            t=t->next;}
            
        }
        if(t->val==val)p->next=NULL;
        return head;
    }
};