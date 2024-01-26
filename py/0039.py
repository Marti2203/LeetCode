class Solution:
  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    ans = []
    from copy import deepcopy
    def dfs(s: int, target: int, path: List[int]) -> None:
      if target < 0:
        return
      if target == 0:
        ans.append(deepcopy(path))
        return

      for i in range(s, len(candidates)):
        path.append(candidates[i])
        dfs(i, target - candidates[i], path)
        path.pop()

    candidates.sort()
    dfs(0, target, [])
    return ans
