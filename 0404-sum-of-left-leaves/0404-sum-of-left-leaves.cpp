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
    void sumofleft(TreeNode* root,int &s){
        if(root==NULL)return;
        if(root->left){
            if(root->left->left==NULL and root->left->right==NULL)s+=root->left->val;
            sumofleft(root->left,s);
        }
        if(root->right)
        {
            sumofleft(root->right,s);
        }
        return;
    }
    int sumOfLeftLeaves(TreeNode* root) {
        int s=0;
        if(root->left==NULL and root->right==NULL)return 0;
        sumofleft(root,s);
        return s;
    }
};