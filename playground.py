import re

def get_lines(file_path):
    return open(file_path, "r").readlines()

def remove_noncontent(line):
    if line in ['\n', ' \n', '"\n', '" \n']:
        return False 
    
    foo = re.search(' =', line)

    if foo:
        return False
    
    else:
        return True
    
def clean_lines(line):
    # remove <unk> flags
    line = re.sub(r'<unk>', '', line)

    # remove 
    line = re.sub(r'\([^)]*\)', '', line)
    line = re.sub(r'\[[^\]]*\]', '', line)
    line = re.sub(r'""', '', line)

    return line


if __name__ == "__main__":
    lines = get_lines("data/train.txt")
    lines = list(filter(remove_noncontent, lines))
    lines = list(map(clean_lines, lines))
    print(lines[2000:2010])
