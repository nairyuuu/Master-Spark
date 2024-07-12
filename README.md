# Master Spark
## Description
You are playing Touhou Impershiable Night, a bullet curtain shooting game, and are fighting against Kirisame Marisa, the boss in stage 4B, who launchs master sparks to attack players. Imagine that the game area is in a 2D plane. The player is restricted in a rectangle region M ({(x,y)|0≤x≤X,0≤y≤Y}) and the sparks can be described as ribbon regions Si ({(x,y)|Ci≤Aix+Biy≤Di}). Following is a illustration of this scene.
![alt text](https://espresso.codeforces.com/f8944ecf0cda634ecc0777262bde08de72ab5131.png "Marisa's spell card: Love-sign Master Spark")

Now given X,Y and n sparks S1,S2,...,Sn, you want to know that if there exists such a point P (P∈M) that ∀i∈{1,2,⋯,n}, P∉Si to avoid all sparks and autowin the game.

## Input
The first line contains one integer T (1≤T≤2000), denoting the number of test cases.
For each test case:

- The first line contatins three integers X,Y,n (1≤X,Y≤1000,1≤n≤2000), denoting the size of the game region and the number of sparks.

- Following n lines each contains four integers A,B,C,D (|A|,|B|,|C|,|D|≤1000,A2+B2>0,C≤D), denoting the parameters of given sparks.

- It's guaranteed that ∑n≤2000.

## Output

Output one 01-string S of length T in one line where Si=1 iff such autowinning point exists in case i while Si=0 iff no such points.

## Example

input
```
2
1 1 2
1 -1 -1 0
2 -1 0 2
1 1 2
1 -1 -1 0
1 -2 0 1
```
output
```
01
```
