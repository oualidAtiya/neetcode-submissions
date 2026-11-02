class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        s = "\n\n\n\n" + "\n\n\n\n\n\n\n".join(strs)
        return s
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        s = s[4:]
        strs = s.split("\n\n\n\n\n\n\n")
        return strs