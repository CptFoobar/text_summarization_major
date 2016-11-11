#!/bin/sh

FILES=data/articles/*
for f in $FILES
do
    RES=$(tr -cd '[:print:]' < $f)
    echo $RES > $f
done
cd ..
