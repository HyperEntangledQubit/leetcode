#include <iostream>
#include <cstdlib>
#include <map>
#include <vector>

std::vector<int> two_sum_dbl_loop(std::vector<int>& nums, int target) {
    std::vector<int> twosum; // Set vector size to only two here

    for(unsigned int i=0; i < nums.size(); i++) {
        if (twosum.size() == 2) {
            break;
        }
        int diff = target - nums[i];
        for(unsigned int j=0; j < nums.size(); j++) {
            if ((i != j) && (nums[i] + nums[j] == target)) {
                twosum.push_back(i);
                twosum.push_back(j);
            }

        }
    }
    return twosum;
}

void two_sum_hash(std::vector<int>& nums, int target) {
        std::map<int, int> seen_vals;
}


int main(int argc, char* argv[]) {
    std::vector<int> search_arr;
    search_arr =  {2, 7, 3, 99, 107, 64, -60};
    int target = -57;
    std::vector<int> result = two_sum_dbl_loop(search_arr, target);

    for(int i: result) {
        std::cout<<i<<std::endl;
    }
    return EXIT_SUCCESS;
}
