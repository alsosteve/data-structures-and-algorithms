# [Data Structures and Algorithms](https://alsosteve.github.io/data-structures-and-algorithms/)
## [Language: Python](https://alsosteve.github.io/data-structures-and-algorithms/python/)

# Stack and a Queue: Multi Bracket Validation
## Feature Tasks
* Write a function called validate brackets
* Arguments: string
* Return: boolean
  * representing whether or not the brackets in the string are balanced

There are 3 types of brackets:

1. Round Brackets : `()`
2. Square Brackets : `[]`
3. Curly Brackets : `{}`


## Whiteboard Process
![challenge13](13.png)

## Examples

| Input	| Output |
|---|---|
| `{}`	| TRUE	|
| `{}(){}`	| TRUE	|
| `()[[Extra Characters]]`	| TRUE	|
| `(){}[[]]`	| TRUE	|
| `{}{Code}[Fellows](())`	| TRUE	|
| `[({}]	`	| FALSE	|
| `(](`	| FALSE	|
| `{(})`	| FALSE	|

> Consider these small examples and why they fail.

| Input	|	Output	|	Why	|
|---|---|---|
| `{`	|	`FALSE`	|	error unmatched opening `{` remaining.	|
| `)`	|	`FALSE`	|	error closing `)` arrived without corresponding opening.	|
| `[}`	|	`FALSE`	|	error closing `}`. Doesn’t match opening `(`.	|

## Unit Tests
* complete tests depicted by examples

## Stretch Goal
None
## Approach & Efficiency
This one was too hard for me. My solution was a `O(N^N)` solution so I asked my classmates what they came up with instead.
