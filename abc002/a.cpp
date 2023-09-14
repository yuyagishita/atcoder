#include <iostream>
using namespace std;

int main() {
  int x, y;
  cin >> x >> y;

  int ans;
  if (x > y) {
    ans = x;
  } else {
    ans = y;
  }

  cout << ans << endl;
}
