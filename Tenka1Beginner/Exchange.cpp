#include <bits/stdc++.h>
using namespace std;

void operation(vector<int>& regs){
    regs[2]--;
    int temp;
    if(regs[0]%2 == 1)
        --regs[0];
    // swap included
    temp =regs[0]/2;
    regs[0]= regs[1] + temp;
    regs[1]= temp;

}

int main(){
    int A, B, K;
    cin >> A >> B >> K;
    vector<int> regs = {A, B, K};
    
    while(regs[2] >0){
        operation(regs);
    }
    if(K%2==0)
    cout << regs[0] << ' ' <<  regs[1] << endl;
    else
    cout << regs[1] << ' ' << regs[0] << endl;
}