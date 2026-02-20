from unittest.mock import AsyncMock

import pytest

from scaffold.persistence.uow import BaseSqlUnitOfWork


@pytest.mark.asyncio
async def test_context_manager_returns_self_and_cleans_up() -> None:
    session = AsyncMock()
    uow = BaseSqlUnitOfWork(session)

    async with uow as entered:
        assert entered is uow

    session.rollback.assert_awaited_once()
    session.close.assert_awaited_once()
