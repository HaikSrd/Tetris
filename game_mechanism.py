import numpy as np




block =  4 #np.random.randint(5)
shapes = {
    0: 'cross',
    1: 'lightning',
    2: 'l',
    3: 'square',
    4: 'line'
}
shape = shapes[block]
if shape == 'cross':
    ones = np.array([[1,3],[1,4],[1,5],[0,4]])
elif shape == 'lightning':
    ones = np.array([[1,5],[0,4],[2,5],[1,4]])
if shape == 'l':
    ones = np.array([[1,4],[0,4],[2,4],[2,5]])
if shape == 'square':
    ones = np.array([[0,5],[0,4],[1,5],[1,4]])
if shape == 'line':
    ones = np.array([[1,4],[0,4],[2,4],[3,4]])

rotation_counter = 0
while True:
    grid = np.zeros((5, 10))
    key = input()

    if key == 's':
        for i in range(len(ones)):
            ones[i,0] += 1
    elif key == 'd':
        for i in range(len(ones)):
            ones[i,1] += 1
    elif key == 'a':
        for i in range(len(ones)):
            ones[i,1] -= 1
    elif key == 'w':
        if shape == 'l':
            if rotation_counter == 0:
                ones[1] += [1, 1]
                ones[2] += [-1, -1]
                ones[3] += [0,-2]
                rotation_counter += 1
            elif rotation_counter == 1:
                ones[1] += [1, -1]
                ones[2] += [-1, +1]
                ones[3] += [-2, 0]
                rotation_counter += 1
            elif rotation_counter == 2:
                ones[1] += [-1, -1]
                ones[2] += [+1, +1]
                ones[3] += [0, 2]
                rotation_counter += 1
            elif rotation_counter == 3:
                ones[1] += [-1, +1]
                ones[2] += [+1, -1]
                ones[3] += [2, 0]
                rotation_counter = 0
        elif shape == 'cross':
            if rotation_counter == 0:
                ones[0] += [1, 1]
                rotation_counter += 1
            elif rotation_counter == 1:
                ones[3] += [+1, -1]
                rotation_counter += 1
            elif rotation_counter == 2:
                ones[2] += [-1, -1]
                rotation_counter += 1
            elif rotation_counter == 3:
                ones[0] += [-1, -1]
                ones[2] += [1, 1]
                ones[3] += [-1, 1]
                rotation_counter = 0
        elif shape == 'line':
            if rotation_counter == 0:
                ones[0] += [1, 0]
                ones[1] += [+2, 1]
                ones[2] += [0, -1]
                ones[3] += [-1, -2]
                rotation_counter += 1
            elif rotation_counter == 1:
                ones[0] += [0, -1]
                ones[1] += [1, -2]
                ones[2] += [-1, 0]
                ones[3] += [-2, 1]
                rotation_counter += 1
            elif rotation_counter == 2:
                ones[0] += [-1, 0]
                ones[1] += [-2, -1]
                ones[2] += [0, 1]
                ones[3] += [1, 2]
                rotation_counter += 1
            elif rotation_counter == 3:
                ones[0] += [0, 1]
                ones[1] += [-1, 2]
                ones[2] += [1, 0]
                ones[3] += [2, -1]
                rotation_counter = 0


    for i in ones:
        grid[i[0],i[1]] = 1

    print(ones)
    print(grid)