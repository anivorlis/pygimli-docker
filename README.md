# This is a demo on how to use containerize pygimli

The repo runs a simple processing on an example dataset from [pygimli.org](https://www.pygimli.org/_examples_auto/3_ert/plot_02_ert_field_data.html#sphx-glr-examples-auto-3-ert-plot-02-ert-field-data-py).

# What it does
- It builds a container.
- It uses uv to manage python packages. 
- It mounts the data folder to the container (so you can read/write data).
- Runs the processing script, inverts the dataset and stores it in the folder.

# How to use it
- Step 1. Install docker
- Step 2. Build the container (docker build -t pygimli-docker-example .)
- Step 3. Run the container (docker run -v ${PWD}/data:/app/data -e DATA_DIR=/app/data pygimli-docker-example)
