from typing import List

def meeting_planner(slotsA: List[List[int]], slotsB: List[List[int]], dur: int) -> List[int]:
    pointerA, pointerB = 0, 0
    while pointerA < len(slotsA) and pointerB < len(slotsB):
        startA, endA = slotsA[pointerA]
        startB, endB = slotsB[pointerB]

        # Find the overlap between slots
        start = max(startA, startB)
        end = min(endA, endB)

        if end - start >= dur:
            return [start, start + dur]

        # Move the pointer that has the earlier ending time
        if endA < endB:
            pointerA += 1
        else:
            pointerB += 1

    return []

