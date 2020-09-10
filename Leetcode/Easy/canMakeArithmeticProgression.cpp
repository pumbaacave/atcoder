#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution
{

public:
    bool canMakeArithmeticProgression(vector<int> &arr)
    {
        if (arr.size() < 2)
        {
            return true;
        }
        sort(arr.begin(), arr.end());
        int delta = arr[1] - arr[0];
        int start = arr[0] - delta;
        for (int &num : arr)
        {
            start += delta;
            if (num != start)
            {
                return false;
            }
        }
        return true;
    }
};

int main()
{
    Solution solution;
    vector<int> temp{4, 5, 6, 7, 0, 2, 1, 3};
    cout << solution.restoreString("codeleet", temp);
    return 0;
}