class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m_rolls = sum(rolls)
        m = len(rolls)
        n_rolls = mean * (m+n) - m_rolls
        missing = []

        if n_rolls < n or n_rolls > 6*n:
            return []
            
        while len(missing) < n:
            complement = ceil(n_rolls / (n - len(missing)))
            missing.append(complement)
            n_rolls -= complement

        return missing
        