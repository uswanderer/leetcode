// Given a collection of candidate numbers (candidates) and a target number (target), 
// find all unique combinations in candidates where the candidate numbers sum to target.
// Each number in candidates may only be used once in the combination.
// Note: The solution set must not contain duplicate combinations.

// Example 1:

// Input: candidates = [10,1,2,7,6,1,5], target = 8
// Output: 
// [
// [1,1,6],
// [1,2,5],
// [1,7],
// [2,6]
// ]

// Example 2:

// Input: candidates = [2,5,2,1,2], target = 5
// Output: 
// [
// [1,2,2],
// [5]
// ]

// --------------------------------------------

// Solution 1: Backtracking

import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        if (candidates == null || candidates.length == 0) {
            return new ArrayList<>();
        }

        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(candidates);
        backtrack(result, candidates, target, new ArrayList<>(), 0);

        return result;
    }

    public void backtrack(List<List<Integer>> res, int[] candidates, int target, List<Integer> temp, int start) {
        if (target == 0) {
            res.add(new ArrayList<>(temp));
            return;
        };

        if (target < 0) return;

        for (int i = start; i < candidates.length; i++) {
            if (i != start && candidates[i] == candidates[i -1]) continue;

            temp.add(candidates[i]);
            backtrack(res, candidates, target - candidates[i], temp, i + 1);
            temp.remove(temp.size() - 1);
        }
    }
}