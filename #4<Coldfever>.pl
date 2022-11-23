check:-
checkfor(Disease),
write('I believe you have '),
write(Disease),
nl,
undo.

checkfor(cold):- cold.
checkfor(fever):- fever.

cold:-
checkSymptom(chills),
checkSymptom(sore_throat),
checkSymptom(cough),
nl.

fever:-
checkSymptom(headache),
checkSymptom(chills),
checkSymptom(fatigue),
nl.

askQuestion(Question):-
write('Do you have the Symptom '),
write(Question),
write('?'),
read(Reply),
nl,
((Reply == yes ; Reply == y) 
-> 
assert(yes(Question));
assert(no(Question)),fail).

:- dynamic yes/1,no/1.

checkSymptom(S) :-
(yes(S) -> true;
(no(S) -> fail;

askQuestion(S))).

undo :- retract(yes(_)),fail.
undo :- retract(no(_)),fail.
undo.
