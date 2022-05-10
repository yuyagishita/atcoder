#include <iostream>
using namespace std;

int main() {
  int a, b, c, d, e, f, x;
  cin >> a >> b >> c >> d >> e >> f >> x;

  int taka_x = x;
  int aoki_x = x;
  int taka_ans = 0;
  int aoki_ans = 0;
  bool hantei = true;

  while (true) {
    if (taka_x == 0)
      break;

    if (taka_x < a) {
      a = taka_x;
    }
    if (taka_x < c) {
      c = taka_x;
    }
    if (hantei) {
      taka_ans += a;
      taka_x = taka_x - a;
      hantei = false;
    } else {
      taka_x = taka_x - c;
      hantei = true;
    }
  }

  hantei = true;
  while (true) {
    if (aoki_x == 0)
      break;

    if (aoki_x < d) {
      d = aoki_x;
    }
    if (aoki_x < f) {
      f = aoki_x;
    }
    if (hantei) {
      aoki_ans += d;
      aoki_x = aoki_x - d;
      hantei = false;
    } else {
      aoki_x = aoki_x - f;
      hantei = true;
    }
  }

  if (taka_ans * b > aoki_ans * e) {
    cout << "Takahashi" << endl;
  } else if (taka_ans * b < aoki_ans * e) {
    cout << "Aoki" << endl;
  } else {
    cout << "Draw" << endl;
  }
}
