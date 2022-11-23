% is used to add comments in code in prolog language
suggest(S) :- write('What is your Gender?: '),read(P),
            write('What are Your Hobbies?: '),read(M), 
            write('What is your Age?: '),read(X),
            write('What is your number of contacts?: '),read(C),
            write('*Note: if there is no match with your preferences then false is printed*'),
            person(S,M,X,P,C).

%marathi
person('inventor',M,X,P,C):- (M = (experimenting) ; M = (reading) ),X >= 15,(P= (male) ; P=(female)),C=<5,!.
person('challenger',M,X,P,C):- (M = (sports) ; M = (reading) ),X >= 18,(P= (male) ; P=(female)),C >=7,!.
person('healer',M,X,P,C):- (M = (music) ; M = (Companionship) ),X >= 20,(P=(female)),C >=5,!.
person('king',M,X,P,C):- (M = (sleeping) ; M = (consumingContent) ),X >= 25,(P= (male)),C >=10,!.


%! is called cut and is used to reduce backtracking
