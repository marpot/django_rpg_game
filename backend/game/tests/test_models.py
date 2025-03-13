import pytest
from accounts.models import CustomUser
from game.models import PlayerCharacter,GameEvent, GameSession


@pytest.fixture
def test_user(db):
    user = CustomUser.objects.create_user(username='testuser', password='testpassword')

@pytest.fixture
def test_player_character(db, test_user, test_adventure, test_location):  
    return PlayerCharacter.objects.create(
        user=test_user,
        name="Testowa_postac",
        current_location=test_location,
        adventure=test_adventure,
        stats = {"strength": 10, "agility": 8}
    )

@pytest.fixture
def test_game_event(db, test_player_character):
    return GameEvent.objects.create(
        player=test_player_character,
        location=None,
        description="Test description",
        timestamp="2023-05-01 12:00:00",
    )

@pytest.fixture
def test_game_session(db, test_player_character):
    return GameSession.objects.create(
        player=test_player_character,
        progress={"level": 1},
        )

def test_game_session_creation(test_game_session):
    assert test_game_session.created_at is not None
    assert test_game_session.updated_at is not None
    assert test_game_session.created_at == test_game_session.updated_at
