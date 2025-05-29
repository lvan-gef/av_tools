
def parse_probe(streams: list[str]) -> dict['str', bool]:
    to_convert = {'audio': False, 'video': False, 'pic': False}

    for stream in streams:
        for line in stream.split('\n'):
            print(line)

        break
    pass

    return to_convert
