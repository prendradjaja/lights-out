def main():
    for line in open('mnemonics', 'r'):
        if is_data_line(line):
            check_line(line)

def is_data_line(line):
    parts = line.split()
    return parts and is_int(parts[0])

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def remove_comment(out_dec):
    if ':' in out_dec:
        return out_dec.split(':')[0]
    else:
        return out_dec

def check_line(line):
    parts = line.split(maxsplit=3)
    try:
        in_dec, in_bin, out_bin, out_dec = parts
    except ValueError:
        print(parts)
        raise
    in_dec = int(in_dec)
    out_dec = int(remove_comment(out_dec))
    in_bin = parse_binary(in_bin)
    out_bin = parse_binary(out_bin)
    assert in_dec == in_bin
    assert out_dec == out_bin
    print(in_dec, 'ok')

def parse_binary(s):
    return int(s.replace('.', '0'), 2)

if __name__ == '__main__':
    main()
