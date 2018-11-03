// Othello

#include <bits/stdc++.h>
using namespace std;

int main(){
    const int CAP = 200000;
    int N, Q;
    cin >> N >> Q;

    bitset<CAP> row{0};
    for (int i = 0; i<Q; i++){
        int l, r;
        cin >> l >> r;
        bitset<CAP> mask{pow(2, N - (l-1))-1 - (pow(2, N-r)-1)};
        mask <<= (CAP - N);
        row ^= mask;
    }
    cout << row.to_string().substr(0,N) << endl;
}