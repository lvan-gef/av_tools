SUPPORTED_VIDEO = {
    'non-transparend': ['PRORES 422 PROXY', 'HAP STANDARD',
                        'PRORES 422 LT', 'HAP Q', 'PHOTO-JPEG'],
    'non-transparend-q': ['PRORES 422', 'PRORES 422 HQ'],
    'transparend': ['PRORES 4444', 'HAP ALPHA'],
    'transparend-q': ['PRORES 4444 XQ'],
    'containers': ['MOV', 'MP4']
}

SUPPORTED_AUDIO = {'codec': ['AIFF', 'WAV', 'CAF', 'AAC'],
                   'channels': {'min': 1, 'max': 24},
                   'samplerate': {'min': 8, 'max': 192},
                   'bitdepth': {'min': 8, 'max': 32}
                   }

SUPPORTED_PIC = {'codec': ['PNG', 'JPG']}
