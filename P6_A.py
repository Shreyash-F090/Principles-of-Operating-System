print("Shreyash Kadam S091")

processes = [
    ["P1", 0, 5],
    ["P2", 4, 2],
    ["P3", 5, 4]
]

quantum = 2
n = len(processes)

remaining = [5, 2, 4]
completion = [0, 0, 0]
waiting = [0, 0, 0]
turnaround = [0, 0, 0]

queue = []
time = 0
completed = 0
added = [False] * n

gantt = []
gantt_time = [0]

while completed < n:

    for i in range(n):
        if processes[i][1] <= time and not added[i]:
            queue.append(i)
            added[i] = True

    if not queue:
        time += 1
        continue

    i = queue.pop(0)

    start = time
    run = min(quantum, remaining[i])

    time += run
    remaining[i] -= run

    gantt.append(processes[i][0])
    gantt_time.append(time)

    for j in range(n):
        if processes[j][1] <= time and not added[j]:
            queue.append(j)
            added[j] = True

    if remaining[i] > 0:
        queue.append(i)
    else:
        completion[i] = time
        completed += 1

for i in range(n):
    turnaround[i] = completion[i] - processes[i][1]
    waiting[i] = turnaround[i] - processes[i][2]

print("\nRound Robin Scheduling")
print("----------------------")

print("Process\tAT\tBT\tWT\tTAT")

for i in range(n):
    print(f"{processes[i][0]}\t{processes[i][1]}\t{processes[i][2]}\t"
          f"{waiting[i]}\t{turnaround[i]}")

print("\nAverage Waiting Time:", sum(waiting) / n, "ms")
print("Average Turnaround Time:", sum(turnaround) / n, "ms")

print("\nGantt Chart")
print("-----------")

for p in gantt:
    print("|", p, end=" ")

print("|")

for t in gantt_time:
    print(t, end="\t")

print()
