# api/tests/test_activity_repo.py
from api.repositories.activity_repo import ActivityRepository
from api.models.activity import Activity
from unittest.mock import AsyncMock, MagicMock
import pytest


@pytest.mark.asyncio
async def test_get_all_activity_mock():
    mock_session = AsyncMock()
    repo = ActivityRepository(mock_session)

    activity = Activity(id=1, name="Тестовая деятельность")

    # Мок scalars().all()
    mock_scalars = MagicMock()
    mock_scalars.all.return_value = [activity]
    mock_session.execute.return_value = AsyncMock(scalars=MagicMock(return_value=mock_scalars))

    result = await repo.get_all()
    assert result == [activity]
    mock_session.execute.assert_awaited()


@pytest.mark.asyncio
async def test_get_by_id_activity_mock():
    mock_session = AsyncMock()
    repo = ActivityRepository(mock_session)

    activity = Activity(id=1, name="Тест")
    mock_scalars = MagicMock()
    mock_scalars.first.return_value = activity
    mock_session.execute.return_value = AsyncMock(scalars=MagicMock(return_value=mock_scalars))

    result = await repo.get_by_id(1)
    assert result == activity
    mock_session.execute.assert_awaited()
