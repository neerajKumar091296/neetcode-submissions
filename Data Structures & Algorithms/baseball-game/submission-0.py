class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        r = []

        for ops in operations:
            if ops not in ["+","C","D"]:
                r.append(int(ops))
            elif ops == "+":
                r.append(r[-1] + r[-2])
            elif ops == "C":
                r.pop()
            elif ops == "D":
                r.append(2 * r[-1])

        return sum(r)