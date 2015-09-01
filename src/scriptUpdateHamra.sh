#!/bin/bash

rm psnTopology.py

cd Hamra
git pull
cd ..

cd pyretic
rm hamraGTR.py
rm hamraGTR.pyc
rm hamraConfig.py
rm hamraConfig.pyc
cd ..


cp ~/Hamra/src/hamraGTR.py ~/pyretic/hamraGTR.py
cp ~/Hamra/src/hamraConfig.py ~/pyretic/hamraConfig.py
cp ~/Hamra/src/psnTopology.py psnTopology.py



