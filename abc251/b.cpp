#include <iostream>
#include <vector>
using namespace std;

int main() {
  int n, w;
  cin >> n >> w;
  vector<int> a(n);
  for (auto &x : a)
    cin >> x;

  vector<int> flag(w + 1);

  for (int i = 0; i < n; i++) {
    int s = a[i];
    if (s <= w) {
      flag[s] = 1;
    }
  }

  for (int i = 0; i < n; i++) {
    for (int j = i + 1; j < n; j++) {
      int s = a[i] + a[j];
      if (s <= w) {
        flag[s] = 1;
      }
    }
  }

  for (int i = 0; i < n; i++) {
    for (int j = i + 1; j < n; j++) {
      for (int k = j + 1; k < n; k++) {
        int s = a[i] + a[j] + a[k];
        if (s <= w) {
          flag[s] = 1;
        }
      }
    }
  }

  int ans = 0;
  for (int i = 1; i <= w; i++) {
    ans += flag[i];
  }
  cout << ans << endl;
}
