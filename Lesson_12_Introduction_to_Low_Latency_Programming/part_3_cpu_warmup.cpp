void warmupRoutine() {
    for (int i = 0; i < 10000; ++i) {
        // Perform dummy calculations to warm up CPU
        volatile int temp = i * i; 
    }
}

int main() {
    warmupRoutine();  // Invoke before actual operations
    // Start trading algorithms here
    return 0;
}
