class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # Build adj list as graph
        # course -> prereq
        # {c: [p1, p2, ...]}
        adj_list = {}
        indegree = {}
        
        # Used to calculated the starting nodes
        track_start = set()
        # Add all courses to track_start, remove later when we know
        # a course has a prereq
        for c in range(numCourses):
            track_start.add(c)


        # input is in [course, prereq order]
        for c, p in prerequisites:

            # As we start from follow up courses and traverse 
            # towards the prereqs, we remove all prereqs
            # leaving courses that have no arrows that point out
            if c in track_start:
                track_start.remove(c)

            if p not in adj_list:
                adj_list[p] = [c]
            else:
                adj_list[p].append(c)

            indegree[c] = indegree.get(c, 0) + 1
        

        q = deque(track_start)

        res = []

        while q:
            p = q.popleft()
            res.append(p)

            if p in adj_list:
                for c in adj_list[p]:
                    indegree[c] -= 1

                    if indegree[c] == 0:
                        q.append(c)

        if len(res) == numCourses:
            return res
            
        return []