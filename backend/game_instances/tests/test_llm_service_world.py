import unittest

from game_instances.services.llm.orchestrator.llm_service import LLMService


class LLMServiceWorldTests(unittest.TestCase):
    def test_generate_world_returns_intro_and_choices(self):
        service = LLMService()

        world = service.generate_world({
            "adventure": {
                "id": 1,
                "title": "Cień Karczmy",
                "description": "Mroczna karczma na skraju miasta",
            }
        })

        self.assertIn("Cień Karczmy", world["intro"])
        self.assertTrue(world.get("choices"))
        self.assertEqual(world["choices"][0]["action"], "inspect")


if __name__ == "__main__":
    unittest.main()
