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
Модель формально представляє структуру даних компонентом `datatype`, а алгоритм - компонентом `algorithm`, який визначає як умову припинення обчислення так і спосіб перетворення даних.
>[!remark]- Remark
Контейнерний тип `option` визначений [тут](https://coq.inria.fr/doc/V8.20.0/stdlib/Coq.Init.Datatypes.html).

Визначення семантики програми базується на відношенні *досяжності* одного стану даних з іншого за допомогою програми. Формально це відношення можна визначити так.
```coq
Inductive reach (p : Program) : datatype p -> datatype p -> Prop :=
| reach_refl : forall x : datatype p, reach p x x
| reach_step : forall x y : datatype p, algorithm p x = Some y -> reach p x y
| reach_trans : forall x y z : datatype p,
    reach p x y -> reach p y z -> reach p x z.

Notation "p [ x ==> y ] " := (reach p x y) (at level 70).
```
Зміст фрази "`y` *є результатом обчислення програми* `p` *для входу* `x`" визначається так 
```coq
Definition compute (p : Program) : datatype p -> datatype p -> Prop :=
  fun x y => forall x y, p[x ==> y] /\ algorithm p y = None.

Notation "p[x ==>! y]" := (compute p x y) (at level 70).
```
Якщо тепер `p` є програмою, а `R` є предикатом, що пов'язує вхідні та вихідні дані `p`, тоді твердження "`p` задовольняє вимогам `R`" треба розуміти як `p |= R` за наступного визначення
```coq
Definition satisfy
  (p : Program)
  (R : datatype p -> datatype p -> Prop) : Prop :=
	forall x y : datatype p, p[x ==>! y] -> R x y.

Notation "p |= R" := (satisfy p R) (at level 70).
```
