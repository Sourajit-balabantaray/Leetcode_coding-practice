class Solution:
    def groupAnagrams(self, strs):
        groups = []

        for word in strs:
            x = list(word)
            x.sort()

            found = False

            for group in groups:
                y = list(group[0])
                y.sort()

                if x == y:
                    group.append(word)
                    found = True
                    break

            if found == False:
                groups.append([word])

        return groups
