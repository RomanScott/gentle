import os
import subprocess
import sys
import tempfile

from contextlib import contextmanager

from util.paths import get_binary

BINARY_PATH = os.path.join("ffmpeg", "ffmpeg.exe" if os.name == "nt" else "ffmpeg")
FFMPEG = get_binary(BINARY_PATH)

def resample(infile, outfile):
    if not os.path.isfile(infile):
        raise IOError("Not a file: %s" % infile)

    '''
    Use FFMPEG to convert a media file to a wav file sampled at 8K
    '''
    return subprocess.call([FFMPEG,
                            '-loglevel', 'panic',
                            '-y',
                            '-i', infile,
                            '-ac', '1', '-ar', '8000',
                            '-acodec', 'pcm_s16le',
                            outfile], cwd=os.path.dirname(sys.executable))

@contextmanager
def resampled(infile):
    with tempfile.NamedTemporaryFile(suffix='.wav') as fp:
        if resample(infile, fp.name) != 0:
            raise RuntimeError("Unable to resample/encode '%s'" % infile)
        yield fp.name
