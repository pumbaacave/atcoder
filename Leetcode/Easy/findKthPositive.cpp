#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution
{

public:
    int findKthPositive(vector<int> &arr, int k)
    {
        int cur = 1;
        int idx = 0;
        while (0 < k && idx < arr.size())
        {
            if (arr[idx] == cur)
            {
                idx++;
                cur++;
            }
            else
            {
                cur++;
                k--;
            }
        }
        return cur + k;
    }
};

int main()
{
    Solution solution;
    vector<int> temp{4, 5, 6, 7, 0, 2, 1, 3};
    cout << solution.restoreString("codeleet", temp);
    return 0;
}