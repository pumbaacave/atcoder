#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <limits.h>
#include <iomanip>
#include <algorithm>
#include <numeric>
#include <functional>
#include <unordered_map>
#include <map>
#include <unordered_set>
#include <array>
#include <queue>
#include <math.h>
#include <assert.h>

#define rep(i, n) for (int i = 0; i < (n); i++)

using namespace std;

#define ll long long
#define all(v) v.begin(),v.end()
#define bootstrap ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);
#define SZ(a) ((int)(a).size())
#define NG (-1)

void solve() {
    priority_queue<ll, vector<ll>, greater<ll> > pq;
    int q, p;
    ll x;
    ll sum = 0;
    cin >> q;
    rep(qq, q) {
        cin >> p;
        if (p == 1) {
            cin >> x;
            pq.push(x - sum);
        } else if (p == 2) {
            cin >> x;
            sum += x;
        } else if (p == 3) {
            x = pq.top();
            cout << x + sum << endl;
            pq.pop();
        }
    }
    return;
}

int main() {
    bootstrap
    solve();
}

