from collections import deque

eggs = deque([int(x) for x in input().split(", ")])
paper_pieces = deque([int(y) for y in input().split(", ")])

box_size = 50
boxes_filled = 0

while eggs and paper_pieces:
    egg = eggs[0]
    paper = paper_pieces[-1]

    if egg <= 0:
        eggs.popleft()
        continue

    elif egg == 13:
        eggs.popleft()
        paper_pieces[0], paper_pieces[-1] = paper_pieces[-1], paper_pieces[0]
        continue

    eggs.popleft()
    paper_pieces.pop()

    if egg + paper <= 50:
        boxes_filled += 1

if boxes_filled > 0:
    print(f"Great! You filled {boxes_filled} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs:
    print(f"Eggs left: {', '.join([str(x) for x in eggs])}")
if paper_pieces:
    print(f"Pieces of paper left: {', '.join([str(y) for y in paper_pieces])}")
