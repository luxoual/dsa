class Solution {
  /**
   * @param {number[]} nums
   * @return {boolean}
   */
  hasDuplicate(nums) {
    const dupes = new Set();
    return nums.some(num => {
      if (dupes.has(num)) return true;
      dupes.add(num);
    })
  }
}

class Solution {
  /**
   * @param {number[]} nums
   * @return {boolean}
   */
  hasDuplicate(nums) {
    const dupes = new Set();
    for (const num of nums) {
      if (dupes.has(num)) return true;
      dupes.add(num);
    }
    return false;
  }
}

