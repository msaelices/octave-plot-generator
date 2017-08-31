# Python script which reads octave scripts and adapt them to generate and save each plot

## Description

Read a bunch of octave scripts and save all the plots generated in those scripts into files.

**Important:** This script is for fixing a very specific problem. Adapt to your needs.

## Requirements

* python 3
* octave
* epstools

## Usage

Run in a terminal the script:

    $ python3 octave-plot-generator.py --format=pdf /path/to/octave-scripts/folder/ /destination/folder/

For more detailed help:

    $ python3 octave-plot-generator.py --help

## Example

    $ python3 octave-plot-generator.py --verbosity 2 /tmp/folder-with-octave-scripts/ /tmp/plots-folder/

    "/tmp/plots-folder" directory does not exist. Creating it...
    Generating octave plots from "/tmp/folder-with-octave-scripts/" folder...
    Entering on "/tmp/folder-with-octave-scripts/" directory...
    Entering on "/tmp/folder-with-octave-scripts" directory...
    Entering on "/tmp/folder-with-octave-scripts/Reports" directory...
        Processing "report-2015-09-25-16-00-19.m" file
        Saved adapted script into "/tmp/plots-folder/Reports/report-2015-09-25-16-00-19.m"
        Executed "report-2015-09-25-16-00-19.m" script. Plots generated in "/tmp/plots-folder/Reports/"
        Processing "report-2015-09-25-15-59-59.m" file
        Saved adapted script into "/tmp/plots-folder/Reports/report-2015-09-25-15-59-59.m"
        Executed "report-2015-09-25-15-59-59.m" script. Plots generated in "/tmp/plots-folder/Reports/"
    ...
