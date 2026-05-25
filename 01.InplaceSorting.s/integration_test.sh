#!/bin/bash

status=true

for size in 0 1 10 100 1000
do
    echo "test size: $size"

    python3 -O ./sorting_demo.py $size
done

$status
