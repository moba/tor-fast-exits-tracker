# tor-fast-exits-tracker

Track fast-exits as specified by Tor compass over time.

## Setup

    git clone git://git.torproject.org/compass.git
    touch compass/__init__.py

## Usage

    ./track-fast-exits.py --download # downloads current dataset from onionoo
    ./track-fast-exits.py # adds fast-exits to db

    ./print-fast-exits.py # prints dates with entries in db 
