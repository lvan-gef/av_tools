import argparse
from pathlib import Path
import sys
import subprocess


def main(path: Path):
    result = subprocess.run(
        f'ffprobe -show_streams {path}',
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

    print(len(streams))

    return streams


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='qlab-video-converter',
        description='Convert video to supported format for qlab')

    parser.add_argument('filename', type=Path,
                        help='The path to the video file')
    args = parser.parse_args()

    args.filename = args.filename.resolve()
    if not args.filename.exists():
        print(f'The video: "{args.filename}" does not exists', file=sys.stderr)
        exit(1)

    streams = main(path=args.filename)
