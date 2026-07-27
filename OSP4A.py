processes = [
    ["P1", 0, 5],
    ["P2", 1, 3],
    ["P3", 2, 8],
    ["P4", 3, 6]
]

n = len(processes)

completion_time = [0] * n
waiting_time = [0] * n
turnaround_time = [0] * n
start_time = [0] * n

current_time = 0

for i in range(n):
    process, arrival_time, burst_time = processes[i]

    if current_time < arrival_time:
        current_time = arrival_time

    start_time[i] = current_time
    completion_time[i] = current_time + burst_time

    turnaround_time[i] = completion_time[i] - arrival_time
    waiting_time[i] = start_time[i] - arrival_time

    current_time = completion_time[i]

total_waiting_time = sum(waiting_time)
total_turnaround_time = sum(turnaround_time)

average_waiting_time = total_waiting_time / n
average_turnaround_time = total_turnaround_time / n

print("Shreyash Kadam S091")
print("FCFS CPU Scheduling")
print("-------------------")

print("Process\tAT\tBT\tST\tCT\tWT\tTAT")

for i in range(n):
    print(
        f"{processes[i][0]}\t"
        f"{processes[i][1]}\t"
        f"{processes[i][2]}\t"
        f"{start_time[i]}\t"
        f"{completion_time[i]}\t"
        f"{waiting_time[i]}\t"
        f"{turnaround_time[i]}"
    )

print("\nAverage Waiting Time:", average_waiting_time, "ms")
print("Average Turnaround Time:", average_turnaround_time, "ms")

print("\nGantt Chart:")
print("| P1 | P2 | P3 | P4 |")
print("0\t5\t8\t16\t22")

