import numpy as np


def furthest_view(this_tree, list_range):
    count = 0
    found_edge = False
    for check_tree in list_range:
        if check_tree >= this_tree:
            found_edge = True
            break
        else:
            count += 1
    if found_edge:
        count += 1
    return count

tree_list = []
with open('input.txt') as data_file:
    for line in data_file:
        tree_list.append(list(line.strip()))

trees = np.array(tree_list, dtype=int)
print(trees)
nrows, ncols = np.shape(trees)
vis_count = 0
best_scenic = 0
for ri in range(nrows):
    for ci in range(ncols):
        if ri in (0, nrows-1) or ci in (0, ncols-1):
            vis_count += 1
        else:
            this_tree = trees[ri, ci]
            print(f"\nThis tree: {this_tree}")
            # row check
            left  = list(trees[ri, :ci])
            left.reverse()
            right = list(trees[ri, ci+1:])
            # col check
            up    = list(trees[:ri, ci])
            up.reverse()
            down  = list(trees[ri+1:, ci])

            print(f"left:  {left}")
            print(f"right: {right}")
            print(f"up:    {up}")
            print(f"down:  {down}")

            if np.all( this_tree > left ) or np.all( this_tree > right ) or np.all( this_tree > up ) or np.all( this_tree > down ):
                #print(row_other)
                vis_count += 1

                # Part 2
                left_view  = furthest_view(this_tree, left)
                right_view = furthest_view(this_tree, right)
                up_view    = furthest_view(this_tree, up)
                down_view  = furthest_view(this_tree, down)
                scenic = left_view * right_view * up_view * down_view
                print(left_view, right_view, up_view, down_view)
                print(scenic)
                if scenic > best_scenic:
                    best_scenic = scenic


print(f"Part 1: {vis_count}")
print(f"Part 2: {best_scenic}")
