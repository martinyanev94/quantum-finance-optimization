#include <unistd.h>
#include <vector>

void batchWriteToDisk(const std::vector<std::string>& data) {
    std::string buffer;
    for (const auto& datum : data) {
        buffer += datum + "\n";
    }
    write(STDOUT_FILENO, buffer.c_str(), buffer.size());
}

int main() {
    std::vector<std::string> data = {"Trade1", "Trade2", "Trade3"};
    batchWriteToDisk(data);  // Batch operations to reduce calls
    return 0;
}
