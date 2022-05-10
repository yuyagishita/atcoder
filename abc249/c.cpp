#include <iostream>
#include <string>
#include <map>
using namespace std;

int main() {
  int n, k;
  cin >> n >> k;
  vector<string> s(n);
  for (int i = 0; i < n; i++) cin >> s[i];

  int ans = 0;
  for (int i = 0; i < (1 << n); i++) {
    int now = 0;
    map<char, int> cnt;
    for (int j = 0; j < n; j++) {
      if ((i >> j) & 1) {
        for (char c : s[i]) cnt[c]++;
      }

    for (auto p : cnt) if (p.second == k) ++now;
    ans = max(ans, now);
    }
  cout << ans << endl;
  }
}
