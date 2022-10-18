## Reflex agent
```
python pacman.py --frameTime 0 -p ReflexAgent -k 1
python pacman.py --frameTime 0 -p ReflexAgent -k 1 -g DirectionalGhost
python autograder.py -q q1
```

## Minimax agent
```
python pacman.py --frameTime 0 -p ReflexAgent -k 2
python pacman.py --frameTime 0 -p ReflexAgent -k 2 -g DirectionalGhost
python autograder.py -q q2
```

## Alpha-Beta agent
```
python pacman.py -p AlphaBetaAgent -l minimaxClassic -a depth=2
python autograder.py -q q3
```

## Expectimax agent
```
python pacman.py --frameTime 0 -p ExpectimaxAgent -k 2
python pacman.py --frameTime 0 -p ExpectimaxAgent -k 2 -g DirectionalGhost
python autograder.py -q q4
```

## Evaluation function
```
python autograder.py -q q5
```
