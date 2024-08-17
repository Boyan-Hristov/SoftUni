w = float(input())
h = float(input())

workspaces_w = w // 1.2
workspaces_h = (h - 1) // 0.7

all_workspaces = int(workspaces_w * workspaces_h - 3)

print(int(all_workspaces))

