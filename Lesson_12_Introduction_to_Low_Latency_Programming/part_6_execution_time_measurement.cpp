#include <iostream>
#include <chrono>

void sampleFunction() {
    for (int i = 0; i < 1e6; ++i);
}

int main() {
    auto start = std::chrono::high_resolution_clock::now();
    sampleFunction();
    auto end = std::chrono::high_resolution_clock::now();
    std::cout << "Execution Time: "
              << std::chrono::duration_cast<std::chrono::nanoseconds>(end - start).count()
              << " ns" << std::endl;
    return 0;
}
