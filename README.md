# Knowledge curation service

# Context

# Running locally

1. Install Poetry for dependency management https://python-poetry.org/docs/
2. Run `poetry self add poetry-exec-plugin && poetry self add poetry-plugin-export` (sadly it is [not possible](https://github.com/python-poetry/poetry/issues/7657) to add `poetry`'s plugins to pyproject.toml currently)
3. Run `poetry install`
4. To build locally by run `poetry exec build`
5. To simulate dispatch of an SQS message locally run `poetry exect consume-sqs-event`

You can initialise virtual env with `poetry shell`
You can add custom commands to `pyproject.toml` underneath the `[tool.poetry-exec-plugin.commands]` section and run them with `poetry exec <command>`

# Managing dependencies

- Ignore `requirements.txt` file! Dependencies are declared and managed in the `pyproject.toml` file and locked in the `poetry.lock` file.
- Currently dependencies broken into dev and main dependencies - only main
  dependencies are used in production, dev dependencies are ignored
- You can add a dev dependency by running `poetry add <dep_name_1 depn_name_2...> --group-dev`.
  Omit `group` flag for a prod dep
- `requirements.txt` exists to make `sam build` work properly. It is updated
  automatically via a pre-commit hook, you should not need to edit it manually
