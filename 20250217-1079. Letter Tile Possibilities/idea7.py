# done by deepseek to convert idea 4
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        from collections import defaultdict

        groupedTiles = defaultdict(int)
        for t in tiles:
            groupedTiles[t] += 1

        count = 0
        # Initialize stack with a copy of the initial groupedTiles and starting index 0
        stack = [(dict(groupedTiles), 0)]

        while stack:
            current_gt, index = stack.pop()
            # Convert to sorted list of (char, count) to ensure consistent processing order
            tiles_list = sorted(current_gt.items())
            for i in range(index, len(tiles_list)):
                char, cnt = tiles_list[i]
                if cnt == 0:
                    continue
                # Create a new state with the current tile's count decremented
                new_gt = dict(current_gt)
                new_gt[char] -= 1
                count += 1  # Increment count for the new sequence
                # Push the current state back to process remaining tiles from the next index
                stack.append((current_gt, i + 1))
                # Push the new state to explore further sequences from the start
                stack.append((new_gt, 0))
                break  # Process the new state immediately (depth-first)
        return count

s = Solution()
print(s.numTilePossibilities('ACCCCA'))  # Output: 195