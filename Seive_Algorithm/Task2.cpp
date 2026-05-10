#include <iostream>
#include <set>
using namespace std;

int main(){
    int n;
    cout << "Enter number: ";
    cin >> n;

    set<int> p;

    for (int i = 2; i <= n; i++){
        p.insert(i);
    }

    for (auto it = p.begin(); it != p.end(); it++){
        int prime = *it;

        for (int multiple = prime * 2; multiple <= n; multiple += prime){
            p.erase(multiple);
        }
    }

    // create another array only_prime
    int size = p.size();
    int only_prime[size];
    int index = 0;

    for(int x : p){
        only_prime[index++] = x;
    }
    
    cout << "List of prime number: ";
    for (int i = 0; i < size; i++){
        cout << only_prime[i] << " ";
    }
}
