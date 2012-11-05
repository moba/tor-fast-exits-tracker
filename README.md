# tor-fast-exits-tracker

Track fast-exits as specified by Tor compass over time.

## Setup

    git clone git://git.torproject.org/compass.git
    touch compass/__init__.py

## Usage

    ./track-fast-exits.py --download
    ./track-fast-exits.py # adds current dataset to db

    ./print-fast-exits.py 
