# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/27 上午10:25
Author: ybx
"""

'''
从网格的左上角走到右下角 一共有多少条路径 每次只能是从当前节点的向下或者向右走一步

'''

class Solution(object):

    def uniquePaths(self, m,n):
        dp = [[False for _ in range(m)] for _ in range(n)]
        print(dp)
        for i in range(m):
            # 按照行的方向
            dp[0][i] = 1
        for j in range(n):
            dp[j][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[j][i] = dp[j][i-1] + dp[j-1][i]

        return dp[n-1][m-1]






if __name__ == '__main__':
    s = Solution()
    result = s.uniquePaths(3,2)
    print(result)