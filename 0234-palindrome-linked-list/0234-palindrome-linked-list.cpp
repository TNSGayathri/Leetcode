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
    bool isPalindrome(ListNode* head) {
        ListNode* f=head;
        ListNode* s=head;
        while(f!=NULL && f->next!=NULL)
        {
            s=s->next;
            f=f->next->next;
        }
        //p->next=NULL;
        ListNode* head1 = NULL;
        if(f==NULL)
        {
           head1=s;
        }
            
        else if(f->next==NULL)
        {  
            head1=s->next;
        }
        // while (head1)
        //  {
        //     cout<<head1->val<<" ";
        //     head1=head1->next;
        //  }

        
        ListNode *prev=NULL;
        ListNode *n=NULL;
        ListNode *cur=head1;
            while(cur){
                n=cur->next;
                cur->next=prev;
                prev=cur;
                cur=n;
            }
            head1=prev;
        while(head1!=NULL)
        {
            if(head->val!=head1->val)
            {
                return false;
            }
            head=head->next;
            head1=head1->next;
        }
        return true;
    }
};