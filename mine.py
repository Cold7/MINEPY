import numpy as np
from minepy import MINE
import argparse   # arguments parser


def print_stats(mine):
    print  mine.mic(), mine.mas(), mine.mev()


############# main ##################
parser = argparse.ArgumentParser()
parser.add_argument('-s1','--serie1', nargs='+', help='<Required> first serie of numbers (usage: -s1 1 43 25 0)', required=True)
parser.add_argument('-s2','--serie2', nargs='+', help='<Required> second serie of numbers (usage: -s1 1 43 25 0)', required=True)
parser.add_argument("-a","--alpha",help="float (0,1.0] the exponent in B(n) n^alpha (default 0.6)", default="0.6")
parser.add_argument("-c","--clumps",help="float (> 0) determines how many more clumps there will be than columns in every partition. Default value is 15, meaning that when trying to draw x grid lines on the x-axis, the algorithm will start with at most 15*x clumps (default 15)", default="15")
args = parser.parse_args()

x = args.serie1
y =  args.serie2
mine = MINE(alpha=float(args.alpha), c=float(args.clumps))
mine.compute_score(x, y)

print_stats(mine)

