% Facts

male(ravi).
male(kumar).
male(arun).
male(suresh).

female(latha).
female(priya).
female(anitha).
female(meena).

% Parent relationships

parent(ravi, kumar).
parent(latha, kumar).

parent(kumar, arun).
parent(priya, arun).

parent(kumar, anitha).
parent(priya, anitha).

parent(arun, meena).

% Rules

father(X, Y) :-
    male(X),
    parent(X, Y).

mother(X, Y) :-
    female(X),
    parent(X, Y).

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

grandfather(X, Y) :-
    male(X),
    grandparent(X, Y).

grandmother(X, Y) :-
    female(X),
    grandparent(X, Y).

sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.
