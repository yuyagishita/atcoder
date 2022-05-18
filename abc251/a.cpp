#include <iostream>
using namespace std;

int main() {
  string s;
  cin >> s;

  string ans = s;

  while (1) {
    if (ans.length() >= 6) {
      break;
    }
    ans += s;
  }

  cout << ans <<endl;
}
