%B: book
%A: age
%I: interest
%L: language
%Need to extend for more examples

suggest :- 
write('Age? '),
read(A),
write('Interest? '),
read(I),
write('language? '),
read(L), 
book(B,A,I,L),
write(B).

book('b1', A,I,L):- A = 15, I=ha, L=eng,!.
book('b2', A,I,L):- A = 15, I=ha, L=eng,!.

book('b3', A,I,L):- A = 25, I=sad, L=hin,!.
book('b4', A,I,L):- A = 25, I=sad, L=hin,!.
