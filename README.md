This repository is intended to serve as a basic test case for packaging and integrating an application into Pennsieve. Since this is strictly for demonstrative purposes, the application simply reads CSV files and writes them out as JSON files. 

# Local Docker Test

Build the image from the project root:

```bash
docker build -t pennsieve-process-test .
```

Create an output directory for generated JSON files:

```bash
mkdir -p data/output
```

Run the container with the local input and output folders mounted:

```bash
docker run --rm \
  -e INPUT_DIR=/data/input \
  -e OUTPUT_DIR=/data/output \
  -v "$PWD/data/input:/data/input" \
  -v "$PWD/data/output:/data/output" \
  pennsieve-process-test
```

Input CSV files should be placed in `data/input`. Generated JSON files will be written to `data/output`.
