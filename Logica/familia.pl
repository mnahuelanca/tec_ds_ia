hombre(jorge).
hombre(roberto).
hombre(pedro).
hombre(diego).
hombre(vicente).
mujer(elena).
mujer(victoria).
mujer(angelica).
mujer(sofia).
mujer(carolina).
es_padre(jorge, roberto).
es_padre(jorge, victoria).
es_padre(roberto, pedro).
es_padre(roberto, sofia).
es_padre(diego, vicente).
es_padre(diego, carolina).
es_madre(elena, roberto).
es_madre(elena, victoria).
es_madre(angelica, pedro).
es_madre(angelica, sofia).
es_madre(victoria, vicente).
es_madre(victoria, carolina).
es_abuela(X, Y) :- mujer(X), es_madre(X, Z), es_madre(Z, Y).
es_abuela(X, Y) :- mujer(X), es_madre(X, Z), es_padre(Z, Y).
es_abuelo(X, Y) :- hombre(X), es_padre(X, Z), es_madre(Z, Y).
es_abuelo(X, Y) :- hombre(X), es_padre(X, Z), es_padre(Z, Y).
es_hermana(X, Y) :- mujer(X), es_madre(Z, X), es_madre(Z, Y).
es_hermana(X, Y) :- mujer(X), es_padre(Z, X), es_padre(Z, Y).
es_hermano(X, Y) :- hombre(X), es_madre(Z, X), es_madre(Z, Y).
es_hermano(X, Y) :- hombre(X), es_padre(Z, X), es_padre(Z, Y).
es_hijo(X, Y) :- hombre(X), es_padre(Y, X).
es_hijo(X, Y) :- hombre(X), es_madre(Y, X).
es_hija(X, Y) :- mujer(X), es_padre(Y, X).
es_hija(X, Y) :- mujer(X), es_madre(Y, X).
