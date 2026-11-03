"""Seat Notes — a private notebook for one seat in a room.

Notes are stored in the seat's own memory folder (the worker swaps that folder per seat),
so one seat can never read another seat's notes.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/seat_notes_agent",
    "version": "1.0.0",
    "display_name": "SeatNotes",
    "description": "Private per-seat notebook for the Rooms distro: remember or recall facts in this seat's own memory only.",
    "author": "kody-w",
    "tags": ["rooms", "memory", "notes", "seat"],
    "category": "core",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

import json
import os
from pathlib import Path

from agents.basic_agent import BasicAgent


def _book():
    # The worker runs with its working directory at the worker folder, where
    # .brainstem_data is a link to the CURRENT seat's private memory folder.
    d = Path(os.getcwd()) / ".brainstem_data"
    d.mkdir(exist_ok=True)
    return d / "seat_notes.json"


class SeatNotesAgent(BasicAgent):
    def __init__(self):
        self.name = "SeatNotes"
        self.metadata = {
            "name": self.name,
            "description": "This seat's private notebook. action 'remember' saves a fact; action 'recall' lists saved facts.",
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string", "enum": ["remember", "recall"]},
                    "fact": {"type": "string", "description": "the fact to remember"},
                },
                "required": ["action"],
            },
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs) -> str:
        book = _book()
        notes = json.loads(book.read_text()) if book.exists() else []
        if kwargs.get("action") == "remember":
            fact = (kwargs.get("fact") or "").strip()
            if not fact:
                return "Nothing to remember."
            notes.append(fact)
            tmp = book.with_suffix(".tmp")
            tmp.write_text(json.dumps(notes))
            os.replace(tmp, book)
            return f"Saved privately: {fact}"
        return "My private notes: " + ("; ".join(notes) if notes else "none yet")
