# connect-four

A simple CLI-based Connect Four game, written in Python. You can run it:
1. **Directly on your machine** (using a virtual environment).
2. **Via Docker** (build and run the container).
3. **Via Docker Compose**.

---

## 1. Prerequisites

- [Python 3.9+](https://www.python.org/downloads/) (if running locally)
- [Docker](https://docs.docker.com/get-docker/) (if running in a container)
- [Docker Compose](https://docs.docker.com/compose/) (if using `docker-compose.yml`)

---

## 2. Running Locally on Linux with Python and `venv`

1. **Clone** or download this repository.

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux / Mac
   # or, on Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
4. **Run the game**:

    ```bash
    python main.py
    ```

    You should see something like this:
    ```bash
    |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |
    -----------------------------
    Organic Player's turn.
    Enter a column (0-6): 
    ```

    - Press `Ctrl + C` to stop.

## 3. Running with Docker

1. **Build and start**:

    ```bash
    docker build -t connect-four-image .
    ```

    This will install dependencies and copy the code into the container.

2. **Run the container interactively**:

    ```bash
    docker run -it --rm connect-four-image
    ```

    - `-it` gives you an interactive shell so you can type your moves.
    - `--rm` removes the container after you exit.

    You will see CLI prompts in the terminal. Enter the column numbers to play.

## 4. ~~Running with Docker Compose~~

If you prefer Docker Compose:

1. **Build and start**:

    ```bash
    docker compose up --build
    ```

    If this gives an error, you might have an older version of Docker Compose installed. Try using:
    ```bash
    docker-compose up --build
    ```

    - This builds the image (from the included Dockerfile) and starts a container named `connect-four-container`.
    - `tty: true` and `stdin_open: true` in `docker-compose.yaml` ensure you can interact with the game.

2. **Stop the container**: 

    - If you used `docker-compose up`, press `Ctrl + C` to stop.


## 5. Running Tests

1. **Locally**:

    From the project root, after installing dependencies:
    ```bash
    python -m unittest discover tests
    ```

2. **Within Docker**:

    ```bash
    docker build -t connect-four-image . && docker run -it --rm connect-four-image python -m unittest discover tests
    ```