#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>

using namespace std;

class Solution
{

public:
    int findLatestStep(vector<int> &arr, int m)
    {
        unordered_map<int, pair<int, int>> lefts, rights;
        int step = -1, cnt = 1;
        int l, r;
        for (int &idx : arr)
        {
            cnt++;
            l = r = idx;
            if (rights.count(idx - 1))
            {
                auto &[a, b] = rights[idx - 1];
                l = a;
                rights.erase(idx - 1);
                lefts.erase(a);
            }
            if (lefts.count(idx + 1))
            {
                auto &[a, b] = lefts[idx + 1];
                r = b;
                lefts.erase(idx + 1);
                rights.erase(b);
            }
            if (r - l + 1 == m)
            {
                step = cnt;
            }
            lefts.emplace(l, pair<int, int>(l, r));
            rights.emplace(r, pair(l, r));
        }
        for (const auto &[k, v] : lefts)
        {
            cout << k << ":" << v.first << " " << v.second << endl;
        }
        cout << "==============\n";
        for (const auto &[k, v] : rights)
        {
            cout << k << ":" << v.first << " " << v.second << endl;
        }
        return step;
    }
};

int main()
{
    Solution solution;
    vector<int> temp{3, 5, 1, 2, 4};
    cout << solution.findLatestStep(temp, 2);
    return 0;
}