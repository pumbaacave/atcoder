#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution
{

public:
    int minCost(string s, vector<int> &cost)
    {
        int total = 0, c = 0, range_sum = 0;
        char last = '#';
        for (int i = 0; i < s.size(); i++)
        {
            if (s[i] != last)
            {
                last = s[i];
                total += range_sum - c;
                c = cost[i];
                range_sum = c;
            }
            else
            {
                c = max(c, cost[i]);
                range_sum += cost[i];
            }
        }
        // for last streak
        total += range_sum - c;
        return total;
    }
};

int main()
{
    Solution solution;
    vector<int> temp{4, 5, 6, 7, 0, 2, 1, 3};
    cout << solution.restoreString("codeleet", temp);
    return 0;
}