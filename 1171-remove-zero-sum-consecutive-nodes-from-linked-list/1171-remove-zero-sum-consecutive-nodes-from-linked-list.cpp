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
    ListNode* removeZeroSumSublists(ListNode* head) {
        if(head->val==0)head=head->next;
        
        ListNode*t1=head;
        int c=0;
        int pre=0;
        while(t1)
        {
            pre=pre+t1->val;
            if(pre==0)head=t1->next;
            t1=t1->next;
            c+=1;
        }
        if(pre==0)
        {
            return NULL;
        }
        if(c==1 and head->val==0){
            return NULL;
        }
        if(c==2){
            if(head->val+head->next->val==0)
            {
                return NULL;
            }
        }
        
        ListNode *temp=head;
        while(temp!=NULL)
        {
            pre=0;
            ListNode* j=temp->next;
            while (j!=NULL)
            {
                pre+=j->val;
                if(pre==0 )
                {
                    temp->next=j->next;
                }
                j=j->next;
            }
            temp=temp->next;
        }
        return head;
        
    }
};