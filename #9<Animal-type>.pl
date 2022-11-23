% is used to add comments in code in prolog language
suggest(S) :- write('is the animal domestic or wild?: '),read(P),
            write('What is the skin colour?: '),read(M), 
            write('Does it have stripes?: '),read(X),
            write('Are the ears big?: '),read(Y),
            write('*Note: if there is no match with your preferences then false is printed*'),
            animal(S,M,X,P,Y).


animal('cat',M,X,P,Y):- ( M = (white) ; M= (black) ), X = (no) ,(P= (domestic)), Y=(no) ,!.
animal('dog',M,X,P,Y):- ( M = (white) ; M = (brown) ; M= (black) ),X = (no) ,(P= (domestic)), Y=(yes) ,!.

animal('lion',M,X,P,Y):- ( M = (golden) ; M= (yellow) ), X = (no) ,(P= (wild)), Y=(yes) ,!.
animal('tiger',M,X,P,Y):- ( M = (white) ; M= (yellow) ), X = (yes) ,(P= (wild)), Y=(yes) ,!.
animal('zebra',M,X,P,Y):- ( M = (white) ), X = (yes) ,(P= (wild)), Y=(no) ,!.


%! is called cut and is used to reduce backtracking
