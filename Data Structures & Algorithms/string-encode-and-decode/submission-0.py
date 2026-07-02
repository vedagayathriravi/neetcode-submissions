#So for this lets say we have ["hello","world"] if we are encoding it directly it will be become helloworld ,which will be hard to decode,but what if we put a sign like # to extract the words,but that also wont haappen because what if the words has that symbol already so the final solution for is 
# using 5#hello5#world so here it will take after pound and how many numbers it needs to extract
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res