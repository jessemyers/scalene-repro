# scalene-repro

Reproducing [https://github.com/emeryberger/scalene/issues/3]().

## Setup

 - Install into a `virtualenv`:

   ```shell
   python3 -m venv venv
   source venv/bin/activate
   python3 -m pip install -e .
   ```

 - Test the `example` console script entry point:

   ```shell
    example
    ```


## Usage

 1. `scalene` should provide meaningful help.

    Test case:

    ```shell
    python3 -m scalene --help
    ```

    Expected behavior: a usage statement

    Actual behavior:

    ```shell
    scalene: could not find input file.
    ```

 2. `scalene` should handle console script entry points

    Test case:

    ```shell
    python3 -m scalene example
    ```

    Expected behavior: profile the example console script

    Actual behavior:

    ```shell
    scalene: could not find input file.
    ```

 3. `scalene` should produce meaningful output

    Test case:

    ```shell
    python3 -m scalene ./venv/bin/example
    ```

    Expected behavior: some profile output

    Actual behavior:

    ```shell
    The example works!
    ```

    (and no other output)
