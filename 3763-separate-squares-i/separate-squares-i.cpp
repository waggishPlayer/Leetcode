class Solution {
public:
    double separateSquares(vector<vector<int>>& squares) {
        double totalArea = 0;
        double minY = 2e9, maxY = 0;
        for (const auto& sq : squares) {
            double y = sq[1];
            double l = sq[2];
            totalArea += (double)l * l;
            minY = min(minY, y);
            maxY = max(maxY, y + l);
        }

        double targetArea = totalArea / 2.0;
        double low = minY;
        double high = maxY;
        double ans = high;
        for (int i = 0; i < 60; i++) {
            double mid = low + (high - low) / 2;
            
            if (getAreaBelow(squares, mid) >= targetArea) {
                ans = mid;
                high = mid;
            } else {
                low = mid;
            }
        }

        return ans;
    }
    double getAreaBelow(vector<vector<int>>& squares, double lineY) {
        double currentArea = 0;
        for (const auto& sq : squares) {
            double y = sq[1];
            double l = sq[2];
            double top = y + l;
            if (y >= lineY) continue;
            if (top <= lineY) {
                currentArea += (double)l * l;
            } 
            else {
                double heightBelow = lineY - y;
                currentArea += heightBelow * l;
            }
        }
        return currentArea;
    }
};