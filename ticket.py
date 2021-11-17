import os, subprocess

with open("ticket.tex", "w+") as f:
    f.write('\\documentclass{article}\n')
    f.write('\\usepackage{chronosys}\n\n')
    f.write('\\begin{document}\n\n')

    # f.write('\\catcode`\\@=11\n\\def\\chron@selectmonth#1{\\ifcase#1\\or January\\or February\\or March\\or April\\or May\\or June\\or July\\or August\\or September\\or October\\or November\\or December\\fi}\n')
    f.write("\\startchronology\n")
    f.write("\\chronoevent{476}{Fall of the Roman empire}\n")
    f.write("\\chronoevent{1492}{Discovery of America}\n")
    f.write("\\chronoevent{1969}{first steps on the Moon}\n")
    f.write("\\stopchronology\n\n")


    f.write('\\end{document}\n')

x = os.system('texlive ticket.tex')
if x != 0:
    print('Exit-code not 0, check result!')
else:
    os.system('start ticket.pdf')