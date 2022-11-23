suggest(S) :- write('Is your Screen lagging?: '),read(M), 
            write('Is your system failing to boot?: '),read(X),
            write('Do you face heating issues?: '),read(P),
            write('Is your Screen Blue?: '),read(D),
            comp(S,M,X,P,D).


comp('Battery Damage',M,X,P,D):- M = (yes), X = (yes) ,P= (yes), D=(no)!.
comp('Fan Damage',M,X,P,D):- ( M = (yes)),X = (no) ,(P= (yes)), D=(no)!.
comp('Display Damage',M,X,P,D):- ( M = (no)), X = (no) ,(P= (no)), D=(yes)!.
