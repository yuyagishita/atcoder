#include <iostream>
using namespace std;

int main() {
  int a, b, c, d, e, f, x;
  cin >> a >> b >> c >> d >> e >> f >> x;

  int p = x / (a + c), r = x % (a + c);
  int s = p * a;
  if (r <= a) {
    s += r;
  } else {
    s += a;
  }
  int T = s * b;

  p = x / (d + f), r = x % (d + f);
  s = p * d;
  if (r <= d) {
    s += r;
  } else {
    s += d;
  }
  int A = s * e;

  if (T > A) {
    cout << "Takahashi" << endl;
  } else if (T < A) {
    cout << "Aoki" << endl;
  } else {
    cout << "Draw" << endl;
  }
}
