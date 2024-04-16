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
    void add(TreeNode* root,int l,int val,int depth)
    {
        if(root==NULL)
        {
            return;
        }
        if(l==depth-1)
        {
            TreeNode *t=new TreeNode(val);
            TreeNode *tmp=root->left;
            root->left=t;
            t->left=tmp;
            TreeNode *t1=new TreeNode(val);
            TreeNode *tmp1=root->right;
            root->right=t1;
            t1->right=tmp1;
            return;
        }
        add(root->left,l+1,val,depth);
        add(root->right,l+1,val,depth);
    }
    TreeNode* addOneRow(TreeNode* root, int val, int depth) {
        if(depth==1){
            TreeNode* t=new TreeNode(val);
            t->left=root;
            return t;
        }
        else{
            int l=1;
            add(root,l,val,depth);
        }
        return root;
        
    }
};