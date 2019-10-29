% problem 1
-module(p001).
-export([compute/0,compute/1]).

compute(N) when N >= 0 ->
    if
        N == 0 -> 0; % base case
        (N rem 3 == 0) or (N rem 5 == 0) -> N + compute(N-1); % include N
        true -> compute(N-1) % exclude N
    end.

compute() ->
    io:fwrite("~w~n",[compute(999)]).
