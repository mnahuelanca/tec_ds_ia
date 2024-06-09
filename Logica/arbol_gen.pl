% Base de conocimiento sobre un árbol genealógico

% Hechos
padre(juan, maria).
padre(juan, jose).
padre(pedro, juan).
padre(manuel, ana).

madre(ana, maria).
madre(ana, jose).
madre(carmen, juan).
madre(rosa, ana).

% Género
hombre(juan).
hombre(jose).
hombre(pedro).
hombre(manuel).

mujer(maria).
mujer(ana).
mujer(carmen).
mujer(rosa).

% Regla: X es hermano de Y si tienen el mismo padre y la misma madre
hermano(X, Y) :-
    padre(P, X), padre(P, Y),
    madre(M, X), madre(M, Y),
    X \= Y.

% Regla: X es abuelo de Y si X es padre de Z y Z es padre o madre de Y
abuelo(X, Y) :-
    padre(X, Z), (padre(Z, Y) ; madre(Z, Y)).

% Regla con variable anónima: X tiene algún hijo si existe 
% un Y tal que X es padre de Y o madre de Y
tiene_hijos(X) :-
    (padre(X, _) ; madre(X, _)).

