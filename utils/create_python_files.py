"""
creates python files in ../aufgaben
"""
def create_python_file(name):
    file = open(f"../aufgaben/{name}.py", "w")

def main():
    for i in range(70,103):
        create_python_file(f"a{i}_")

if __name__=="__main__":
    main()

