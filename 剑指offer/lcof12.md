剑指 Offer 12. 矩阵中的路径
====
https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/
```
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。
```
![image](https://assets.leetcode.com/uploads/2020/11/04/word2.jpg)
```
示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true

示例 2：
输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
```

## 思路

给定网格， 搜索 🔍 就要想到 DFS 啦。

没有给定初始位置， 所以就两个循环 dfs 找初始位置。

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(i, j, k):
            
            ## 剪枝
            if i < 0 or i > len(board) - 1 or j < 0 or j > len(board[0]) - 1 or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            ## 标记为已访问， 避免重复选择
            board[i][j] = ''
            ans = dfs(i - 1, j, k + 1) or dfs(i + 1, j, k + 1) or dfs(i, j - 1, k + 1) or dfs(i, j + 1, k + 1)

            ## 还原网格
            board[i][j] = word[k]
            return ans

    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
        
        return False
```

## 复杂度分析
- 时间复杂度：O(MN * 3^K) 
    - 起点寻找， 需要两个循环: MN。

    - 寻找匹配的字符串， 上下左右四个位置舍弃回头的位置一共有三个选择， 最坏的时间复杂度是找 k 的长度 3^k。

- 空间复杂度： O(K) 递归栈的深度不会超过 k