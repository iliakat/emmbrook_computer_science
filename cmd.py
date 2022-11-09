from subprocess import PIPE, Popen

command = ""
path = "C:\\Users\\iliak\\Desktop\\"

def cd_set(path, **kwargs):
    new_path = ""
    for i in args:
        new_path+=f"{i} "
    return new_path

def cd_plus(path, **kwargs):
    temp = ""
    for i in args:
        temp += f"{i} "
    new_path = path+temp
    return new_path

def cd_back(path, num=1):
    new_path = ""
    end = int(num)+1
    for i in path.split("\\")[0:-end]:
        new_path += f"{i}\\"
    return new_path

print(f"{'='*40}\n\tCMD by def1de\n\tv1.0.7\n\tGood look, start now!\n{'='*40}\n\n")
while True:
    command = str(input(f"{path} >>> "))
    if command == "exit":
        input("\nPress ENTER to continue...")
        break
    elif command.split()[0] == "cd":
        params = command.split()[1:]
        args = params[1:]
        if params[0] == "-":
            path = cd_back(path=path, num=args[0])
        elif params[0] == "+":
            path = cd_plus(path=path, args=args[1:])
        elif params[0] == "=":
            path = cd_set(path=path, dir=args[1])
        else:
            print("Unknown parameter")
    else:
        with Popen(command, stdout=PIPE, stderr=None, shell=True, cwd=path) as process:
            output = process.communicate()[0].decode("utf-8")
            print(output)