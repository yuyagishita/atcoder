#include <cctype>
#include <iostream>
#include <set>
#include <string>
using namespace std;

int main() {
  string S;
  cin >> S;

  int s_len = S.length();
  bool omoji = false;
  bool komoji = false;
  set<char> st;

  for (auto i : S) {
    if (isupper(i)) {
      omoji = true;
    }
    if (islower(i)) {
      komoji = true;
    }
    st.insert(i);
  }
  
  if (omoji && komoji && st.size() == S.size()) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }
}
