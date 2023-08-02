# Computation is an interaction of Mealy and Moore Automata

Here, the general imperative model of computation is given.
This model was proposed by V. Glushkov in 1964.
We demonstrate that the unlimited register machine is a particular case of this general concept.

## State Machines

A state machine is a principal concept for our further consideration.

### Definitions

>**Definition** (of a state machine).
>A ***state machine*** is a triple $(Q,\Sigma,\mathtt{do})$ where
>- $Q$ is a set whose elements are called ***states***;
>- $\Sigma$ is a finite alphabet called the ***input alphabet***;
>- $\mathtt{do}:Q\to Q^\Sigma$ called the ***transition function***.

The presented definition specifies only the structure of a state machine but does not say anything about its behaviour.
To define the behaviour of a state machine, the following function $\mathtt{run}: Q\to Q^{\Sigma^\ast}$ is needed where

$$\begin{array}{ll}
\mathtt{run}\ q=\lambda\ x:\Sigma^\ast\mathop{.}&\mathtt{match}\ x\ \mathtt{with} \\
&\mid[\ ]\Rightarrow\ q \\
&\mid a :: \mathtt{tail}\Rightarrow\ \mathtt{run}\ (\mathtt{do}\ q\ a)\ \mathtt{tail} \\
&\mathtt{end}\end{array}\quad\quad\quad\texttt{for any $q\in Q$.}$$

Sometimes, this function is called the ***reaction function*** of the state machine.

### Python realization

```
class StateMachine:
    """
    Attributes:
    -----------
        _Q      the state set
        _Sigma  the input alphabet

    Methods:
    --------
        do      the transition function
        run     the reaction function
    """

    def __init__(self, Q, Sigma, do):
        """StateMachine constructor"""
        args_checkingflag = (
            isinstance(Q, set) and
            isinstance(Sigma, set) and
            callable(do))                # is True if arguments are correct
        if not args_checkingflag:
            raise ValueError("invalid argument(s) of state machine constructor")
        self._Q = Q
        self._Sigma = Sigma
        self._do = do

    def do(self, q, a):
        """returns the result of applying the transition function"""
        if q in self._Q and a in self._Sigma:
            try:
                return self._do(q, a)
            except:
                raise ValueError("check definition of 'do'")
        raise ValueError("invalid 'do'-argument(s)")

    def run(self, q, aa):
        """returns the result of applying the reaction function"""
        args_checkingflag = (
            isinstance(aa, list) and
            all(map(lambda x: x in self._Sigma, aa)))
        if not args_checkingflag:
            raise ValueError("invalid argument of 'run'")
        if aa:
            a, aaa = aa[0], aa[1 :]
            return self.run(self.do(q, a), aaa)
        else:
            return q
```

The function $\mathtt{run}$ determines the states changing of a state machine as the response to a sequence of input impacts.

Such an approach can be characterized as a sequential approach due to the following properties of the function $\mathtt{run}$.

>**Proposition**.
>Let $(Q,\Sigma,\mathtt{do})$ be a state machine then
>1. $\mathtt{run}\ q\ [\ ]=q$ for any $q\in Q$;
>2. $\mathtt{run}\ q\ [a]=\mathtt{do}\ q\ a$ for any $q\in Q$ and $a\in\Sigma$;
>3. $\mathtt{run}\ q\ (x + y)=\mathtt{run}\ (\mathtt{run}\ q\ x)\ y$ for any $q\in Q$ and $x,y\in\Sigma^\ast$.

## Mealy Automata

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
