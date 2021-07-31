/*
#include<cstdio> 
#include<algorithm> 
using namespace std; 
int n,ck[1000],r; 
pair<int,int> p[1000];

int main() { 
    scanf("%d", &n); 
    for (int i = 0; i < n; i++) 
    scanf("%d", &p[i].first), p[i].second = i;
    // for(int i = 0 ; i < n; i++){
    //     printf("%d %d\n", p[i].first,p[i].second);
    // }
    sort(p, p + n);
    // for(int i = 0 ; i < n; i++){
    //     printf("%d %d\n", p[i].first,p[i].second);
    // }

    for (int i = 0; i < n; i++) { 
        if (ck[i]) 
            continue; 
        int c=0; 
        for (int j = i; !ck[j]; j = p[j].second) { 
            ck[j] = 1;
            printf("BEFORE : %d\n",r);
            r += p[j].first; 
            printf("AFTER : %d\n",r);
            c++; 
        }
        printf("END\n");
        //printf("BEFORE : %d\n",r);
        r += min(p[0].first*(c + 1) + p[i].first, p[i].first*(c-2));
        //printf("AFTER : %d\n",r);
    } 
    printf("%d", r); 
    return 0;
}
*/
#include <iostream> 
#include <vector> 
#include <algorithm> 
#include <limits> 
using namespace std; 
typedef pair<int,int> bag; 
int N; bag a[100001]; 
int visited[100001]; 
int total_min = numeric_limits<int>::max(); 
void find_cycle(int st, int &mmin, int &sum, int &cnt) { 
    mmin=10001, sum=0, cnt=0; 
    int here=st; 
    while (true) { 
        visited[here] = 1; 
        cnt++; 
        sum+=a[here].first; 
        mmin=min(mmin, a[here].first); 
        here=a[here].second; 
        if(here == st)
            break; 
    } 
 } 
int main() { 
    scanf("%d", &N); 
    for(int i = 0; i < N; i++) { 
        scanf("%d", &a[i].first); 
        a[i].second = i; 
        total_min=min(total_min, a[i].first); 
    }
    sort(a, a + N);
    int ret = 0; 
    for (int i = 0; i < N; i++) { 
        if (a[i].second != i && visited[i] == 0) {
            int mmin, sum, cnt; 
            find_cycle(i, mmin, sum, cnt); 
            ret += min((sum-mmin) + (cnt-1)*mmin, mmin+sum+(cnt+1)*total_min); 
            } 
        } 
    printf("%d\n", ret); 
}