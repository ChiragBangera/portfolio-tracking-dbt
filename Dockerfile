FROM astral/uv:python3.12-bookworm-slim

WORKDIR /

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen

WORKDIR /dbt

CMD [ "bash" ]
