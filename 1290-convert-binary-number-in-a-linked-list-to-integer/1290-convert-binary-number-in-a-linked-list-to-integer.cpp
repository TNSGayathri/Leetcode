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
    int getDecimalValue(ListNode* head) {
        ListNode *t=head;
        double c=0;
        while(t){
            c+=1;
            t=t->next;
        }
        int s=0;
        int p=int(pow(2.0,c-1));
        while(head){
            if(head->val==1){
            s+=p;}
            p=p/2;
            head=head->next;
        }
        return s;
    }
};