import numpy as np


def kornig_hcube_mat(dims):
    if dims == 1:
        result = np.array([[1]], dtype=int)
    else:
        lower_dim_mat = kornig_hcube_mat(dims - 1)
        identity = np.identity(2**(dims-2), dtype=int)
        result = np.block([
            [lower_dim_mat, identity],
            [identity, lower_dim_mat]
        ])
    return result


def show_mat(mat):
    for row in mat:
        print(''.join(['.' if x == 0 else '1' for x in row]))
    return


def show_mat_mul(mat1, mat2, mat3):
    for row1, row2, row3 in zip(mat1, mat2, mat3):
        rowstr = ''.join(['.' if x == 0 else '1' for x in row1])
        rowstr += '\t'
        rowstr += ''.join(['.' if x == 0 else '1' for x in row2])
        rowstr += '\t'
        rowstr += ''.join(['.' if x == 0 else '1' for x in row3])
        print(rowstr)
    return

if __name__ == '__main__':
    dims = 7
    night_count = 2**(dims-2)
    nights = [kornig_hcube_mat(dims) for _ in range(night_count)]
    '''
    checks = [
            [0, 1, 2, 3, 4], 
            [1, 2, 3, 4, 5],
            [2, 3, 4, 5, 6],
            [3, 4, 5, 6, 7],
            #[3, 4, 5, 6, 7],
            #[2, 3, 4, 5, 6],
            #[1, 2, 3, 4, 5],
            ]
    checks = [[]]*4
    checks = [
            [0, 1, 2, 3, 4, 5, 6, 7, 8], 
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [2, 3, 4, 5, 6, 7, 8, 9, 10],
            [3, 4, 5, 6, 7, 8, 9, 10, 11],
            [4, 5, 6, 7, 8, 9, 10, 11, 12],
            [5, 6, 7, 8, 9, 10, 11, 12, 13],
            [6, 7, 8, 9, 10, 11, 12, 13, 14],
            [7, 8, 9, 10, 11, 12, 13, 14, 15],
            ]
    '''
    checks = [list(range(i, i+night_count+1)) for i in range(night_count)]

    for night, checklist in zip(nights, checks):
        for check in checklist:
            night[check] = 0

    print('Full transition matrix')
    show_mat(kornig_hcube_mat(dims))

    current_night = nights[0]
    for next_night_matrix in nights[1:]:
        new_night = current_night @ next_night_matrix
        print('------------------')
        print('Current night \t Transition matrix \t Result')
        show_mat_mul(current_night, next_night_matrix, new_night)
        # active_hole_count = len(np.nonzero(current_night)[0])
        # print('total paths:', np.sum(current_night))
        # print('active terminals:', active_hole_count)
        # print('active terminal density:', np.sum(current_night)/(active_hole_count + 0.00001))
        current_night = new_night
