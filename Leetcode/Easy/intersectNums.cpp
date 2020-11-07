#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>

using namespace std;

class Solution
{

public:
    vector<int> intersect(vector<int> &nums1, vector<int> &nums2)
    {
        vector<int> res;
        unordered_map<int, int> for_1, for_2;
        for (auto &num : nums1)
        {
            for_1[num]++;
        }
        for (auto &num : nums2)
        {
            for_2[num]++;
        }
        for (auto &[k, v] : for_1)
        {
            int cnt = min(v, for_2[k]);
            while (cnt > 0)
            {
                cnt--;
                res.push_back(k);
            }
        }
        return res;
    }
};

int main()
{
    Solution solution;
    vector<int> temp{3, 5, 1, 2, 4};
    cout << solution.findLatestStep(temp, 1);
    return 0;
}