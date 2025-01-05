# Coq-модель програми

%% Тут вставляється текст картки %%

Синтаксично програми можна моделювати в термінах [The Coq Proof Assistant](https://coq.inria.fr/) у такий спосіб
```coq
Structure Program :=
{ datatype : Set
; algorithm : datatype -> option datatype
}.
```
Ця модель формально представляє *[[Data structure|структуру даних]]* компонентом `datatype`, а *[[Algorithm|алгоритм]]* - компонентом `algorithm`, який визначає правило, що ідентифікує умову припинення обчислення або спосіб перетворення даних (щодо контейнерного типу `option` дивись [тут](https://coq.inria.fr/doc/V8.20.0/stdlib/Coq.Init.Datatypes.html)).

Визначення семантики програми базується на відношенні *досяжності* одного стану даних з іншого за допомогою програми. Формально це відношення можна визначити так.
```coq
Inductive pass (p : Program) : datatype p -> datatype p -> Prop :=
| refl : forall x : datatype p, pass p x x
| cont : forall x x' y : datatype p,
	pass p x x' -> algorithm p x' = Some y -> pass p x y.

Notation "p : x ==> y" := (pass p x y) (at level 70).
```
Тепер визначити зміст фрази "`y` *є результатом обчислення програми* `p` *для входу* `x`" можна так 
```coq
Definition compute (p : Program) : datatype p -> datatype p -> Prop :=
  fun x y => forall x y, p : x ==> y /\ algorithm p y = None.

Notation "p : x ==>! y" := (compute p x y) (at level 70).
```
