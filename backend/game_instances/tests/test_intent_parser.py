from game_instances.services.llm.intent.intent_parser import IntentParser


def test_polish_move_phrase_is_parsed_as_move():
    parser = IntentParser()

    result = parser.parse("idę do karczmy")

    assert result["action"] == "move"
    assert result["target"] is not None
