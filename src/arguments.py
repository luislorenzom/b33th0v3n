import argparse

from src.constants import VERSION

parser = argparse.ArgumentParser(prog='b3th0v33n', description='music file analyzer')

parser.add_argument('-f', action='store', dest='files_songs', help='input the files to analyze from csv, dataset must have song as columna name')
parser.add_argument('-d', action='store', dest='music_folder', help='input the files to analyze from their folder')
parser.add_argument('-o', action='store', dest='output', help='input the files to analyze from csv')
parser.add_argument('-g', action='store_true', default=False, dest='get_datasets_switch', help='get required dataset to refactor recommendator')
parser.add_argument('-v', '--version', action='version', version='%(prog)s {}'.format(VERSION))

args = parser.parse_args()
