
class Solution:
    @staticmethod
    def occurrences(string, substring):
        count = start = 0
        while True:
            start = string.find(substring, start) + 1
            if start > 0:
                count += 1
            else:
                return count

    def longestDupSubstring(self, s: str) -> str:
        max_dublicate_string = {
            'value': '',
            'counter': 0,
            'len': 0,
        }
        for length in range(1, len(s)):
            for i in range(len(s) - length):
                substring = s[i:length + i:]
                counter = self.occurrences(s, substring)
                if counter >= 2:
                    if length > max_dublicate_string['len']:
                        max_dublicate_string['value'] = substring
                        max_dublicate_string['len'] = length

        return max_dublicate_string['value']


s = Solution()
answer = s.longestDupSubstring(input())
print(answer)
