% Genders
male(john). male(charles). male(david). male(peter). male(james).
female(mary). female(ann). female(lisa). female(sarah). female(emma).

% parent(Parent, Child)
% Grandparents to Parents & Uncles/Aunts
parent(john, charles).
parent(john, ann).
parent(john, david).
parent(mary, charles).
parent(mary, ann).
parent(mary, david).

% Parents to Children (Your core family)
parent(charles, peter).
parent(lisa, peter).
parent(charles, sarah).
parent(lisa, sarah).

% Uncle/Aunt (David) to Cousins
parent(david, james).
parent(emma, james).


% Father & Mother
father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).

% Child
child(X, Y) :- parent(Y, X).

% Siblings
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

% Grandparent & Grandchild
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
grandchild(X, Y) :- grandparent(Y, X).

% Uncle or Aunt (Sibling of a parent)
uncle_or_aunt(X, Y) :- parent(Z, Y), sibling(X, Z).

% Specific Uncle / Aunt
uncle(X, Y) :- uncle_or_aunt(X, Y), male(X).
aunt(X, Y) :- uncle_or_aunt(X, Y), female(X).

% Cousins (Children of siblings)
cousin(X, Y) :- parent(A, X), parent(B, Y), sibling(A, B).