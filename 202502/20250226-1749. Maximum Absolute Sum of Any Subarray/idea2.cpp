#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int maxAbsoluteSum(vector<int>& nums) {
        int maxabsSum = 0;
        int imin =  0; //minimum sum value for subarrays end with index i
        int imax = 0; //maximum sum value for subarrays end with index i
        for (int val : nums){
            imin = imin<0? imin+val:val;
            imax = imax>0? imax+val:val;
            maxabsSum = max({maxabsSum, abs(imin), abs(imax)});
        }
        return maxabsSum;
    }
};

int main(int argc, char const *argv[]){
    vector<int> nums = {1,-3,2,3,-2};
    Solution s;
    cout << s.maxAbsoluteSum(nums) << endl;
    return 0;
}