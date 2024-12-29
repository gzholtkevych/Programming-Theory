# Що таке програма?

Відома формула "Програма = алгоритм + структура даних", що явно сформульована [**Ніклаусом Віртом**](https://uk.wikipedia.org/wiki/%D0%9D%D1%96%D0%BA%D0%BB%D0%B0%D1%83%D1%81_%D0%92%D1%96%D1%80%D1%82),  слугує фундаментальною концепцією в теорії програмування. Вона виокремлює два ключових компоненти обчислення
- [[Algorithm|алгоритм]] та
- [[Data structure|структуру даних]],
які взаємодіють в процесі виконання програми.

В процесі обчислення
- структура даних визначає множину можливих станів даних, а
- алгоритм - правила перетворення цих даних.

Синтаксично програми можна моделювати в термінах [The Coq Proof Assistant](https://coq.inria.fr/) у такий спосіб
```coq
Structure Program :=
{ datatype : Set
; algorithm : datatype -> option datatype
}.
```
Вона формалізує представляє структуру даних компонентом `datatype`, а алгоритм - компонентом `algorithm`, який визначає правило, що ідентифікує умову припинення обчислення або спосіб перетворення даних (більш детально дивись [визначення контейнерного типу `option`](https://coq.inria.fr/doc/V8.20.0/stdlib/Coq.Init.Datatypes.html)).

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
