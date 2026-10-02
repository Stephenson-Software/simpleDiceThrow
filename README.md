# simpleDiceThrow

Lets you throw a dice once or a hundred times and then gives you the statistics.

## Requirements

- **Python 3**. (It was written for Python 2 and ported to Python 3 when it was put in the browser.)
- No third-party packages. The only import is `randint` from the standard library's `random` module.

## Running

```
python3 throwTheDice.py
```

The program prints a prompt, reads a single line of input, acts on it, and then waits for Enter before exiting.

## Options

Input is lowercased before it is compared, so `ONCE` and `once` are equivalent.

| Input | Behavior |
|-------|----------|
| `once` | Rolls the die a single time and prints the result. |
| `hundred` | Rolls the die one hundred times, then prints how many times each of the faces 1 through 6 came up. |
| anything else | Prints `That wasn't an option silly! Try ONCE or HUNDRED.` and exits. |

The prompt also advertises a `QUIT` option, but no branch implements it — typing `quit` currently takes the "anything else" path above. This is tracked in [issue #2](https://github.com/Stephenson-Software/simpleDiceThrow/issues/2).

## Known issues

Open items are listed on the [issue tracker](https://github.com/Stephenson-Software/simpleDiceThrow/issues).

## Play in your browser
The same game, unmodified, runs in a browser tab under [tak](https://github.com/Stephenson-Software/tak)'s console runtime (Python via Pyodide): https://dice.play.danielstephenson.dev, listed with the rest at [danielstephenson.dev/play](https://danielstephenson.dev/play). To build and serve it locally (needs `tak` installed):
```
python3 web/build_zip.py
python3 -c "from tak.web.serve import main; main(root='.', title='Simple Dice Throw')"
```
Pushes to `master` deploy it to [arcade](https://github.com/Stephenson-Software/arcade) (`.github/workflows/browser.yml`).

## License

Released under the Stephenson Software Non-Commercial License (Stephenson-NC). See [LICENSE](LICENSE) for the terms.
