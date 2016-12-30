def get_path0(maze):
    if not maze or not len(maze): return None
    path = []
    if _get_path0(maze, len(maze) - 1, len(maze[0]) - 1, path):
        return path
    return path

def _get_path0(maze, row, col, path):
    if col < 0 or row < 0 or not maze[row][col]:
        return False

    is_at_origin = not row and not col

    if (is_at_origin or _get_path0(maze, row, col - 1, path) or 
            _get_path0(maze, row - 1, col, path)):
        path.append((row, col))
        return True

    return False

def get_path2(maze):
    if not maze or not len(maze): return None
    path = []
    _get_path2(maze, 0, 0, path)
    return path

def _get_path2(maze, row, col, path):
    if row == len(maze)-1 and col == len(maze[0])-1:
        path.append((row, col))
    elif row+1 < len(maze) and maze[row+1][col]:
        path.append((row, col))
        _get_path2(maze, row+1, col, path)
    elif col+1 < len(maze[row]) and maze[row][col+1]:
        path.append((row, col))
        _get_path2(maze, row, col+1, path)
    else:
        path[:] = []
