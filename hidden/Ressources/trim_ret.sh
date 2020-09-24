#!/bin/bash
cat ret.txt | awk '!/Non/ && !/Demande/ && !/Tu/ && !/Toujours/'
