#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <random>
#include <iomanip>
#include <sstream>

int main() {
    std::mt19937 rng(std::random_device{}());
    std::uniform_int_distribution<int> dist(0, 255);

    std::string input;
    std::cin >> input;
    
    if (input.length() < 4) {
        std::cout << "Input is too short!" << std::endl;
        return 0;
    }

    std::vector<int> inputNumbers(input.begin(), input.end());

    int n = static_cast<int>(std::ceil(std::sqrt(inputNumbers.size())));
    int requiredSize = n * n;

    inputNumbers.resize(requiredSize, dist(rng));

    std::vector<std::vector<int>> originalMatrix(n, std::vector<int>(n, 0));

    int row = 0;
    int col = 0;
    int dir = 0; // Direction: 0 = right, 1 = down, 2 = left, 3 = up

    for (int i = 0; i < requiredSize; ++i) {
        originalMatrix[row][col] = inputNumbers[i];
        if (dir == 0 && (col + 1 == n || originalMatrix[row][col + 1] != 0)) dir = 1;
        else if (dir == 1 && (row + 1 == n || originalMatrix[row + 1][col] != 0)) dir = 2;
        else if (dir == 2 && (col == 0 || originalMatrix[row][col - 1] != 0)) dir = 3;
        else if (dir == 3 && (row == 0 || originalMatrix[row - 1][col] != 0)) dir = 0;

        switch (dir) {
            case 0: ++col; break;
            case 1: ++row; break;
            case 2: --col; break;
            case 3: --row; break;
        }
    }

    // Using a pair of integers to represent the positions.
    std::vector<std::vector<std::pair<int, int>>> s_box(n, std::vector<std::pair<int, int>>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            s_box[i][j] = {i, j};
        }
    }

    // Shuffle the s-box
    for (int i = 0; i < n * n; i++) {
        int randRow = dist(rng) % n;
        int randCol = dist(rng) % n;
        std::swap(s_box[i / n][i % n], s_box[randRow][randCol]);
    }

    std::vector<std::vector<int>> shuffledMatrix(n, std::vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            shuffledMatrix[i][j] = originalMatrix[s_box[i][j].first][s_box[i][j].second];
        }
    }

    for (auto& row : shuffledMatrix) {
        for (auto& element : row) {
            element *= 8;
        }
    }

    std::stringstream serial_number;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i != 0 || j != 0)
                serial_number << "-";
            serial_number << std::setfill('0') << std::setw(2) << std::hex << s_box[i][j].first
                          << std::setfill('0') << std::setw(2) << std::hex << s_box[i][j].second
                          << std::setfill('0') << std::setw(4) << std::hex << shuffledMatrix[i][j];
        }
    }

    std::cout << serial_number.str() << std::endl;

    return 0;
}