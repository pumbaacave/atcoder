// Drone

#include <bits/stdc++.h>
using namespace std;

int main(){
    string S;
    int T;
    cin >> S >> T;

    int x =0;
    int y =0;
    int count = 0;
    for (auto ch:S){
        if (ch == 'L'){
            x -= 1;
        }
        else if (ch == 'R'){
            x += 1;
        }
        else if (ch == 'U'){
            y += 1;
        }
        else if (ch == 'D'){
            y -= 1;
        }
        else if (ch == '?'){
            count++;
        }
    }

    int dis = abs(x) + abs(y);
    if( T == 1){
        cout << dis + count << endl;
    }
    else if (T == 2){
        if ((dis - count)>0){
            cout << dis - count << endl;
        }
        else{
        // redundant '?' will lead to 1 when it is odd
        cout << abs(dis - count) %2 << endl;
        }
    }
}