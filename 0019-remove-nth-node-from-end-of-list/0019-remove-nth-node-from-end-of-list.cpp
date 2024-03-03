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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *temp=head;
        int c=0;
        while (temp)
        {
            c+=1;
            temp=temp->next;
        }
        if(c==1 and n==1)
        {
            return NULL;
        }
        ListNode *t2=head;
        int c1=0;
        int k=(c-n);
        ListNode *prev=NULL;
        if(k==0)
        {
            return head->next;
        }
        while(t2)
        {
            if(c1==k){
                prev->next=t2->next;
                return head;
            }
            prev=t2;
            t2=t2->next;
            c1+=1;
        }
        return head;
    }
};