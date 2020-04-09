import os

def print_tree(startpath):

    dexclude = ['.git']
    fexclude = ['.DS_Store']

    for root, dirs, files in os.walk(startpath):
        dirs[:] = [d for d in dirs if d not in dexclude]
        files[:] = [f for f in files if f not in fexclude]

        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 2 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 2 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

print_tree(os.getcwd())