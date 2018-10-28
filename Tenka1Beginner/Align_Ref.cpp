include <bits/stdc++.h>
using namespace std;
int main(){
    long n;
    cin>>n;
    vector<long> a(n);
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    sort(begin(a),end(a));
    long first=0,last=a.size()-2;
    long left=a[last+1],right=a[last+1];
    long sum=0;
    a.pop_back();
    while(first<=last){
        long t1=max(abs(left-a[first]),abs(right-a[first]));
        long t2=max(abs(left-a[last]),abs(right-a[last]));
        if(t1>t2){
            sum+=t1;
            if(abs(left-a[first])>abs(right-a[first]))
                left=a[first];
            else
                right=a[first];
            first++;
        }
        else{
            sum+=t2;
            if(abs(left-a[last])>abs(right-a[last]))
                left=a[last];
            else
                right=a[last];
            last--;
        }
    }
    cout<<sum;
}
