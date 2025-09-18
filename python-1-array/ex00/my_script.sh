#! source

if [ -d ".venv" ]
then
    source .venv/bin/activate
else
    python3.10 -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r requirement.txt
fi

alias norminette=flake8
