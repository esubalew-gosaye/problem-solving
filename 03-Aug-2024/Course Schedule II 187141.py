# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        if not prerequisites and numCourses > 0:
            return [i for i in range(numCourses - 1, -1, -1)]

        course_dict = defaultdict(list) # Add courses to prerequisites.
        incoming_count = {} # Count num of prerequisites.

        for course, prereq in prerequisites:
            course_dict[prereq].append(course)
            incoming_count[course] = incoming_count.get(course, 0) + 1
            incoming_count[prereq] = incoming_count.get(prereq, 0)
        

        bfs = deque()

        for i in range(numCourses):
            if incoming_count.get(i, 0) == 0:
                bfs.append(i)

        result = deque()
        while bfs:
            node = bfs.popleft()
            result.append(node)
            for neigh in course_dict[node]:
                incoming_count[neigh] -= 1

                if incoming_count[neigh] == 0:
                    bfs.append(neigh)

        return result if len(result) == numCourses else []