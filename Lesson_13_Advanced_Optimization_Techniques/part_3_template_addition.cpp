#include <iostream>

template <typename T>
T add(T a, T b) {
    return a + b;
}

int main() {
    std::cout << "Add Integers: " << add(5, 7) << std::endl;
    std::cout << "Add Doubles: " << add(5.5, 7.3) << std::endl;
    return 0;
}
