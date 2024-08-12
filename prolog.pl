%main code that calls helper to implement function
reverse_list :-
    read(Input),
    reverse_list(Input, Result),
    write(Result).

%first case is the base case to check if the list is empty, otherwise it reverses the list starting from the tail
reverse_list([], []).
reverse_list([Head|Tail], Reversed) :-
    reverse_list(Tail, ReversedTail),
    append(ReversedTail, [Head], Reversed).

