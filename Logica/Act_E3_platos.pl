% Base de conocimiento sobre ingredientes y platos de comida

% Hechos sobre ingredientes
ingrediente(papa).
ingrediente(queso).

% Propiedades de los ingredientes
es_vegetal(papa).
es_lacteo(queso).

% Platos y sus ingredientes
plato(papas_fritas).
plato(papa_al_horno).
plato(gratinado_de_papas).

contiene(papas_fritas, papa).
contiene(papa_al_horno, papa).
contiene(gratinado_de_papas, papa).
contiene(gratinado_de_papas, queso).

% Relaciones
tiene_lacteo_presente(Plato) :-
    contiene(Plato, Ingrediente),
    es_lacteo(Ingrediente).


