# Gentle
**Robust yet lenient forced-aligner built on Kaldi. A tool for aligning speech with text.**

Modified by Roman Scott for the Nofanity application.

## Getting Started
**Mac and Linux**

Download the source code, install the dependencies (place an ffmpeg binary inside ```ext```), and run ```./install.sh```. Then, inside the ```ext``` folder, rename k3 and m3 to gentleK3 and gentleM3, and run ```pyinstaller gentle.spec```. Then, in the ```dist``` folder generated, run ```./gentle``` to start the server.

**Windows**

Run ```git submodule init``` and ``git submodule update``. Download an ffmpeg binary and place it inside the ```ext``` folder. Run the ```install_models.sh``` script as well.

Go inside the Kaldi folder and make the following changes in the code as shown in the commits: [here](https://github.com/kaldi-asr/kaldi/commit/4507183f30e5e517ecbd577cd3b0e9d3e0c300cd), [here](https://github.com/kaldi-asr/kaldi/commit/67cabd02622fd7f72b896bfe5705f55c790555bc), [here](https://github.com/kaldi-asr/kaldi/commit/21cfe99c5e08a35eb410ce3cc28d150fd4cb7505), and [here](https://github.com/kaldi-asr/kaldi/commit/c747ed5d51687003f995f859b449cb64dc0fc0c7).

Then go inside ```kaldi/src``` and create a folder called ```gentle```, and copy-paste the Makefile, k3-win.cc, and m3.cc from the ```ext``` folder into the new folder.

Go back to ```kaldi/src``` and to the parent Makefile: add the word gentle at the end of the line ```SUBDIRS = ``` and at the end of the line after "The tools depend on all the libraries".

After this, follow the [compilation instructions for Kaldi on Windows](https://github.com/kaldi-asr/kaldi/blob/21cfe99c5e08a35eb410ce3cc28d150fd4cb7505/windows/INSTALL.md). **NOTE:** Set Runtime Options to Multithreaded (/MT) instead of Multithreaded DLL (/MD)

Grab your k3.exe and m3.exe files from the built solution, rename them to gentleK3.exe and gentleM3.exe, and move them into ```ext```. Then run ```pyinstaller gentle.spec``` and, in the ```dist``` folder generated, run ```gentle.exe``` to start the server.

## Using Gentle

By default, the aligner listens at http://localhost:8765. That page has a graphical interface for transcribing audio, viewing results, and downloading data.

There is also a REST API so you can use Gentle in your programs. Here's an example of how to use the API with CURL:

```bash
curl -F "audio=@audio.mp3" -F "transcript=@words.txt" "http://localhost:8765/transcriptions?async=false"
```
