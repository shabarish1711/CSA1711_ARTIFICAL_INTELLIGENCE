% Sum of N numbers

sum_n(4, Sum).

sum_n(N, Sum) :-
    N > 0,
    write('Enter number: '),
    read(X),
    N1 is N - 1,
    sum_n(N1, S),
    Sum is X + S.
