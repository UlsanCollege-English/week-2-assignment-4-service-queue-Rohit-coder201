from typing import List, Tuple

def take_next(queue: List[str]) -> Tuple[str | None, List[str]]:
    if not queue:
        return None, []
    return queue[0], queue[1:]

def move_to_back(queue: List[str], name: str) -> List[str]:
    if name in queue:
        q = queue.copy()
        q.remove(name)
        q.append(name)
        return q
    return queue.copy()

def interleave(q1: List[str], q2: List[str]) -> List[str]:
    result = []
    i = j = 0
    while i < len(q1) and j < len(q2):
        result.append(q1[i])
        result.append(q2[j])
        i += 1
        j += 1
    result.extend(q1[i:])
    result.extend(q2[j:])
    return result