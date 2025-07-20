class Solution():
    def compareVersion(self, version1, version2):
        v1 = version1.split('.')
        v2 = version2.split('.')

        max_len = max(len(v1), len(v2))


        for i in range(max_len):

            rev1 = int(v1[i]) if i < len(v1) else 0

            rev2 = int(v2[i]) if i < len(v2) else 0

            if rev1 < rev2:
                return -1
            
            elif rev1 > rev2:
                return 1
            
        return 0
    

sol = Solution()

print(sol.compareVersion("1.02", "1.10"))

# print(sol.compareVersion("3.0", "1.002"))
