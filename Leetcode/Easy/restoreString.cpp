#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution
{

public:
    string restoreString(string s, vector<int> &indices)
    {
        string res{s};
        for (int i = 0; i < indices.size(); i++)
        {
            res[indices[i]] = s[i];
        }
        return res;
    }
};

int main()
{
    Solution solution;
    vector<int> temp{4, 5, 6, 7, 0, 2, 1, 3};
    cout << solution.restoreString("codeleet", temp);
    return 0;
}