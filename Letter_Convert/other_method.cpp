#include <iostream>
using namespace std;

int main(){
    int index = 0;
    int size;
    cout << "Enter the size of char: ";
    cin >> size;
    char capital_letter[size];
    char small_letter_ascii[size];
    
    for (int i = 0; i < size; i++){
        cout << "Enter " << (i + 1) << " char: ";
        cin >> small_letter_ascii[i];
    }

    for (int i = 0; i < size; i++){
        capital_letter[i] = char(small_letter_ascii[i] - 32);
    }

    for (int i = 0; i < size; i++){
       cout << capital_letter[i] << ", ";
    }
}