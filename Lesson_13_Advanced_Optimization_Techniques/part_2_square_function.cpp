#include <iostream>

inline int square(int x) {
    return x * x;
}

int main() {
    int num = 10;
    std::cout << "Square of " << num << " is " << square(num) << std::endl;
    return 0;
}
