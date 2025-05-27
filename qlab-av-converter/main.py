import argparse
from pathlib import Path
import sys
import subprocess

from args_parser import parse_arguments


def parse_probe(streams: list[str]) -> dict['str', bool]:
    to_convert = {'audio': False, 'video': False, 'pic': False}

    for stream in streams:
        for line in stream.split('\n'):
            print(line)

        break
    pass

    return to_convert


def main(args: dict):
    result = subprocess.run(
        f'ffprobe -show_streams {args["filename"]}',
        shell=True,
        capture_output=True,
        text=True
    )
    if result.returncode > 0:
        print(f'ffprobe failed with returncode: {
              result.returncode}, error message: \'{result.stderr}\'',
              file=sys.stderr)
        exit(2)

    streams = [stream for stream in result.stdout.split('[STREAM]') if stream]
    if len(streams) < 1:
        print('ffprobe did not found any stream', file=sys.stderr)
        exit(3)

    parse_probe(streams=streams)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='qlab-av-converter',
        description='Convert av file to supported format for qlab 5')

    parser.add_argument('filename', type=Path,
                        help='The path to the av file')
    parser.add_argument('-ca', '--codec-audio', type=str, default='WAV',
                        help='The audio codec that you want to use. (Default: WAV)')
    parser.add_argument('-as', '--audio-samplerate', type=float, default=48.0,
                        help='The samplerate you want to use (kHz). (Default: 48.0)')
    parser.add_argument('-ab', '--audio-bitdepth', type=int, default=32,
                        help='The audio bit depth you want to use. (Default: 32)')
    parser.add_argument('-ac', '--audio-channels', type=int, default=2,
                        help='How many audio channels you want to use. (Default: 2)')
    parser.add_argument('-cv', '--codec-video', type=str,
                        help='The video codec that you want to use. (Default: ProRes 422 proxy)')
    parser.add_argument('-vr', '--video-resolution', type=str,
                        help='The resolustion you want to use. (Default: 1920x1080)')

    args = parse_arguments(parser=parser)
    streams = main(args=args)
