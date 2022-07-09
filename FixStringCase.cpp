#include <string>

std::string solve(const std::string& str){
  int capital = 0, lower = 0;
  
  std::string s = str;
  for (auto x : str) {
    if (x >= 'A' && x <= 'Z') {
      capital++;
    }
    else {
      lower++;
    }
  }
  if (capital > lower) {
    std::transform(s.begin(), s.end(), s.begin(), ::toupper);
  }
  else {
    std::transform(s.begin(), s.end(), s.begin(), ::tolower);
  }
  return s;
}