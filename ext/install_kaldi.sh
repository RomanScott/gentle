#!/bin/bash

# Prepare Kaldi
cd kaldi/tools
make clean -j4
make atlas openfst OPENFST_VERSION=1.4.1 -j4
cd ../src
make clean -j4
./configure --static --static-math=yes --static-fst=yes --use-cuda=no
make depend -j4
cd ../../