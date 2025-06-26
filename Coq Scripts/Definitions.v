Class aDecSet (X : Set) : Set :=
  eq_dec : forall x y : X, {x = y} + {x <> y}.


Structure Program :=
{ datatype : Set
; datatype_aDecSet : aDecSet datatype
; algorithm : datatype -> option datatype
}.


Inductive pass (p : Program) : datatype p -> datatype p -> Prop :=
| step : forall x y : datatype p, algorithm p x = Some y -> pass p x y
| trans : forall x y z : datatype p,
	  pass p x y -> pass p y z -> pass p x z.

Notation "p : x ==> y" := (pass p x y) (at level 70).


Definition compute (p : Program) : datatype p -> datatype p -> Prop :=
  fun x y => p : x ==> y /\ algorithm p y = None.

Notation "p : x ==>! y" := (compute p x y) (at level 70).


Section nsteps.
Variable p : Program.
Variables x y : datatype p.
Hypothesis H : p : x ==> y.

Fixpoint nsteps : nat :=  



Lemma Church_Rosser :
  forall p x y1 y2, p : x ==> y1 -> p : x ==> y2 ->
    exists z, p : y1 ==> z /\ p : y2 ==> z.
Proof.
  intros.

Lemma func_compute : forall (p : Program) (x y z : datatype p),
  p : x ==>! y -> p : x ==>! z -> y = z.
Proof.
  intros *. unfold "_ : _ ==>! _". intros Hy Hz.
  destruct Hy as (Hy, Hy'). destruct Hz as (Hz, Hz').
  destruct Hy as [| x y' y Hxy' Hy'y].
  - 
  induction Hz as [x z Hxz | x z' z Hxz' Hz'z].
  - rewrite H in Hxz. now injection Hxz.
  - apply IHHz1. 2: { trivial. }
     