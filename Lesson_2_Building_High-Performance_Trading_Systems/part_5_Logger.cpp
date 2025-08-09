#include <fstream>
#include <iostream>

class Logger {
private:
    std::ofstream logFile;

public:
    Logger(const std::string& fileName) {
        logFile.open(fileName, std::ios_base::app);
        if (!logFile.is_open()) {
            std::cerr << "Error opening log file!" << std::endl;
        }
    }

    ~Logger() {
        if (logFile.is_open()) {
            logFile.close();
        }
    }

    void log(const std::string& message) {
        if (logFile.is_open()) {
            logFile << message << std::endl;
        }
    }
};
