#include <iostream>

// Show a working function
int abs(int x) { return x * ((x > 0) - (x < 0)); }

int main() {
  // print hello world
  std::cout << "Hello World!\n";

  // Determine which of two numbers is greater
  int num1, num2;
  num1 = 10, num2 = 99;

  if (num1 == num2)
    std::cout << "They both are equal.\n";
  else if (num1 > num2)
    std::cout << num1 << " is greater than " << num2 << "\n";
  else
    std::cout << num2 << " is greater than " << num1 << "\n";

  int v = -16;
  std::cout << abs(v);

  return 0;
}