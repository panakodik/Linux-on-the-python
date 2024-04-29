import subprocess


def subproc_file(directory: str, find_name: str) -> bool:
    result = subprocess.run(directory, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    if result.returncode == 0:
        lst = out.split("\n")
        if find_name in lst:
            return True
        return False
    return False


if __name__ == '_main_':
    print(subproc_file('cat /etc/os-release', 'VERSION="22.04.1 LTS (Jammy Jellyfish)"'))
