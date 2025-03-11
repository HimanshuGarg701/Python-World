from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        degree = [0] * numCourses
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            degree[course] += 1
        queue = deque(index for index, value in enumerate(degree) if value == 0)
        completed = 0
        while queue:
            node = queue.popleft()
            completed += 1
            for neighbor in graph[node]:
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    queue.append(neighbor)
        return completed == numCourses
