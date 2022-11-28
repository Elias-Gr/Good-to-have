import numpy as np

Vektor_U = np.round(np.random.rand(10), 4)   # Array of data in column 1
Vektor_I = np.round(np.random.rand(10), 4)
Vektor_P = np.round(Vektor_U * Vektor_I, 4)

quantities = ['U', 'I', 'P']  # strings of physical quantities
units = ['V', 'A', 'W']
explanation = ['Voltage drop at resistor', 'Current flow through the resistor', 'Power used by the resistor']
Data_for_table = [Vektor_U, Vektor_I, Vektor_P]


def listofemptystrings(n):
    S = [str('')]
    for i in range(n):
        S.append('')
    return S


def writinglines(lines, f):
    for line in lines:
        f.write(line)
        f.write('\n')


def LaTeX_tab(quantities, Data, Name):    # use this function to create a .txt file with the table
    n_columns = len(explanation)
    n_rows = len(Data[0])
    Lines_header = listofemptystrings(n_columns)

    Lines_start = ['\\begin{table}', '\caption{}', '\label{}', '\centering', '\\begin{minipage}{0.7\linewidth}',
                   '\\begin{tabular}{cl}']

    for n in range(n_columns):
        Lines_header[n] = '$' + quantities[n] + '$&…' + explanation[n] + '\\\\'

    Spalten = ''
    for i in range(len(explanation)):
        Spalten = Spalten + '|c'

    Lines_middle = ['\end{tabular}', '\\begin{tabular}{' + Spalten + '|}', '\hline']
    Lines_bulk = listofemptystrings(int(2 * n_rows))
    Line_columnheader = '$' + quantities[0] + '$\,/\,' + units[0]

    for n in range(n_columns - 1):
        Line_columnheader = Line_columnheader + '&$' + quantities[int(n + 1)] + '$\,/\,' + units[
            int((n + 1))]
    Line_columnheader = Line_columnheader + '\\\\'

    for n in range(n_rows):
        Lines_bulk[2 * n] = '$' + str(Data[0][n]) + '$'
        for i in range(n_columns - 1):
            Lines_bulk[int(2 * n)] = Lines_bulk[int(2 * n)] + '&$' + str(Data[i + 1][n]) + '$'
        Lines_bulk[int(2 * n)] = Lines_bulk[int(2 * n)] + '\\\\'
        Lines_bulk[int(2 * n + 1)] = '\hline'

    Lines_end = ['\end{tabular}', '\end{minipage}', '\end{table}']

    with open(Name + '.txt', 'w') as f:
        writinglines(Lines_start, f)
        writinglines(Lines_header, f)
        writinglines(Lines_middle, f)
        f.write(Line_columnheader)
        f.write('\n')
        writinglines(['\hline', '\hline'], f)
        writinglines(Lines_bulk, f)
        writinglines(Lines_end, f)


LaTeX_tab(quantities, Data_for_table, 'LaTeX_Table_from_Python')
