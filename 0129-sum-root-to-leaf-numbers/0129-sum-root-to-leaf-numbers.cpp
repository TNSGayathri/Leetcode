/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void sumleaf(TreeNode* root,string &s,int &c)
    {
        if(root==NULL)return;
        if(root->left==NULL and root->right==NULL)
        {
            // cout<<s<<" ";
            c+=stoi(s);
            return;
        }
        if(root->left){
            sumleaf(root->left,s.append(to_string(root->left->val)),c);
            s.pop_back();
        }
        if(root->right)
        {sumleaf(root->right,s.append(to_string(root->right->val)),c);
        s.pop_back();}
    }
    int sumNumbers(TreeNode* root) {
        string s=to_string(root->val);
        int c;
        sumleaf(root,s,c);
        return c;
        
    }
};