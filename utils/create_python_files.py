"""
creates python files in ../aufgaben
"""
def create_python_file(name):
    file = open(f"../aufgaben/{name}.py", "w")

def main():
    for i in range(37,103):
        create_python_file(f"a{i}_")

main()

