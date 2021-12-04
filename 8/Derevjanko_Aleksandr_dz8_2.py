import re
RE_PARSED = re.compile(r'(\d+\.\d+\.\d+\.\d+).*(\[.*])\s"(GET)\s([^"]+)"\s(\d+)\s(\d+)')
with open('nginx_logs.txt') as f:
    for line in f:
        if len(RE_PARSED.findall(line)) != 0:
            print(RE_PARSED.findall(line)[0])
