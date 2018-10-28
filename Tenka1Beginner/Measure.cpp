#include <bits/stdc++.h>
#include <string.h>
using namespace std;

int main() {
    string target;
    cin >> target;
    if (target.size() == 2)
    {
        cout << target << endl;
    }
    else if(target.size() == 3)
    {
        //string output(target.rbegin(), target.rend());
        //cout << target << endl;
        cout << target[2] << target[1] << target[0] << endl;
    }
  
}