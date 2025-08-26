## DEVELOPING

Install [uv](https://docs.astral.sh/uv/)

To make a simple compatibility test for python3.8 run:

```
uv run src/aihordeclient.py
```

We avoid to have external dependencies far from python standard libraries,
which are huge.

```
uv build
```

[Managin version](https://docs.astral.sh/uv/guides/package/#updating-your-version)

More [uv instructions](https://docs.astral.sh/uv/guides/projects/#running-commands)


