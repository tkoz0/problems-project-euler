% problem 2
-module(p002).
-export([compute/0,compute/4]).

compute(A,B,S,Limit) ->
    C = A+B, % next fibonacci
    if
        C > Limit -> S; % end recursion
        C rem 2 == 0 -> compute(B,C,S+C,Limit); % even, add this
        true -> compute(B,C,S,Limit) % else odd, dont add
    end.

compute() ->
    io:fwrite("~w~n",[compute(0,1,0,4000000)]).
