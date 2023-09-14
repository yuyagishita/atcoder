#include <iostream>
using namespace std;

int main() {
  string w;
  cin >> w;
  char arr[] = {'a', 'i', 'u', 'e', 'o'};
  string ans;

  int tmp;

  for (int i = 0; i < w.length(); i++) {
    tmp = 0;
    for (int j = 0; j < 5; j++) {
      if (arr[j] == w[i]) {
        tmp++;
      }
    }
    if (tmp <= 0) {
      ans += w[i];
    }
  } 

  cout << ans << endl;
}
