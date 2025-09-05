## DEVELOPING

Install [uv](https://docs.astral.sh/uv/)

To make a simple compatibility test for python3.8 run:

```
uv run src/aihordeclient.py
```

To make use of Opus translation from hf infrastructure we
now depende on urllib3 and sseclient-py, maintaining 3.8 compatibility
and upwards

To preprare the package for the next release make sure the sample
runs
```
uv run main.py
```

After everything is ok with the new version

```
uv build && uv publish
```

[Managing version](https://docs.astral.sh/uv/guides/package/#updating-your-version)

More [uv instructions](https://docs.astral.sh/uv/guides/projects/#running-commands)


