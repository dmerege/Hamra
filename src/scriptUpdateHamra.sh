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
rm psnTopology.py
rm psnTopology.pyc
cd ..


cp ~/Hamra/hamraGTR.py ~/pyretic/hamraGTR.py
cp ~/Hamra/hamraConfig.py ~/pyretic/hamraConfig.py
cp ~/Hamra/psnTopology.py psnTopology.py



