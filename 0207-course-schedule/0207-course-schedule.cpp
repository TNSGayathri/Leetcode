class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int>adj[numCourses];
        vector<int>indegree(numCourses,0);
        for (auto it:prerequisites){
            adj[it[1]].push_back(it[0]);
            indegree[it[0]]++;
        }
        
       queue<int>q;
       for (int i=0;i<numCourses;i++){
           // cout<<indegree[i]<<i<<" ";
           if(indegree[i]==0){
               q.push(i);
           }
       } 
    vector<int>topo;
    while (!q.empty()){
        int node=q.front();
        q.pop();
        topo.push_back(node);
        for (auto it:adj[node]){
            indegree[it]-=1;
            if(indegree[it]==0){
                q.push(it);
            }
        }
}
        return (topo.size()==numCourses);
        
    }
};