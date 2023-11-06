#include <iostream>

using namespace std;

int main()
{
  int N;
  int sum = 0;
  string number;

  cin >> N;
  cin >> number;
  
  for (int i = 0; i < N; i++)
  {
    sum += number[i] - '0';
  }
  cout << sum << '\n';
  return 0;
}