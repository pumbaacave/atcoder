#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; ++i)

int doSum(vector<int>con, vector<int>rev, int N){
    int half,sum;
    if (N%2==0)
        half = N/2 -1;
    else
        half = (N+1)/2 -1;

    int sum =0;
    for(int i=0;i<half-1;i++){
        sum += abs(rev[i]-con[i+1]);
        sum += abs(con[i]-rev[i+1]);
    }
    sum+=(rev[0] - con[0]);
    if (N%2!=0){
        sum -= (rev[half-1]-con[half]);
    }
    return sum;
}

int main(){
    int N, half;
    cin  >> N;
    vector<int> con(N);
    rep(i,N) cin >> con[i];
    sort(con.begin(), con.end());
    vector<int> rev(con.rbegin(), con.rend());
    int sum1, sum2, sum;
    sum1 = doSum(con, rev, N);
    sum2 = doSum(rev, con, N);
    sum = sum1 > sum2 ? sum1:sum2;
    cout << sum << endl;
}