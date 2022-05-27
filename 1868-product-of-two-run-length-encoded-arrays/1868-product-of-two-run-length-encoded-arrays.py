class Solution:
    def findRLEArray(self, encoded1, encoded2):
        i, j, res, ans = 0, 0, [], []

        while i < len(encoded1) and j < len(encoded2):
            if encoded1[i][1] < encoded2[j][1]:
                res.append([encoded1[i][0] * encoded2[j][0], encoded1[i][1]])
                encoded2[j][1] -= encoded1[i][1]
                i += 1
            elif encoded1[i][1] > encoded2[j][1]:
                res.append([encoded1[i][0] * encoded2[j][0], encoded2[j][1]])
                encoded1[i][1] -= encoded2[j][1]
                j += 1
            else:
                res.append([encoded1[i][0] * encoded2[j][0], encoded2[j][1]])
                i += 1
                j += 1


        for i in res:
            if ans and ans[-1][0] == i[0]:
                ans[-1][1] += i[1]
            else:
                ans.append(i)

        return ans