#include <iostream>
#include <queue>

using namespace std;

int main(){
    int n;
    queue<int> q;
    int a;
    cin >> n;

    for (int i=1;i<=n;i++){
        q.push(i);
    }

    
    while (q.size() > 1){
        q.pop();
        a = q.front();
        q.pop();
        q.push(a);
    }
    a = q.front();
    cout << a;
}