/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        unordered_set<ListNode*>hs;
        ListNode *temp=headA;
        while(temp){
            hs.insert(temp);
            temp=temp->next;
        }
        temp=headB;
        while(temp){
            if (hs.find(temp)!=hs.end()){
return temp;}
            temp=temp->next;
        }
        
        return NULL;
    }
};