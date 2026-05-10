#include <iostream>
using namespace std;

int main(){
    char capital_letter[26];
    int small_letter_ascii[26];
    int index = 0;

    for (int i = 97; i <= 122; i++){
        small_letter_ascii[index++] = i;
    }

    for (int i = 0; i < 26; i++){
        capital_letter[i] = char(small_letter_ascii[i] - 32);
    }

    for (int i = 0; i < 26; i++){
       cout << capital_letter[i] << " ";
    }
}