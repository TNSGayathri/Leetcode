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
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode *t1=list1;
        ListNode *t2=NULL;
        int c=0;
        while (c!=a-1)
        {
            t1=t1->next;
            c+=1;
        }
        t2=t1->next->next;
        // cout<<c<<t1->val<<t2->val<<" ";
        t1->next=list2;
        c+=1;
        while (c!=b)
        {
            t2=t2->next;
            c+=1;
        }
        // cout<<c<<t1->val<<t2->val<<" ";
        while (list2->next!=NULL)
        {
            list2=list2->next;
        }
        list2->next=t2;
        return list1;
    }
};