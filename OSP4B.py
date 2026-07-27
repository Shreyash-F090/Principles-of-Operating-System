processes = [
    ["P1", 0, 7],
    ["P2", 2, 4],
    ["P3", 4, 1],
    ["P4", 5, 4]
]

n = len(processes)
completed = [False] * n

completion_time = [0] * n
waiting_time = [0] * n
turnaround_time = [0] * n
start_time = [0] * n

current_time = 0
completed_count = 0
gantt = []

while completed_count < n:
    shortest = -1

    for i in range(n):
        if not completed[i] and processes[i][1] <= current_time:
            if shortest == -1 or processes[i][2] < processes[shortest][2]:
                shortest = i
            elif processes[i][2] == processes[shortest][2]:
                if processes[i][1] < processes[shortest][1]:
                    shortest = i

    if shortest == -1:
        current_time += 1
        continue

    process, arrival_time, burst_time = processes[shortest]

    start_time[shortest] = current_time
    completion_time[shortest] = current_time + burst_time
    waiting_time[shortest] = start_time[shortest] - arrival_time
    turnaround_time[shortest] = completion_time[shortest] - arrival_time

    current_time = completion_time[shortest]
    completed[shortest] = True
    completed_count += 1

    gantt.append((process, start_time[shortest], completion_time[shortest]))

average_waiting_time = sum(waiting_time) / n
average_turnaround_time = sum(turnaround_time) / n

print("\nShreyash Kadam S091")
print("\nNon-Preemptive SJF CPU Scheduling")
print("=================================")

print("\nProcess\tAT\tBT\tST\tCT\tWT\tTAT")

for i in range(n):
    print(f"{processes[i][0]}\t{processes[i][1]}\t{processes[i][2]}\t"
          f"{start_time[i]}\t{completion_time[i]}\t"
          f"{waiting_time[i]}\t{turnaround_time[i]}")

print("\nAverage Waiting Time:", average_waiting_time, "ms")
print("Average Turnaround Time:", average_turnaround_time, "ms")

print("\nGantt Chart")
print("-----------")

for process, start, end in gantt:
    print(f"| {process} ", end="")

print("|")

for process, start, end in gantt:
    print(f"{start}\t", end="")

print(gantt[-1][2])
