# Python script which reads octave scripts and adapt them to generate and save each plot

## Description

Read a bunch of octave scripts and save all the plots generated in those scripts into files.

**Important:** This script is for fixing a very specific problem. Adapt to your needs.

## Requirements

* python 3
* octave
* epstools

## Basic usage

Run in a terminal the script:

    $ python3 octave-plot-generator.py /path/to/octave-scripts/folder/ /destination/folder/

## Detailed usage

    $ python octave-plot-generator.py --help
    usage: octave-plot-generator.py [-h] [-v VERBOSITY] [-f FORMAT] [-o OCTAVE]
                                    [--noexec]
                                    folder destfolder

    positional arguments:
      folder
      destfolder

    optional arguments:
      -h, --help            show this help message and exit
      -v VERBOSITY, --verbosity VERBOSITY
                            increase output verbosity
      -f FORMAT, --format FORMAT
                            output plot format
      -o OCTAVE, --octave OCTAVE
                            octave binary path
      --noexec              do no execute octave. only adapt scripts

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
