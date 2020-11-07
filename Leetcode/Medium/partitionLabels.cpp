#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>
#include <execinfo.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

using namespace std;
void handler(int sig)
{
    void *array[10];
    size_t size;

    // get void*'s for all entries on the stack
    size = backtrace(array, 10);

    // print out all the frames to stderr
    fprintf(stderr, "Error: signal %d:\n", sig);
    backtrace_symbols_fd(array, size, STDERR_FILENO);
    exit(1);
}

class Solution
{

public:
    vector<int> partitionLabels(string S)
    {
        vector<int> res;
        unordered_map<char, int> start;
        vector<int> ends(26, 0);
        vector<char> seq;
        for (int i = 0; i < S.length(); i++)
        {
            char &ch = S[i];
            if (start.count(ch) == 0)
            {
                start[ch] = i;
                seq.push_back(ch);
            }
            ends[ch - 'a'] = i;
        }
        int l = 0;
        //int r = ends[seq[0] - 'a'];
        int r = 0;
        //cout << ends.size();
        for (char &ch : seq)
        {
            if (r < start[ch])
            {
                res.push_back(r - l + 1);
                l = start[ch];
            }
            //cout << ch << ": " << ch - 'a' << ' ' << endl;
            //r = max(r, ends.at(ch - 'a'));
            r = max(r, ends[ch - 'a']);
        }
        res.push_back(r - l + 1);
        return res;
    }
};

int main()
{
    signal(SIGSEGV, handler); // install our handler
    Solution solution;
    vector<int> temp{3, 5, 1, 2, 4};
    auto res = solution.partitionLabels("ababcbacadefegdehijhklij");
    for (auto &num : res)
    {
        cout << num << " ";
    }
    return 0;
}