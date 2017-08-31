#! /usr/bin/env python3

import argparse
import logging
import os
import subprocess
from os import path

# command line args config
parser = argparse.ArgumentParser()
parser.add_argument('folder')
parser.add_argument('destfolder')
parser.add_argument(
    '-v', '--verbosity', help='increase output verbosity', type=int, default=1)
parser.add_argument(
    '-f', '--format', help='output plot format', type=str, default='pdf')
parser.add_argument(
    '-o', '--octave', help='octave binary path', type=str, default='octave')
parser.add_argument(
    '--noexec', help='do no execute octave. only adapt scripts', action="store_true")

# parsed command line args
args = parser.parse_args()

# logging config
logging.basicConfig(
    format='%(message)s',
    level=logging.DEBUG if args.verbosity >= 2 else logging.INFO,
)


def _saveas_line(script_name, plot_count):
    global args
    return "saveas(f, '%(name)s-f%(count)d.%(fmt)s', '%(fmt)s');" % {
        'name': script_name,
        'count': plot_count,
        'fmt': args.format,
    }


def refactor_script(basedir, file_name):
    """
    Adapt an already existing Octave script to save all its plot figures to files
    """
    global args

    script_name, ext = path.splitext(file_name)
    script_file = open(path.join(basedir, file_name))
    script_lines = script_file.readlines()
    script_file.close()

    adapted_script = []

    plot_count = 0
    for line in script_lines:
        line = line.strip()
        # new plot
        if line == 'figure();':
            line = "f = figure('visible', 'off');"
            if plot_count != 0:
                # line which save the plot into a file
                adapted_script.append(_saveas_line(script_name, plot_count))
            plot_count += 1
        adapted_script.append(line)

    # ensure we save last plot
    adapted_script.append(_saveas_line(script_name, plot_count))

    return '\n'.join(adapted_script)


def main():
    """
    Main function
    """
    global args
    folder = args.folder
    destfolder = args.destfolder
    noexec = args.noexec
    octave = args.octave

    if folder == destfolder:
        logging.error('folder cannot be the same as the destfolder')
        os.exit(1)

    if not path.exists(destfolder):
        logging.debug('"%s" directory does not exist. Creating it...' % destfolder)
        os.makedirs(destfolder)

    logging.info('Generating octave plots from "%s" folder...' % folder)
    for root, dirs, files in os.walk(folder):
        parent_dir = root[len(folder):]
        parent_dir = parent_dir[1:] if parent_dir.startswith(os.sep) else parent_dir
        logging.debug('Entering on "%s" directory...', root)

        dest_parent_dir = path.join(destfolder, parent_dir)
        if not path.exists(dest_parent_dir):
            os.makedirs(dest_parent_dir)

        for file_name in files:
            name, ext = path.splitext(file_name)
            if ext != '.m':
                continue
            logging.debug('\tProcessing "%s" file' % file_name)
            adapted_script = refactor_script(root, file_name)
            # save adapted script
            adapted_script_path = path.join(dest_parent_dir, file_name)
            adapted_script_file = open(adapted_script_path, 'w')
            adapted_script_file.write(adapted_script)
            adapted_script_file.close()
            logging.debug('Saved adapted script into "%s"' % adapted_script_path)

            if not noexec:
                octave_cmd = '%s "%s"' % (octave, file_name)
                subprocess.run(octave_cmd, cwd=dest_parent_dir, shell=True, check=True)
                logging.debug(
                    'Executed "%(name)s" script. Plots generated in "%(dir)s"' % {
                        'name': file_name,
                        'dir': dest_parent_dir,
                    })

    logging.info('Done.')

if __name__ == '__main__':
    main()
