#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; ++i)
typedef long long int_t;

const int size = 200000;
int_t n;
int_t a[size];
int_t b[size];

bool input() {
  if (cin >> n) {
    rep (i, n) cin >> a[i];
    rep (i, n) cin >> b[i];
    return true;
  }
  return false;
}

const int psize = 50;
int_t p[psize];
int_t t[psize][size];

int count(int k, int_t ai) {
  int res = 0;
  auto tk = t[k];
  int c1 = lower_bound(tk, tk+n, p[k] - ai) - lower_bound(tk, tk+n, p[k-1] - ai);
  int c2 = lower_bound(tk, tk+n, p[k+1] - ai) - lower_bound(tk, tk+n, p[k] + p[k-1] - ai);
  return c1 + c2;
}

void solve() {
  p[0] = 1;
  rep (k, psize-1) {
    p[k+1] = p[k] * 2LL;
  }

  int_t mask = 1;
  rep (k, psize) if (k > 0) {
    rep (i, n) t[k][i] = b[i] & mask;
    sort(t[k], t[k]+n);
    mask = (mask << 1LL) | 1LL;
  }

  int cnt[psize];
  fill(cnt, cnt+psize, 0);
  int_t mask2 = 1;
  rep (k, psize-1) if (k > 0) {
    rep (i, n) {
      cnt[k] += count(k, a[i] & mask2);
    }
    mask2 = (mask2 << 1LL) | 1LL;
  }

  int_t res = 0;
  rep (k, psize) if (k > 0) {
    if (cnt[k] % 2) {
      res += 1LL << (k-1);
    }
  }
  cout << res << endl;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  while (input()) {
    solve();
  }
  return 0;
}
