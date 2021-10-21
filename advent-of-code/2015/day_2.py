def calculate_wrapping_area(box_dim):
    side_surfaces = (box_dim[0] * box_dim[1], box_dim[0] * box_dim[2], box_dim[1] * box_dim[2])
    return 2 * sum(side_surfaces) + min(side_surfaces)


def calculate_ribbon_needed(box_dim):
    a, b, c = box_dim
    return 2 * (min(a + b, b + c, a + c)) + a * b * c


with(open("input/day-2.txt")) as file:
    data = map(lambda x: x.split('x'), file.readlines())
    total_paper_needed = 0  # part 1
    total_ribbon_needed = 0  # part 2
    for box in data:
        box = [int(size.replace('/n', '')) for size in box]
        total_paper_needed += calculate_wrapping_area(box)
        total_ribbon_needed += calculate_ribbon_needed(box)
    print(total_paper_needed)  # first part
    print(total_ribbon_needed)  # second part
