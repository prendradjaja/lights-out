def main():
    for line in open('mnemonics', 'r'):
        if is_data_line(line):
            try:
                check_line(line)
            except AssertionError:
                print(line)
                raise

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
    in_bin_raw = in_bin
    out_bin_raw = out_bin
    in_dec = int(in_dec)
    out_dec = int(remove_comment(out_dec))
    in_bin = parse_binary(in_bin)
    out_bin = parse_binary(out_bin)
    assert in_dec == in_bin
    assert out_dec == out_bin
    assert get_mask(in_bin_raw) == out_bin_raw
    print(in_dec, 'ok')

def get_mask(in_bin_raw):
    masks = {
        0: 0b11000,
        1: 0b11100,
        2: 0b01110,
        3: 0b00111,
        4: 0b00011
    }
    out = 0
    for (i, char) in enumerate(in_bin_raw):
        if char == '1':
            out ^= masks[i]
    return format(out, '05b').replace('0', '.')

def parse_binary(s):
    return int(s.replace('.', '0'), 2)

if __name__ == '__main__':
    main()
