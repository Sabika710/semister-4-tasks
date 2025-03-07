from collections import deque

def waterJugProblem(capacity1, capacity2, goal):
    queue = deque()
    visited = set()

    queue.append((0, 0))
    visited.add((0, 0))

    actions = []

    while queue:
        jug1, jug2 = queue.popleft()
        actions.append((jug1, jug2))

        # Check if target is achieved
        if jug1 == goal or jug2 == goal:
            print("Solution Found")
            for action in actions:
                print(action)
            return True

        # Apply rules
        rules = [
            (capacity1, jug2),  # 1: fill jug1
            (jug1, capacity2),  # 2: fill jug2
            (0, jug2),  # 3: empty jug1
            (jug1, 0),  # 4: empty jug2
            (max(0, jug1 - (capacity2 - jug2)), min(capacity2, jug2 + jug1)),  # 5: pour jug1 into jug2 until jug2 is full
            (min(capacity1, jug1 + jug2), max(0, jug2 - (capacity1 - jug1))),  # 6: pour jug2 into jug1 until jug1 is full
            (jug1 + jug2, 0),  # 7: pour jug1 into jug2 until jug1 is empty
            (0, jug1 + jug2),  # 8: pour jug2 into jug1 until jug2 is empty
        ]

        for state in rules:
            if state not in visited:
                visited.add(state)
                queue.append(state)

    print("No Solution found")
    return False

# Test the function
jug1Capacity = 4
jug2Capacity = 3
target = 2

waterJugProblem(jug1Capacity, jug2Capacity, target)