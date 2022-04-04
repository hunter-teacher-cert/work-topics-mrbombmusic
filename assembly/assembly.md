### Assembly assignment part 1

Problem was 3rd input was subtracted from value in mailbox.
Needed to store 3rd input value in mailbox, then put sum value in accumulator, then subtract 3rd input value which was stored in a different mailbox

```

INP
STA 99
INP
ADD 99
STA 99
INP
STA 98
LDA 99
SUB 98
OUT
HLT

```
**MILD**

Two inputs - output larger number

```
INP
STA 99
INP
ADD 99
STA 99
INP
STA 98
LDA 99
SUB 98
OUT
HLT

```
