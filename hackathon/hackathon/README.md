# Error-Proof Calculator API (Prototype)

Quick prototype demonstrating decorators, custom exceptions, and robust error handling.

How to run

1. Ensure you have Python 3.7+ installed.
2. From the project folder run:

```bash
python harness.py
```

Commands
- `demo` — runs a set of edge-case test calls (strings, zero division, etc.)
- `add`, `subtract`, `multiply`, `divide` — interactive prompts for operands
- `exit` — quit

Behavior summary
- `InvalidInputError` is defined and used by `@validate_inputs`.
- `@validate_inputs` checks argument types and returns a friendly error instead of crashing.
- `@safe_divide` catches `ZeroDivisionError` and returns `Infinity`.
- Every call is appended to `log.txt` with arguments and results.
