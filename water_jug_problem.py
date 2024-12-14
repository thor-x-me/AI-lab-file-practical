from collections import deque


def water_jug_problem(jug1_capacity, jug2_capacity, target):
    # Use a set to store visited states
    visited = set()
    # Queue for BFS with initial state (0, 0)
    queue = deque([(0, 0)])

    while queue:
        # Dequeue the front state
        current_jug1, current_jug2 = queue.popleft()

        # If the target is reached, return the state
        if current_jug1 == target or current_jug2 == target:
            return (current_jug1, current_jug2)

        # If the state has already been visited, skip it
        if (current_jug1, current_jug2) in visited:
            continue

        # Mark the state as visited
        visited.add((current_jug1, current_jug2))

        # Generate all possible states
        possible_states = [
            (jug1_capacity, current_jug2),  # Fill jug1
            (current_jug1, jug2_capacity),  # Fill jug2
            (0, current_jug2),  # Empty jug1
            (current_jug1, 0),  # Empty jug2
            # Pour jug1 into jug2
            (max(current_jug1 - (jug2_capacity - current_jug2), 0),
             min(current_jug2 + current_jug1, jug2_capacity)),
            # Pour jug2 into jug1
            (min(current_jug1 + current_jug2, jug1_capacity),
             max(current_jug2 - (jug1_capacity - current_jug1), 0))
        ]

        # Add all valid states to the queue
        for state in possible_states:
            if state not in visited:
                queue.append(state)

    return None  # If no solution is found


# Example usage
jug1_capacity = 4
jug2_capacity = 3
target = 2

result = water_jug_problem(jug1_capacity, jug2_capacity, target)
if result:
    print(f"Target reached with state: {result}")
else:
    print("No solution found")
