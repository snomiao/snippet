default_ignores = [".git", ".venv", "__pycache__"]
def is_ignored(path, ignores = default_ignores):
    for x in ignores:
        if x in path:
            return True
    return False

def walk_with_ignores(path, depth, ignores = default_ignores):
    """Recursively list files and directories up to a certain depth"""
    depth -= 1
    with os.scandir(path) as p:
        for entry in p:
            if is_ignored(entry.path, ignores):
                continue
            yield entry.path
            if entry.is_dir() and depth > 0:
                yield from walk_with_ignores(entry.path, depth, ignores)
