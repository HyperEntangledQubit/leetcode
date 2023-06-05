#include <iostream>
#include <cstdlib>
#include <vector>

int main(int argc, char* argv[]) {
    std::vector<int> search_arr;
    search_arr =  {2, 7, 3, 99, 107, 64, -60};
    for(unsigned int i=0; i < search_arr.size(); i++) {
        std::cout << search_arr[i] << std::endl;
    }
    return EXIT_SUCCESS;
}
