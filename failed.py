import pdb
from collections import defaultdict


def generate():
    with open('failed.py.row', 'w') as file:
        print('\def \styleb{0.1\\textwidth}', file=file)
        print('\\begin{figure*}[t]\centering\setlength\\tabcolsep{0pt}\\begin{tabularx}{\linewidth}{',
              ('Y' * (2 * 4 + 1)), '}', sep='', file=file)
        for f in range(4):
            print('& \\multicolumn{2}{c}{Feature ', f, end='} ', sep='', file=file)
        print('\\\\', file=file)

        for l in range(12):
            print('\\raisebox{2.5\\totalheight}{Layer {', l, '} }', file=file, end='')
            for f in range(4):
                print('& \includegraphics[width=\styleb]{figures/failed/vis/', l, '_', f, '.jpg}', sep='', file=file)
                print('& \includegraphics[width=\styleb]{figures/failed/eval/', l, '_', f, '.jpg}', sep='', file=file)
            print('\\\\', file=file)

        print('\end{tabularx} \caption{} \label{fig:zoom} \end{figure*}', file=file)
        print('', file=file)


if __name__ == '__main__':
    generate()
