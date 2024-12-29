Structure Program :=
{ datatype : Set
; algorithm : datatype -> option datatype
}.


Inductive pass (p : Program) : datatype p -> datatype p -> Prop :=
| refl : forall x : datatype p, pass p x x
| cont : forall x x' y : datatype p,
	pass p x x' -> algorithm p x' = Some y -> pass p x y.

Notation "p : x ==> y" := (pass p x y) (at level 70).


Definition compute (p : Program) : datatype p -> datatype p -> Prop :=
  fun x y => forall x y, p : x ==> y /\ algorithm p y = None.

Notation "p : x ==>! y" := (compute p x y) (at level 70).
 