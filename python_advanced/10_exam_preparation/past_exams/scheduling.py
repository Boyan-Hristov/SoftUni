from collections import deque

jobs = deque([int(x) for x in input().split(", ")])
index = int(input())

cycles = 0

jobs_copy = jobs.copy()

while jobs_copy:
    job = min(jobs_copy)
    job_index = jobs.index(job)
    if job_index == index:
        cycles += job
        break
    else:
        cycles += job
        jobs_copy.remove(job)

print(cycles)
