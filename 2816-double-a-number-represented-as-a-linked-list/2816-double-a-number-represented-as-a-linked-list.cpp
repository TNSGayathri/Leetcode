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
    ListNode *reverse(ListNode *head){
        ListNode *p=NULL;
        ListNode *n=NULL;
        ListNode *cur=head;
        while(cur){
            n=cur->next;
            cur->next=p;
            p=cur;
            cur=n;
        }
        head=p;
        return head;
    }
    ListNode* doubleIt(ListNode* head) {
        ListNode *head1= reverse(head);
        ListNode *t=head1;
        int d=0;
        ListNode *p=NULL;
        while (t){
            p=t;
            int c=t->val;
            c=c*2;
            t->val=(c%10)+d;
            d=c/10;
            t=t->next;
        }
        if(d>0){
            ListNode *temp=new ListNode(d);
            p->next=temp; 
        }
        
        return reverse(head1);
    }
};