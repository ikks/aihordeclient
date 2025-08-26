# AIHordeclient

AIHordeclient is a lib to connect to https://aihorde.net/api/v2 and
ease plugin development.

## USAGE

Look at [https://github.com/ikks/aihordeclient/blob/main/main.py](main.py) for the simplest sample, for other real
use cases:

* See [stablehorde-gimp3](https://github.com/ikks/gimp-stable-diffusion/)
* See [libreoffice-stable-horde](https://github.com/ikks/libreoffice-stable-diffusion/)

Get an AIHORDE [free api_key](https://aihorde.net/register) to run
the sample code, once you have installed the package.

```sh
git clone https://github.com/ikks/aihordeclient/
cd aihordeclient
uv venv -p 3.13
source .venv/bin/activate
AIHORDE_API_KEY=<yourapikey> python main.py
```

# AUTHORS

Most of the code descends from
[blueturtleai Gimp 2.10.X plugin](https://github.com/blueturtleai/gimp-stable-diffusion)
initial work.

# THANKS

* AIHorde
