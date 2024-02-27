from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    now_weight = 0
    idx = 0
    
    while bridge:
        answer += 1
        out_truck = bridge.popleft()
        now_weight -= out_truck
        if idx < len(truck_weights):
            if now_weight + truck_weights[idx] <= weight:
                bridge.append(truck_weights[idx])
                now_weight += truck_weights[idx]
                idx += 1
            else:
                bridge.append(0)
    return answer
