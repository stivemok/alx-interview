#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Rotate 2D matrix 90 degrees"""
    width = len(matrix[0])
    height = len(matrix)
    total_items = width * height
    map_ = build_map(matrix, total_items, width)
    for index in map_:
        prev_index = index
        value = map_[prev_index]["value"]
        new_index = map_[prev_index]["new_index"]
        row, index = compute_row_and_index(new_index, width)
        matrix[row][index] = value


def build_map(m, length, width):
    """returns a map of prev_index and their next positions"""
    dct = {
        i: {
            "new_index": get_new_index(i, width),
            "value": get_value(m, i, width)
        }
        for i in range(length)
    }
    return dct


def get_new_index(i, width):
    """computes new position"""
    current_index = i % width
    current_row = int(i / width)
    next_index = width - 1 - current_row
    next_row = current_index
    next_position = next_row * width + next_index
    return next_position


def get_value(m, i, width):
    """gets the value of a 2d array by denormalizing its flattened index"""
    current_index = i % width
    current_row = int(i / width)
    return m[current_row][current_index]


def compute_row_and_index(flat_index, width):
    """returns denormalized row and index from a flattened 2d array index"""
    row = int(flat_index / width)
    index = flat_index % width
    return row, index


def printx(mlist):
    """custom print function to print 2d array"""
    print("[")
    for item in mlist:
        print("  ", str(item) + ",")
    print("]")


def build_matrix(n):
    """ builds n * n 2d matrix """
    parent = []
    y = 1
    for i in range(n):
        child = []
        for x in range(y, n * n + 1):
            child.append(x)
            if x % n == 0 and x != 1:
                y = x + 1
                break
        parent.append(child)
    return parent


if __name__ == "__main__":
    matrix = build_matrix(3)

    rotate_2d_matrix(matrix)
    printx(matrix)
    print()
    matrix = build_matrix(5)

    rotate_2d_matrix(matrix)
    printx(matrix)
