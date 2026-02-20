import os

import pytest

from scaffold.utils import get_postgresql_url


def test_get_postgresql_url_for_sqlalchemy(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv(
        "DATABASE_URL",
        "postgresql://user:pass@localhost:5432/dbname",
    )

    url = get_postgresql_url(for_sqlalchemy=True)

    assert url == "postgresql+psycopg://user:pass@localhost:5432/dbname"


def test_get_postgresql_url_invalid_scheme(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DATABASE_URL", "mysql://user:pass@localhost:3306/dbname")

    with pytest.raises(ValueError):
        get_postgresql_url()
