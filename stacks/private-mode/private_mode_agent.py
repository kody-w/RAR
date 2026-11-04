"""Private Mode: name the topics that must never leave this computer.

"keep my health questions private" -> add_topic(health). From then on any chat that mentions it is answered by a
local model (Ollama) whatever model is picked; with no local model running it is refused, never sent out. The
routing itself requires the active providers layer (one provider part per shape); this agent only keeps the list
and cannot verify the host's active layers. Coverage is case-insensitive substring matching, not semantic detection.
Unreadable or invalid policies are errors, never silently replaced with an empty list.
"""
import json
import os

from agents.basic_agent import BasicAgent

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/private_mode_agent",
    "version": "1.0.3",
    "display_name": "Private Mode",
    "description": "Edit private topic substrings; requires the active providers layer to route matching chats locally or refuse. Cannot verify host enforcement.",
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
        except FileNotFoundError:
            return {"topics": []}
        if not isinstance(d, dict) or not isinstance(d.get("topics"), list) or not all(
                isinstance(t, str) and t.strip() for t in d["topics"]):
            raise ValueError("expected an object with a topics list of non-empty strings")
        if d.get("model") is not None and (not isinstance(d["model"], str) or not d["model"].strip()):
            raise ValueError("model must be a non-empty string or null")
        topics = d["topics"]
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
        try:
            t = self._load().get("topics") or []
        except (OSError, ValueError) as error:
            return f"<private_mode>Privacy policy error: {error}. Refuse chat until repaired.</private_mode>"
        if not t:
            return None
        return ("<private_mode>Topics the owner keeps on this computer only: " + ", ".join(t) +
                ". Chats about them are answered by a local model. Never suggest pasting them into another service."
                "</private_mode>")

    def perform(self, action="list", topic=None, text=None, **_):
        try:
            return self._perform(action, topic, text)
        except (OSError, ValueError) as error:
            return f"Privacy policy error: {error}. Policy not updated; repair private-topics.json before retrying."

    def _perform(self, action, topic, text):
        d = self._load()
        topics = d.setdefault("topics", [])
        if action == "add_topic":
            t = _clean(topic)
            if not t:
                return "Which topic should stay private?"
            if t not in topics:
                topics.append(t); self._save(d)
            return (f"Saved private topic '{t}'. Requires the active providers layer for local-only routing; "
                    f"this editor cannot verify enforcement. Private topics: {', '.join(topics)}.")
        if action == "remove_topic":
            t = _clean(topic)
            if t not in topics:
                return f"'{t}' was not on the private list."
            topics.remove(t); self._save(d)
            return f"'{t}' is no longer private. Private topics: {', '.join(topics) or 'none'}."
        if action == "check":
            hit = next((t for t in topics if t in (text or "").lower()), None)
            result = (f"That matches private substring '{hit}'." if hit
                      else "That matches no private substring; semantic privacy is not checked.")
            return result + " Requires the active providers layer; this editor cannot verify enforcement."
        return "Private topics: " + (", ".join(topics) if topics else "none yet. Say 'keep my health questions private'.")
