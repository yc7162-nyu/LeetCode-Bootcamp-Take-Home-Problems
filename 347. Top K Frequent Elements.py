class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hmap = defaultdict(int)

        for n in nums:
            hmap[n] += 1
        
        # No max heap in python, so we do min heap of -ve frequency
        heap = []

        # Store pairs of (-freq, val) in heap
        for val, freq in hmap.items():
            heap.append((-freq, val))

        # Heapify in python is an O(len(array)) operation
        heapq.heapify(heap)

        # Then we can pop from the heap k times
        ans = []

        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        
        return ans

        # Time Complexity: O(3n + klogk) => O(n)
        # Space Complexity: O(2n) => O(n)  

    '''
        Build frequency map

        maintain a maxheap of (freq, val) pairs
    '''