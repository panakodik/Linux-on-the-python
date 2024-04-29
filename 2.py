import subprocess

MARKS = '''!()-[]{};?@#$%:'"\,./^&;*_ ='''


def subproc_file(directory: str, find_name: str, find_word='Yes'):
    result = subprocess.run(directory, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    if result.returncode == 0:
        lst = out.split("\n")
        if find_name in lst:
            for x in find_name:
                if x in MARKS:
                    find_name = find_name.replace(x, " ")
            if find_word in find_name:
                print('Find')
            else:
                print('No find')
            return True
        return False
    return False


if __name__ == '_main_':
    print(subproc_file('cat /etc/os-release', 'VERSION="22.04.1 LTS (Jammy Jellyfish)"', '04'))
