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
    void small(TreeNode* root,string s,vector<string> &v)
    {
        if(root==NULL)return;
        if(root->left==NULL and root->right==NULL)
        {
            // cout<<s<<" ";
            reverse(s.begin(), s.end()); 
            // cout<<s<<" "; 
            v.push_back(s);
            return;
        }
        if(root->left){
            char c=root->left->val+97;
            small(root->left,s+c,v);
            // s.pop_back();
        }
        if(root->right){
            char c=root->right->val+97;
            small(root->right,s+c,v);
            // s.pop_back();
        }
        return;
    }
    string smallestFromLeaf(TreeNode* root) {
        char c=(root->val+97);
        string s="";
        s=s+c;
        vector<string>v;
        small(root,s,v);
        sort(v.begin(),v.end());
        return v[0];
        
    }
};