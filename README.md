# sound-processing-e

The following program uses SDL2 (Simple DirectMedia layer 2) for to generate a continuous audio waveform (such as a sine wave at 440 Hz, the musical note A4), and saves it into an file.

### Compiling:

```bash
# compile the program:
gcc -arch arm64 -g -o bin/main main.c -DPLOT -I/opt/homebrew/include -L/opt/homebrew/lib -lSDL2 -Wall

# Runs the program:
./bin/main
```

`plot.py` script reads the output file and visualizes the audio waveform using matplotlib. 

```bash
# Creates a virtualenv
python3 -m venv myvenv

# Install dependencies
pip install requirements.txt
```

Topics covered:
- Audio synthesis
- Playback
- Visualization