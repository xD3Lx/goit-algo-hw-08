import heapq

def min_cost_of_connecting_cables(cables):
    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:
        # Choose the two smallest cables
        first_length = heapq.heappop(cables)
        second_length = heapq.heappop(cables)

        current_cable = first_length + second_length
        total_cost += current_cable

        # Add the current cable back to the heap
        heapq.heappush(cables, current_cable)

        print(f"Connecting cables {first_length} and {second_length} for cost {current_cable}. Total cost: {total_cost}")

    return total_cost


if __name__ == "__main__":
    cables = [10, 2, 5, 8, 6]
    min_cost = min_cost_of_connecting_cables(cables)
    print("Min cost of connecting cables:", min_cost)