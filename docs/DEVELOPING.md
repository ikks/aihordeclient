## DEVELOPING

Install [uv](https://docs.astral.sh/uv/)

To make use of Opus translation from hf infrastructure we
now depend on urllib3 and sseclient-py, maintaining 3.8 compatibility
and upwards

To preprare the package for the next release make sure the sample
runs
```
uv run main.py
```

Then update the version with `uv version --bump patch` , minor or major,
push to the repo.

And publish

```
uv build && uv publish -t $PYPI_AIHORDECLIENT_TOKEN dist/aihordeclient-$(grep version pyproject.toml | sed -E 's/.*"(.+).*"/\1/g')*
```



[Managing version](https://docs.astral.sh/uv/guides/package/#updating-your-version)

More [uv instructions](https://docs.astral.sh/uv/guides/projects/#running-commands)


