## Setting up the Environment

This assumes you are using a Unix-based system (MacOS or Linux)

Make sure you are in the `software/` directory (use `cd`)

1. Create a Python virtual environment:
```
python3 -m venv venv
```

2. Enter the virtual environment:

```
source ./venv/bin/activate
```

3. Validate that you are actually in the virtual environment:
```
pip -V
```
The current directory path should be part of what is printed. Every time you start a new shell session, you will need to do steps 2 and 3.

4. Install the dependencies:
```
pip install -r requirements.txt
```

## Running the Code

Make sure steps 2 and 3 have been performed if this is a new shell session. Also make sure you're in the `software/` directory. Run the following:
```
python3 main.py
```
