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
    void sum(TreeNode *root, int &su){
        if(root==NULL)return ;
            sum(root->right,su);
            su+=root->val;
            root->val=su;
        
        
            sum(root->left,su);
        
    }
    TreeNode* bstToGst(TreeNode* root) {
        if(root==NULL)return root;
        int su=0;
        sum(root,su);
        return root;
    }
};