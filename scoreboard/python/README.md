## Chess.com Python API

### Environment set up

Download and install [Miniconda](https://docs.conda.io/en/latest/miniconda.html). Create a virtual environment

	conda create -n chess python=3.7 

NOTE: make sure to use Python 3.7 as the Chess.com package depends on it. 
Activate the virtual environment by running:

	conda activate chess

Once the virtual environment is activated download the dependencies via:

	pip install -r scoreboard/python/requirements.txt

Lastly, append the path to this repository to the system python path:

	export PYTHONPATH=$PYTHONPATH:/path/to/discord-chess-scorecard

From here, you should be able to run python files from the repository directory, i.e.:

	cd /path/to/discord-chess-scorecard
	python scoreboard/python/...

### Usage