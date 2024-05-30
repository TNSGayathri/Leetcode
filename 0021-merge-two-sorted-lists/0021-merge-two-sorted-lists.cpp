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
ListNode* head=NULL;
void insert_back(int value)
{
ListNode* new_node;
new_node=new ListNode;
new_node->val=value;
if(head==nullptr)
{
head=new_node;
new_node->next=nullptr;
}
else {
ListNode* temp = head;
while (temp->next != nullptr) {
temp = temp->next;
}
temp->next = new_node;
new_node->next=nullptr;
}
}

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
            head=NULL;
    while(list1!=NULL&&list2!=NULL)
    {
        int n1=list1->val,n2=list2->val;
        if(n1<=n2)
        {
            insert_back(list1->val);
            list1=list1->next;
        }
        else
        {
            insert_back(list2->val);
            list2=list2->next;
        }
       
    }
        if(list2!=NULL)
        {
            while(list2!=NULL)
            {
                insert_back(list2->val);
                list2=list2->next;
            }
        }
        else if(list1!=NULL)
        {
            while(list1!=NULL)
            {
                insert_back(list1->val);
                list1=list1->next;
            }
        }
     return head;
}

        
    
};