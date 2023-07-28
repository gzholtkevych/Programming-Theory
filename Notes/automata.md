# Mealy and Moore Automata

>**Definition** (of a state machine).
>A ***state machine*** is a triple $(Q,\Sigma,T)$ where
>- $Q$ is a set whose elements are called ***states***;
>- $\Sigma$ is a finite alphabet called the ***input alphabet***;
>- $T:Q\times\Sigma\to Q$ called the ***transition function***.

>**Definition** (of a Mealy automaton).
>A ***Mealy automaton*** is a quintuple $(Q,\Sigma,\Lambda,T,G)$ where
>- $(Q,\Sigma,T)$ is a state machine;
>- $\Lambda$ is a finite alphabet called the ***output alphabet***;
>- $G:Q\times\Sigma\to\Lambda$ called the ***output function***.

>**Definition** (of a Moore automaton).
>A ***Moore automaton*** is a quintuple $(Q,\Sigma,\Lambda,T,M)$ where
>- $(Q,\Sigma,T)$ is a state machine;
>- $\Lambda$ is a finite alphabet called the ***output alphabet***;
>- $G:Q\to\Lambda$ called the ***output function***.

>**Definition** (of a program model).
>A ***program model*** is a tuple $(L,D,\Sigma,\Lambda,C,G,T,M,l_0,H)$ where
>- $(L,\Sigma,\Lambda,C,G)$ is a Mealy automaton with the finite state set $L$ called the ***program control structure***;
>- $(D,\Lambda,\Sigma,T,M)$ is a Moore automaton called the ***program data structure***;
>- $l_0\in L$ called the ***initial state***;
>- $H\subset L$ called the ***set of halting states***.

>**Definition** (of a program dynamics).
>Let $P=(L,D,\Sigma,\Lambda,C,G,T,M,l_0,H)$ be a program model then $\delta P:L\times D\to L\times D$ is called the program dynamics if
>$$\delta P(l,d)=(C(l,M(d)),T(d,G(l,M(d)))).$$
>
