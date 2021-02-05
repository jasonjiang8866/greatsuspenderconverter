import re

filename_in = 'input.html'
filename_out = 'output.html'
pattern = '(?<=uri=).*'
search = re.compile(pattern)

with open(filename_in) as f:
    with open(filename_out, 'w+') as f2:
        for line in f.readlines():
            if 'chrome-extension' in line:
                result = search.search(line)
                f2.write(result[0]+'\n')
            else:
                f2.write(line)
