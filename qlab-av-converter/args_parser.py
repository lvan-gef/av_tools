import argparse
import sys

from defaults import SUPPORTED_AUDIO


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

    return parse_args
