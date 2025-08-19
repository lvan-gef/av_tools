def parse_probe(streams: list[str], config: dict) -> dict['str', bool]:
    to_convert = {'audio': False, 'video': False, 'pic': False}

    video_streams = []
    audio_streams = []
    pictures_stream = []

    for stream in streams:
        if 'video' in stream:
            video_streams.append(stream)
        elif 'audio' in stream:
            audio_streams.append(stream)
        else:
            pictures_stream.append(stream)

    for video_stream in video_streams:
        for line in video_stream.split('\n'):
            if 'codec_tag_string' in line:
                codec = line.split('=')[1].upper()
                if codec != config['video_codec']:
                    to_convert['video'] = True
                    break
            elif 'codec_width' in line:
                width = line.split('=')[1]
                if width != config['resolution']['width']:
                    to_convert['video'] = True
                    break
            elif 'codec_height' in line:
                height = line.split('=')[1]
                if height != config['resolution']['height']:
                    to_convert['video'] = True
                    break

    for audio_stream in audio_streams:
        pass

    for picture_stream in pictures_stream:
        pass

    return to_convert
