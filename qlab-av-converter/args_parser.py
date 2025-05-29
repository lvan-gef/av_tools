import argparse
import sys

from defaults import SUPPORTED_AUDIO, SUPPORTED_VIDEO


def parse_arguments(parser: argparse.ArgumentParser) -> dict:
    args = parser.parse_args()

    args.filename = args.filename.resolve()
    if not args.filename.exists():
        print(f'The file: "{args.filename}" does not exists', file=sys.stderr)
        exit(1)

    parse_args = {'filename': args.filename}
    if args.codec_audio.upper() not in SUPPORTED_AUDIO['codec']:
        print(f'Not supported audio codec: {
              args.codec_audio}', file=sys.stderr)
        exit(2)
    else:
        parse_args['audio_codec'] = args.codec_audio.upper()

    if args.audio_samplerate < SUPPORTED_AUDIO['samplerate']['min'] or args.audio_samplerate > SUPPORTED_AUDIO['samplerate']['max']:
        print(f'Value: {args.audio_samplerate} is out of bound should be between: {
              SUPPORTED_AUDIO["samplerate"]["min"]} and {SUPPORTED_AUDIO["samplerate"]["max"]}')
        exit(3)
    else:
        parse_args['audio_samplerate'] = args.audio_samplerate

    if args.audio_bitdepth < SUPPORTED_AUDIO['bitdepth']['min'] or args.audio_bitdepth > SUPPORTED_AUDIO['bitdepth']['max']:
        print(f'Value: {args.audio_bitdepth} is out of bound should be between: {
              SUPPORTED_AUDIO["bitdepth"]["min"]} and {SUPPORTED_AUDIO["bitdepth"]["max"]}')
        exit(4)
    else:
        parse_args['bitdepth'] = args.audio_bitdepth

    if args.audio_channels < SUPPORTED_AUDIO['channels']['min'] or args.audio_channels > SUPPORTED_AUDIO['channels']['max']:
        print(f'Value: {args.audio_channels} is out of bound should be between: {
              SUPPORTED_AUDIO["channels"]["min"]} and {SUPPORTED_AUDIO["channels"]["max"]}')
        exit(5)
    else:
        parse_args['channels'] = args.audio_channels

    if args.codec_video.upper() not in SUPPORTED_VIDEO['non-transparend']:
        print(f'Not supported video codec: {
              args.codec_video.upper()}', file=sys.stderr)
        exit(6)
    else:
        parse_args['video_codec'] = args.codec_video

    resolution = args.video_resolution.lower().split('x')
    if len(resolution) != 2:
        print(f'video resolution is in the wrong format. Must be "heigth"x"width"', file=sys.stderr)
        exit(7)

    if not resolution[0].isdigit() or not resolution[1].isdigit():
        print(f'argument for resolution have a non digit in side it: {resolution}',
              file=sys.stderr)
        exit(8)

    parse_args['resolution'] = {'width': int(resolution[0]),
                                'heigth': int(resolution[1])}

    return parse_args
