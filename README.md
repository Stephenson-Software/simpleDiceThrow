# simpleDiceThrow

Lets you throw a dice once or a hundred times and then gives you the statistics.

## Requirements

- **Python 2** — the script uses `print` as a statement, `raw_input`, and `xrange`, none of which are valid in Python 3. Running it under a Python 3 interpreter fails immediately with a `SyntaxError`.
- No third-party packages. The only import is `randint` from the standard library's `random` module.

## Running

```
python2 throwTheDice.py
```

The program prints a prompt, reads a single line of input, acts on it, and then waits for Enter before exiting.

## Options

Input is lowercased before it is compared, so `ONCE` and `once` are equivalent.

| Input | Behavior |
|-------|----------|
| `once` | Rolls the die a single time and prints the result. |
| `hundred` | Rolls the die one hundred times, then prints how many times each of the faces 1 through 6 came up. |
| anything else | Prints `That wasn't an option silly!` and exits. |

The prompt also advertises a `QUIT` option, but no branch implements it — typing `quit` currently takes the "anything else" path above. This is tracked in [issue #2](https://github.com/Stephenson-Software/simpleDiceThrow/issues/2).

## Known issues

Open items are listed on the [issue tracker](https://github.com/Stephenson-Software/simpleDiceThrow/issues).

## License

Released under the Stephenson Software Non-Commercial License (Stephenson-NC). See [LICENSE](LICENSE) for the terms.
