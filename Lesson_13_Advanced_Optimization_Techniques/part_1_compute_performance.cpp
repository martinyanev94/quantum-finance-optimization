#include <iostream>
#include <chrono>

void computeWithFloat() {
    float result = 0.0f;
    for (int i = 1; i < 1e7; ++i) {
        result += 1.0f / static_cast<float>(i);
    }
    std::cout << "Result with Float: " << result << std::endl;
}

void computeWithInt() {
    long long result = 0;
    for (int i = 1; i < 1e7; ++i) {
        result += 1 / i;
    }
    std::cout << "Result with Int: " << result << std::endl;
}

int main() {
    auto start = std::chrono::high_resolution_clock::now();
    computeWithFloat();
    auto end = std::chrono::high_resolution_clock::now();
    std::cout << "Time taken for Float: "
              << std::chrono::duration_cast<std::chrono::microseconds>(end - start).count()
              << " microseconds" << std::endl;

    start = std::chrono::high_resolution_clock::now();
    computeWithInt();
    end = std::chrono::high_resolution_clock::now();
    std::cout << "Time taken for Int: "
              << std::chrono::duration_cast<std::chrono::microseconds>(end - start).count()
              << " microseconds" << std::endl;

    return 0;
}
