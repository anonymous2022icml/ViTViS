import pdb
from collections import defaultdict


def generate():
    with open('failed2.row', 'w') as file:
        print('\def \styleb{0.08\\textwidth}', file=file)
        print('\\begin{figure*}[t]\centering\setlength\\tabcolsep{0pt}\\begin{tabularx}{\linewidth}{Y',
              ('Y' * (1 + 8)), '}', sep='', file=file)

        print('\\toprule &', end='', sep='', file=file)
        for f in range(8):
            print('& Feature ', f, end='', sep='', file=file)
        print('\\\\ \\midrule', file=file)

        for l in range(8, 12):
            print('\multirow{6}{*}{Layer', l, '}', file=file, sep='')
            for name in ['key', 'query', 'value']:
                print('& \\raisebox{', 2.5 if name != 'key' else 1.8, '\\totalheight}{', name, '}', file=file, sep='')
                for f in range(8):
                    print('& \includegraphics[width=\styleb]{figures/failed2/', name, '/', l, '_', f, '.jpg}',
                          sep='', file=file)
                print('\\\\ \\cmidrule{', 1 if name == 'value' else 2, '-10}', file=file, sep='')

        print('\end{tabularx} \caption{} \label{fig:zoom} \end{figure*}', file=file)
        print('', file=file)


if __name__ == '__main__':
    generate()
