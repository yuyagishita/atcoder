#include <bits/stdc++.h>
using namespace std;

int main() {
  int n, a, i, tmp;
  string ans;

  cin >> n >> a;

  i = 0;
  tmp = 0;
  while (true) {
    tmp = (n - (500 * i));
    if (tmp == 0) {
      break;
    }
    if (tmp <= 0) {
      tmp = (n - (500 * (i - 1)));
      break;
    }
    i++;
  }

  if (tmp == 0) {
    ans = "Yes";
  } else if (tmp > 0 && tmp - a <= 0) {
    ans = "Yes";
  } else {
    ans = "No";
  }

  cout << ans << endl;
}
