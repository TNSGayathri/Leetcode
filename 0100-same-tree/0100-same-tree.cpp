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
    vector<int> fun(TreeNode* root,vector<int>&v){
        if(root==NULL)
        {v.push_back('null');
            return v;}
        v.push_back(root->val);
        fun(root->left,v);
        fun(root->right,v);
        return v;
    }
    bool isSameTree(TreeNode* p, TreeNode* q) {
        vector<int> v;
        fun(p,v);
        vector<int> m;
        fun(q,m);
        for(int i=0;i<v.size();i++){
            if(v[i]!=m[i])return false;
        }
        return true;
    }
};