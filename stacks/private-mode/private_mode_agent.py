"""Private Mode: name the topics that must never leave this computer.

"keep my health questions private" -> add_topic(health). From then on any chat that mentions it is answered by a
local model (Ollama) whatever model is picked; with no local model running it is refused, never sent out. The
routing itself lives in the providers layer (one provider part per shape); this agent only keeps the list.
"""
import json
import os

from agents.basic_agent import BasicAgent

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/private_mode_agent",
    "version": "1.0.2",
    "display_name": "Private Mode",
    "description": "Name topics (health, money, a person) that must never leave this computer; chats about them are answered by a local model or not at all.",
    "author": "kody-w",
    "tags": ["privacy", "local", "ollama", "topics"],
    "category": "privacy",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

FILE = os.path.join(os.environ.get("GRAIL_LAYERS_HOME") or os.path.expanduser("~/.brainstem/layers"), "private-topics.json")


FILLER = {"my", "our", "the", "a", "an", "about", "questions", "question", "stuff", "things", "topics", "topic",
          "anything", "related", "to", "chats", "chat", "info", "information"}


def _clean(topic):
    """'my money questions' -> 'money': the topic is the word that will actually appear in a chat."""
    words = [w for w in (topic or "").lower().replace(",", " ").split() if w not in FILLER]
    return " ".join(words).strip()


class PrivateModeAgent(BasicAgent):
    def __init__(self):
        self.name = "PrivateMode"
        self.metadata = {
            "name": self.name,
            "description": ("Keeps the list of private topics that must never leave this computer. Use when the person "
                            "says 'keep X private', 'stop keeping X private', 'what is private', or asks whether a "
                            "question would stay on this computer."),
            "parameters": {"type": "object", "properties": {
                "action": {"type": "string", "enum": ["add_topic", "remove_topic", "list", "check"]},
                "topic": {"type": "string", "description": "ONE plain word that will appear in such chats, e.g. 'health', 'money', 'divorce'"},
                "text": {"type": "string", "description": "for check: the question to test"}},
                "required": ["action"]},
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def _load(self):
        try:
            with open(FILE) as f:
                d = json.load(f)
            d = d if isinstance(d, dict) else {"topics": []}
        except Exception:
            return {"topics": []}
        topics = d.get("topics") or []
        fixed = list(dict.fromkeys(_clean(t) or t for t in topics if isinstance(t, str)))
        if fixed != topics:  # heal lists written before 1.0.1, every turn (system_context loads it each chat)
            d["topics"] = fixed
            self._save(d)
        return d

    def _save(self, d):
        os.makedirs(os.path.dirname(FILE), exist_ok=True)
        tmp = FILE + ".tmp"
        with open(tmp, "w") as f:
            json.dump(d, f, indent=1)
        os.replace(tmp, FILE)

    def system_context(self):
        t = self._load().get("topics") or []
        if not t:
            return None
        return ("<private_mode>Topics the owner keeps on this computer only: " + ", ".join(t) +
                ". Chats about them are answered by a local model. Never suggest pasting them into another service."
                "</private_mode>")

    def perform(self, action="list", topic=None, text=None, **_):
        d = self._load()
        topics = d.setdefault("topics", [])
        if action == "add_topic":
            t = _clean(topic)
            if not t:
                return "Which topic should stay private?"
            if t not in topics:
                topics.append(t); self._save(d)
            return f"'{t}' is private now: chats about it stay on this computer. Private topics: {', '.join(topics)}."
        if action == "remove_topic":
            t = _clean(topic)
            if t not in topics:
                return f"'{t}' was not on the private list."
            topics.remove(t); self._save(d)
            return f"'{t}' is no longer private. Private topics: {', '.join(topics) or 'none'}."
        if action == "check":
            hit = next((t for t in topics if t in (text or "").lower()), None)
            return (f"That mentions '{hit}', so it stays on this computer." if hit
                    else "That mentions no private topic, so it goes to the model you picked.")
        return "Private topics: " + (", ".join(topics) if topics else "none yet. Say 'keep my health questions private'.")
