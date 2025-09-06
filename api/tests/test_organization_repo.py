# api/tests/test_organization_repo.py
from api.repositories.organization_repo import OrganizationRepository
from api.models.organization import Organization
from unittest.mock import AsyncMock, MagicMock
import pytest


@pytest.mark.asyncio
async def test_get_all_organization_mock():
    mock_session = AsyncMock()
    repo = OrganizationRepository(mock_session)

    org = Organization(id=1, name="Тестовая организация")
    mock_scalars = MagicMock()
    mock_scalars.all.return_value = [org]
    mock_session.execute.return_value = AsyncMock(scalars=MagicMock(return_value=mock_scalars))

    result = await repo.get_all()
    assert result == [org]
    mock_session.execute.assert_awaited()


@pytest.mark.asyncio
async def test_get_by_id_organization_mock():
    mock_session = AsyncMock()
    repo = OrganizationRepository(mock_session)

    org = Organization(id=1, name="Тест")
    mock_scalars = MagicMock()
    mock_scalars.first.return_value = org
    mock_session.execute.return_value = AsyncMock(scalars=MagicMock(return_value=mock_scalars))

    result = await repo.get_by_id(1)
    assert result == org
    mock_session.execute.assert_awaited()


@pytest.mark.asyncio
async def test_get_by_activity_mock():
    mock_session = AsyncMock()
    repo = OrganizationRepository(mock_session)

    org = Organization(id=1, name="Тест")
    mock_scalars = MagicMock()
    mock_scalars.all.return_value = [org]
    mock_session.execute.return_value = AsyncMock(scalars=MagicMock(return_value=mock_scalars))

    result = await repo.get_by_activity(1)
    assert result == [org]
    mock_session.execute.assert_awaited()
