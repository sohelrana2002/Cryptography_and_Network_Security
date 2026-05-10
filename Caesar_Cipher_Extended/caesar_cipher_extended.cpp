#include <bits/stdc++.h>
#include <cctype>
using namespace std;

string encrypt(const string &text, int key){
    string result = "";

    for (char ch : text){
        if (isalpha(ch)){
            bool is_upper = isupper(ch);
            char base = is_upper ? 'A' : 'a';

            // Caesar Cipher logic
            char keyed_char = (ch - base + key + 26) % 26 + base;
            result += keyed_char;
        }
        else{
            result += ch; // input non-letter
        }
    }

    return result;
}

string decrypt(const string &cipherText, int key){
    return encrypt(cipherText, -key); // reverse method
}

int main(){
    string plainText;
    cout << "Write a message: ";
    getline(cin, plainText);

    int key_value;
    cout << "Enter a secret key: ";
    cin >> key_value;

    string encrypted_text = encrypt(plainText, key_value);
    string decrypted_text = decrypt(encrypted_text, key_value);

    cout << "Original Text: " << plainText << endl;
    cout << "Encrypted Text: " << encrypted_text << endl;
    cout << "Decrypted Text: " << decrypted_text << endl;

    return 0;
}