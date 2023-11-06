#include <iostream>
using namespace std;

int main()
{
  int N;
  cin >> N;
  int scores[N];
  int max = 0;
  double sum = 0;

  for (int i = 0; i < N; i++)
  {
    cin >> scores[i];
    if (max < scores[i])
    {
      max = scores[i];
    }
  }

  for (int i = 0; i < N; i++)
  {
    sum += (double) scores[i] / max * 100.0;
  }
  cout << sum / N;
  return 0;
}