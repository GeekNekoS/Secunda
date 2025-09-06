# api/tests/test_office_repo.py
from api.repositories.office_repo import OfficeRepository
from api.models.office import Office
from unittest.mock import AsyncMock, MagicMock
import pytest


@pytest.mark.asyncio
async def test_get_all_office_mock():
    mock_session = AsyncMock()
    repo = OfficeRepository(mock_session)

    office = Office(id=1, address="Тестовый адрес")
    mock_scalars = MagicMock()
    mock_scalars.all.return_value = [office]
    mock_session.execute.return_value = AsyncMock(scalars=MagicMock(return_value=mock_scalars))

    result = await repo.get_all()
    assert result == [office]
    mock_session.execute.assert_awaited()


@pytest.mark.asyncio
async def test_get_by_id_office_mock():
    mock_session = AsyncMock()
    repo = OfficeRepository(mock_session)

    office = Office(id=1, address="Тест")
    mock_scalars = MagicMock()
    mock_scalars.first.return_value = office
    mock_session.execute.return_value = AsyncMock(scalars=MagicMock(return_value=mock_scalars))

    result = await repo.get_by_id(1)
    assert result == office
    mock_session.execute.assert_awaited()
