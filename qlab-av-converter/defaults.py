SUPPORTED_VIDEO = {
    'non-transparend': ['ProRes 422 Proxy', 'Hap Standard',
                        'ProRes 422 LT', 'Hap Q', 'Photo-JPEG'],
    'non-transparend-q': ['ProRes 422', 'ProRes 422 HQ'],
    'transparend': ['ProRes 4444', 'Hap Alpha'],
    'transparend-q': ['ProRes 4444 XQ'],
    'containers': ['MOV', 'MP4']
}

SUPPORTED_AUDIO = {'codec': ['AIFF', 'WAV', 'CAF', 'AAC'],
                   'channels': {'min': 1, 'max': 24},
                   'samplerate': {'min': 8, 'max': 192},
                   'bitdepth': {'min': 8, 'max': 32}
                   }

SUPPORTED_PIC = {'codec': ['PNG', 'JPG']}
