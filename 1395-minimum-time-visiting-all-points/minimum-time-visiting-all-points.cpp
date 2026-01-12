class Solution {
public:
    int minTimeToVisitAllPoints(vector<vector<int>>& points) {
        int time = 0;
        for (int i = 0; i < points.size() - 1; i++ ){
            int x1 = points[i][0];
            int y1 = points[i][1];
            int x2 = points[i+1][0];
            int y2 = points[i+1][1];

            int x = abs(x2 - x1);
            int y = abs(y2 - y1);

            time += max(x,y);
        }
        return time;
    }
};