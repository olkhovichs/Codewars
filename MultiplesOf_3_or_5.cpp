#include <vector>
#include <cmath>

int solution(int number) {
  std::vector<int> numbers;
  int sum = 0;

  for (int i = 0; i < number; i++) {
    numbers.push_back(i);
  }
  for (auto x : numbers) {
    if ((!std::fmod(x, 3)) || (!std::fmod(x, 5))) {
      sum += x;
    }
  }
  return sum;
}