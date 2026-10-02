class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        stack = []

        for pos, speed in sorted(pairs):
            time = (target - pos) / speed

            while stack and time >= stack[-1]:
                stack.pop()
            stack.append(time)
        return len(stack)

