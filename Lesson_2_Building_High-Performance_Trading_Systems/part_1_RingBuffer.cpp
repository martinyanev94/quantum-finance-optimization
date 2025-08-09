#include <iostream>
#include <vector>
#include <mutex>

class RingBuffer {
private:
    std::vector<double> buffer;
    size_t head;
    size_t tail;
    size_t maxSize;
    std::mutex mtx;

public:
    RingBuffer(size_t size) : maxSize(size), head(0), tail(0) {
        buffer.resize(size);
    }

    void add(double value) {
        std::lock_guard<std::mutex> lock(mtx);
        buffer[head] = value;
        head = (head + 1) % maxSize;
        if (head == tail) {
            tail = (tail + 1) % maxSize; // Overwrite the oldest value
        }
    }

    double get() {
        std::lock_guard<std::mutex> lock(mtx);
        if (head == tail) {
            throw std::out_of_range("Buffer is empty");
        }
        double value = buffer[tail];
        tail = (tail + 1) % maxSize;
        return value;
    }

    bool isEmpty() {
        return head == tail;
    }
};
