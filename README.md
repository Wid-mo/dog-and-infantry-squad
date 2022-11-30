# dog-and-infantry-squad
Visual solution to math problem. And solving more general problem.


<img src="https://user-images.githubusercontent.com/22799520/204902772-afe315ab-e8e5-4ec5-b8c2-69eb3941bb4c.gif" alt="thumbnail" width=500 title='thumbnail' />

## assignment from the book

> An infantry squad, formed in the shape of a square with side b = 20m marches in a straight line at a constant speed. In the middle of the last row (at the end of the squad) runs a dog, which is the mascot of the squad. At some point, the dog ran (at constant speed), to the first row of the squad. After reached the first row the dog immediately returns to the last row. At the same time as the dog ran from last row to first row and from first row to last row infantry squad moved by s = 20m. How far (how many meters) did the dog travel from last row to first row and back? 

<img src="./visual-solution.gif" alt="Infantry squad moved up. Stopped. Next continue movement and again stop" width=200 title="Visual solution" />

**WHAT DISTANCE DID THE DOG TRAVEL❓**

## General solution

![rysunek-poczatkowy](https://user-images.githubusercontent.com/22799520/204905880-780b5064-5e04-49a9-a967-d4274a35c6a3.png)

$$
  \begin{cases}
  V_d=\frac{s_1}{t_1} & \text{dog's speed in the first phase of movement}\\
  V_d=\frac{s_2}{t_2} & \text{dog's speed in the second phase of movement}
  \end{cases}
$$

compare:

$$
\begin{equation}
\frac{s_1}{t_1} = \frac{s_2}{t_2}
\end{equation}
$$

---

### Simplify $s_2$:

![obliczone-s2](https://user-images.githubusercontent.com/22799520/204910196-dc2df1d8-0951-4215-89f9-352d63ef748c.png)

where:  
&emsp;_C - total length_  
&emsp;_D - squad length_

---

### $t_1$ and $t_2$ into $t$.  
First and second phase of movement (t_1 + t_2) last 1 unit of time.  
Variable $t$ is time of movement in first phase.  
So:

    t_1 = t 
    t_2 = 1 - t

---

### Simplify $s_1$  
$s_1$ = (`distance travelled by squad in first phase`) + (`squad length`)

Squad diring a whole movement travel distance $C - D$.  
So _distance travelled by squad in first phase_ = $(C - D)*t$

$$ s_1 = (C - D)t + D $$

---

### Let's substitute everything into first equation (1)
$$ \frac{s_1}{t_1} = \frac{s_2}{t_2} $$
$$ \frac{(C - D)*t+D}{t} = \frac{s_1-(C-D)}{1-t} $$
$$ \frac{(C - D)*t+D}{t} = \frac{(C - D)*t+D-(C-D)}{1-t} $$
$$ \frac{(C - D)*t+D}{t} = \frac{(C - D)*t+2D-C}{1-t} $$

Multiplying fractions:

$$ (C - D)t^2 + 2Dt - Ct = (C - D)t + D - (C - D)t^2 - Dt$$
$$ 2(C - D)t^2 + 3Dt - Ct - (C - D)t - D = 0 $$
$$ 2(C - D)t^2 + 3Dt - 2Ct + Dt - D = 0 $$
$$ 2(C - D)t^2 + (4D - 2C)t - D = 0 $$
$$ \begin{equation} 2(C - D)t^2 + 2(2D - C)t - D = 0 \end{equation} $$

Now we solve quadratic equation. Let's see that for data from our assignment equation greatly simplifies.  
$t$ in first power is reduced. And later we easily solved the rest of the assignment.

$$
  t = \frac{\sqrt{2}}{2}\approx 71\%   
  s_1 \approx 34.14m   
  s_2 \approx 14.14m    
  s_1 + s_2 = 48.28m
$$

---

### To get more general equations we must solve quadratic equation (2):  
$$ t_{1,2} = \frac{-2(2D-C) \pm \sqrt{4(2D-C)^2 + 4*2(C-D)*D}}{4(C-D)} $$
$$ t_{1,2} = \frac{-(2D-C) \pm \sqrt{(2D-C)^2 + 2(C-D)*D}}{2(C-D)} $$
$$ t_{1,2} = \frac{-(2D-C) \pm \sqrt{4D^2 - 4DC + C^2 - 2D^2 + 2CD}}{2(C-D)} $$
$$ t_{1,2} = \frac{-(2D-C) \pm \sqrt{2D^2 -2DC + C^2}}{2(C-D)} $$
$$ t_{1,2} = \frac{-(2D-C) \pm \sqrt{(D - C)^2 + D^2}}{2(C-D)} $$
or
$$ t_{1,2} = \frac{-(2D-C) \pm \sqrt{(C - D)^2 + D^2}}{2(C-D)} $$
Let's put everything into form $(C - D)$
$$ t_{1,2} = \frac{(C - D) \pm \sqrt{(C - D)^2 + D^2} - D}{2(C-D)} $$
We know that $C > D$. and that our result $t \in (0; 1)$. So our $t$ must be positive.  
Denominator always be positive. Variable $D$ is greater than 0. The value on the square root is greater than, what is on the left, i.e $(C - D)$.  
It means that we can extrude case with minus sign under square root. Because it always return negative nominator, and so negative $t$.  
$$ t = \frac{(C - D) + \sqrt{(C - D)^2 + D^2} - D}{2(C-D)} $$
We can simplify further:
$$ t = \frac{1}{2} + \frac{\sqrt{(C - D)^2 + D^2} - D}{2(C-D)} $$
and:

$$
\begin{cases}
  s_{squad} = C - D \\
  t = \frac{1}{2} (1 + \frac{\sqrt{s_{squad}^2 + D^2} - D}{s_{squad}}) \\
\end{cases}
$$

And how to understand this expression: $\frac{\sqrt{s_{squad}^2 + D^2} - D}{s_{squad}}$?  
Let's see this inequality: $$\sqrt{a^2+b^2} \le \sqrt{a^2} + \sqrt{b^2}$$
Applying this transformation on expression we get the information that this expression cannot be greater than 1.  
and so $t$ takes values in the range: $$t \in (0.5; 1)$$

---

## **Results:**

$$
\begin{cases}
  s_{squad} = C - D \\
  t = \frac{1}{2} (1 + \frac{\sqrt{s_{squad}^2 + D^2} - D}{s_{squad}}) \\
  s_1 = s_{squad}*t + D \\
  s_2 = s_1 - s_{squad}
\end{cases}
$$

where:  
    $s_{squad}$ total distance travelled by squad  
    $t$ time of first phase movement (in percent)  
    $s_1$ distance travelled by dog in first phase  
    $s_2$ distance travelled by dog in second phase  
    $D$ squad length  
    $C$ total height

---

## Visualisation of general solution

<img src="https://user-images.githubusercontent.com/22799520/204917937-bd39969a-778e-4656-85eb-3b57ed259619.gif" alt="couple-examples-general-solution" width=300 title='general solution, infinite animation' />

## **Visualisation of general solution in Codepen**

[See visualisation](https://codepen.io/wid-mo/pen/BaJGEWo)

## ❗❗ **Source code calculating the result**

```javascript
function solve(heightOfInfantrySquad = 20, totalHeight = 40) {
  const [D, C] = [heightOfInfantrySquad, totalHeight];

  // time
  const s_squad = C - D; // infantry squad total distance travelled
  const t = 0.5 * (1 + (Math.sqrt(s_squad ** 2 + D ** 2) - D) / s_squad); // first phase percent time (t in scope (0.5; 1) )
  const firstPhaseTimePercent = t;
  const secondPhaseTimePercent = 1 - t;

  const firstPhase = {
    dogDistance: s_squad * firstPhaseTimePercent + D,
    squadDistance: s_squad * firstPhaseTimePercent,
    timePercent: firstPhaseTimePercent,
  };
  const secondPhase = {
    dogDistance: firstPhase.dogDistance - s_squad,
    squadDistance: s_squad * secondPhaseTimePercent,
    timePercent: secondPhaseTimePercent,
  };
  const totalDistances = {
    dog: firstPhase.dogDistance + secondPhase.dogDistance,
    squad: s_squad,
  };

  const VDog = totalDistances.dog / 1; // both phases lasted one unit of time
  const VSquad = totalDistances.squad / 1;
  const howManyTimesDogIsFasterThenSquad = VDog / VSquad;

  return {
    firstPhase,
    secondPhase,
    totalDistances,
    howManyTimesDogIsFasterThenSquad,
  };
}
```

## Results for the assignment in the book

### solve():

```javascript
{
  firstPhase: {dogDistance: 34.14213562373095, squadDistance: 14.142135623730951, timePercent: 0.7071067811865476}
  howManyTimesDogIsFasterThenSquad: 2.414213562373095
  secondPhase: {dogDistance: 14.142135623730951, squadDistance: 5.857864376269049, timePercent: 0.2928932188134524}
  totalDistances: {dog: 48.2842712474619, squad: 20}
}
```

## Using code to solve the task

Paste above code to console in browser. <br>
Next to show solution, write this:

```javascript
solve(20, 40);
```

<br>

---

[Link to project with thumbnail from Desmos](https://www.desmos.com/calculator/1bryohyg4d)
