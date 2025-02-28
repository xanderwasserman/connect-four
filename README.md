# connect-four

A simple Connect Four game, written in Python. A demo can be found on [connect4.alexanderwasserman.co.za](https://connect4.alexanderwasserman.co.za)

There are two versions which can be run:
- A simple CLI User Interface
- A basic web application

You can run these as follows:
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

    - Linux/MacOS:
        ```bash
        python -m venv venv
        source venv/bin/activate   # On Linux / Mac
        ```
    - Windows: 
        ```bash
        venv\Scripts\activate
        ```

3. **Install dependencies**:

    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
4. **Run the game**:

    - CLI Version:
        ```bash
        python main_cli.py
        ```
    - Web App Version:
        ```bash
        python main_web.py
        ```

    - Press `Ctrl + C` to stop the program.

## 3. Running with Docker (preferred method)

1. **Build and start**:

    - CLI Version:
        ```bash
        docker build -t connect-four-cli -f Dockerfile.cli .
        ```

    - Web Version:
        ```bash
        docker build -t connect-four-web -f Dockerfile.web .
        ```

    This will install dependencies and copy the code into the container.

2. **Run the container**:

    - CLI Version:
        ```bash
        docker run -it --rm connect-four-cli
        ```
        - `-it` gives you an interactive shell so you can type your moves.
        - `--rm` removes the container after you exit.

        You will see CLI prompts in the terminal. Enter the column numbers to play.

    - Web Version:
        ```bash
        docker run -d --rm connect-four-web
        ```
        - `-d` detaches your terminal from the container shell for it to run in the background. Otherwise use `-it` to give you an interactive shell so you can easily exit the program.
        - `--rm` removes the container after you exit.

        Navigate to http://localhost:5000 on your web browser to access the web interface.

2. **Stop the container**: 

    - If you used an interactive terminal (`-it`) then you can simply stop by pressing `Ctrl + C` on your keyboard.
    - If you ran the container detached (`-d`) then you can use the `docker ps` command to list all running docker containers. Find the `CONTAINER ID` if the Image called `connect-four-web` and copy it. Then enter the following in your terminal, replacing `<container-id>` with the ID that you just copied:
        ```bash
        docker stop <container-id>
        ```

## 5. Running Tests

1. **Locally**:

    From the project root, after installing dependencies:
    ```bash
    python -m unittest discover tests
    ```

2. **Within Docker**:

    You can use either of the following two commands:
    ```bash
    docker build -t connect-four-cli -f Dockerfile.cli . && docker run -it --rm connect-four-cli python -m unittest discover tests
    ```
    ```bash
    docker build -t connect-four-web -f Dockerfile.web . && docker run -it --rm connect-four-web python -m unittest discover tests
    ```
