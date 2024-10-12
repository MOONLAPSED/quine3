import ast

class State:
    state = 2

def get_source():
    with open(__file__, 'r') as file:
        return file.read()

def increment_state(source):
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == 'State':
            for sub_node in node.body:
                if isinstance(sub_node, ast.Assign) and sub_node.targets[0].id == 'state':
                    sub_node.value.n += 1
                    break
    return ast.unparse(tree)

def main():
    if State.state >= 1:
        print('buy the stock')
    source = get_source()
    new_source = increment_state(source)
    print(new_source)
    with open(__file__, 'w') as file:
        file.write(new_source)
if __name__ == '__main__':
    main()