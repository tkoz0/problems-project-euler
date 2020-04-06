
/* delete all */
delete_all([],D,[]).
delete_all([H|T],D,[H|Result]) :- H \== D, delete_all(T,D,Result).
delete_all([H|T],D,Result) :- delete_all(T,D,Result).

/* replace all */
replace_all([],Old,New,[]).
replace_all([H|T],Old,New,[New|Result]) :- H == Old, replace_all(T,Old,New,Result).
replace_all([H|T],Old,New,[H|Result]) :- replace_all(T,Old,New,Result).

find3(3,L).
find3(X,Limit) :- X @=< Limit, Y is X+1, find3(Y,Limit).

:- use_module(library(clpfd)).

digit(D) :- between(0,9,D).
pairAdd10(D1,D2) :- digit(D1), digit(D2), D1 + D2 =:= 10.
allPairs(L) :- findall(p(D1,D2),pairAdd10(D1,D2),L).

palindrome(S) :-
    digit(D1), digit(D2), digit(D3), digit(D4),
    S is (10*D1+D2)*(10*D3+D4),
    S >= 1000,
    mod(div(S,1000),10) =:= mod(S,10),
    mod(div(S,100),10) =:= mod(div(S,10),10).
allPalindromes(S,L) :- findall(P,palindrome(P),S), length(S,L).
