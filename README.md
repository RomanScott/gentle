# Gentle
**Robust yet lenient forced-aligner built on Kaldi. A tool for aligning speech with text.**

Modified by Roman Scott for the Nofanity application.

## Getting Started

Download the source code, install the dependencies, and run ```./install.sh``` and then ```pyinstaller gentle.spec```. Then, in the ```dist``` folder generated run ```./gentle``` to start the server. This version of Gentle works on Linux.

## Using Gentle

By default, the aligner listens at http://localhost:8765. That page has a graphical interface for transcribing audio, viewing results, and downloading data.

There is also a REST API so you can use Gentle in your programs. Here's an example of how to use the API with CURL:

```bash
curl -F "audio=@audio.mp3" -F "transcript=@words.txt" "http://localhost:8765/transcriptions?async=false"
```
