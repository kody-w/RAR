---
name: "rar-cat-agent-skills-spend-more-time-with-friends-and-family"
description: "While you're out of office, watches a group chat and answers questions from your local knowledge docs (clearly marked AI-generated), logs anything it can't answer for later, and pings you on Teams if its setup is incomplete."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/spend_more_time_with_friends_and_family", "rar_sha256": "d11659b95fb22912398412b573f58ec52b940dcff10574f772ed0a4b4be892db", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "spend_more_time_with_friends_and_family_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/spend-more-time-with-friends-and-family:50fc9235f98e5d882bb0e6168318d056f071160b6d20a213f3217723be7864a0", "kind": "skill"}, "version": "2.0.0", "author": "Adi Leibowitz", "tags": ["automation", "teams", "out_of_office", "knowledge"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/spend_more_time_with_friends_and_family`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `spend_more_time_with_friends_and_family_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

Spend More Time With Friends & Family — While you're out of office, watches a group chat and answers questions from your local knowledge docs (clearly marked AI-generated), logs anything it can't answer for later, and pings you on Teams if its setup is incomplete.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#spend-more-time-with-friends-and-family
  Upstream author: Adi Leibowitz
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `spend_more_time_with_friends_and_family_agent.py` and embedded as the fenced Python below (sha256 d11659b95fb22912…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `spend_more_time_with_friends_and_family_agent.py` first:

```bash
python3 spend_more_time_with_friends_and_family_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 spend_more_time_with_friends_and_family_agent.py   # or on stdin
python3 spend_more_time_with_friends_and_family_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Spend More Time With Friends & Family — While you're out of office, watches a group chat and answers questions from your local knowledge docs (clearly marked AI-generated), logs anything it can't answer for later, and pings you on Teams if its setup is incomplete.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#spend-more-time-with-friends-and-family
  Upstream author: Adi Leibowitz
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/spend_more_time_with_friends_and_family',
    "version": '2.0.0',
    "display_name": 'Spend More Time With Friends & Family',
    "description": "While you're out of office, watches a group chat and answers questions from your local knowledge docs (clearly marked AI-generated), logs anything it can't answer for later, and pings you on Teams if its setup is incomplete.",
    "author": 'Adi Leibowitz',
    "tags": ['automation', 'teams', 'out_of_office', 'knowledge'],
    "category": 'integrations',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'spend-more-time-with-friends-and-family',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#spend-more-time-with-friends-and-family',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'bd12abb4ba09a5e5',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Scout'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'kind:automation'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class SpendMoreTimeWithFriendsAndFamily(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'SpendMoreTimeWithFriendsAndFamily'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
                "required": ["operation"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── helpers ─────────────────────────────────────────────────────────

    def _subject(self, kwargs):
        for key in ("subject", "input", "target", "topic"):
            value = str(kwargs.get(key) or "").strip()
            if value:
                return value
        return ""

    def _header(self, subject):
        label = subject or f"<no {_SPEC['subject_label']} supplied>"
        return f"{_SPEC['verb']}: {label}"

    def _context(self, kwargs):
        extras = []
        for key in _SPEC["params"]:
            if key == "subject":
                continue
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _plan(self, subject, kwargs):
        lines = [self._header(subject)]
        extras = self._context(kwargs)
        if extras:
            lines += ["", "Context:"] + [f"  {e}" for e in extras]
        lines += ["", "Procedure:"]
        lines += [f"  {i}. {step}" for i, step in enumerate(_SPEC["steps"], 1)]
        if not subject:
            lines += [
                "",
                f"Pass subject=\u0022...\u0022 to bind this procedure to a "
                f"specific {_SPEC['subject_label']}.",
            ]
        return lines

    def _checklist(self):
        return ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]]

    def _provenance(self):
        src = __manifest__["source"]
        lines = [
            f"{__manifest__['display_name']} (v{__manifest__['version']})",
            "",
            __manifest__["description"],
            "",
            f"Capability shape: {_SPEC['archetype']} "
            f"(confidence {_SPEC['confidence']})",
        ]
        platforms = __manifest__.get("platforms") or []
        if platforms:
            lines.append("Runs on:          " + ", ".join(platforms))
        lines += [
            "",
            f"Indexed from:     {src['source_name']}",
            f"Upstream entry:   {src['upstream_url']}",
            f"Upstream author:  {__manifest__['author']}",
            "",
            "RAR indexes this capability and implements its method; the "
            "upstream library remains the authority for its own instructions. "
            "Open the link above to get those from the source.",
        ]
        return lines

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if op == "describe":
            return "\n".join(self._provenance())

        if op == "checklist":
            return "\n".join([self._header(subject), ""] + self._checklist())

        if op == "plan":
            return "\n".join(self._plan(subject, kwargs))

        if op == "run":
            lines = self._plan(subject, kwargs)
            lines += [""] + self._checklist()
            lines += ["", f"Deliverable: {_SPEC['deliverable']}"]
            lines += ["", f"Source: {__manifest__['source']['upstream_url']}"]
            return "\n".join(lines)

        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )


if __name__ == "__main__":
    print(SpendMoreTimeWithFriendsAndFamily().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916a5eiSLruX+HkrHWqesxKuQs5a9baKKIogiKK0tUri0twkftd6N3//QRqZlVPT+89s9f5tK2qTIGIN97r87wR1K9PZl35afH0+sQ5ASKBwErboOqfnp8cUNpFkFVBmsCnuh9EAOnS+lMBkLSukNSFf93ABs9Ia1a2D0rERLwirTPE9s0KMRMH/itbUJRIXoNykFMibpHGg5QCiVLbjJAwSdsIOB5AnNQukc92BMwi6pDYLELgIJz4xQMJKMwKOD89wzkeXCXpKj9IPCSoENtMPlWPZRA3hVLhyOL5tngGx5TDWkiaIBow4xIJXDipREpQQS0DeJ3YaZxFoAIv0GBwNYeL8un151+enwL4/en11yc7Mkt462mfgcTZpAXQghjoQeULRQDvlFziCGYcRB2UEJmJB4dmUEHotOenDBRQqRjecoCLPK4+lyByn5G//jVszcIrf3r9miCPz9en4Y9aJ0jlA6RKzRLaDY3MTCuIgqp7QbioNbsSKaAFRTJ4vKwKaOfLfeZ3SWmG/H149vm+yIsHqs9fn9JscCUMxNennxDora9PRT18fxmkZJ9/eolS6MjPP32XU9bWBdjVIAxq/fL2uH6IhQO/D4XOHVb9O5R6Tx0LfH36wbjhc9d7sBPOfHq5pEHy+S44K9IGJGZig88//ZlYmGR2GAVl9S/J/fku2AemA216KA6TaHDUL8joYdCHzD9fNoNh/XcsgcPfl3tGHo76M9k3//+D6ChIYDG9e/yfivtnE0Z/R37+U9v+qwnPiPv1iQdR0MDssCLwivz6tt/OZz9/cr7f/PTLb1D0fytmD0vbvkl4i80kcGHdv739/Km83f70y8+f6gzmGizGt7qI/pnMf+bX2zq/8+Bj1Offz4XrH5IBURLkI9ORX9Ps/xS/vSBHMwqc7/fLV+THehk+I2Qw4n3Ruwt+qJkS6vqDH396+g2CRAKtqe3bY1jlf/kLsgnsIi1Tt0L29gCTMMAVBIxBec2HkKM9ivrbfi1K0kvsfBuAaCh3CBFmHVXIojCDCIH1MER8sAAi7bf/sM3qiwmxsPpShkEUleNywKO3GALS27DAG0Rt/829Y9IbxL8394ZK314QzYfLp0XgBQlEXJXbbpGbpGHhW4qUdfylGdaGegV37FFn4oA7ZR2BvyHf/sW13m5iX7JusOlrAoNkwsg5SAXiLC3MAg5BzAG0rK4CXyDcQmAp0iiyTDtEhh919jI4SvdB8nAfBHgEXIFdV+DBGC7kofIZZkCZRg0EycGpN5cgTlBAj6VFd4N/6PjXQdi3b98ss/S/JndUJpA7q5VjOOBDYeTLl6wAbhR4fvU1AbafIp9+/e0T8p/IfzXrJnxYYwsp4uY2mNkRstorMgLLtI7hsIFkYMBN5xbGX3+7x2PQDtIaAosrcANwmwylfc+JG3vegvQeIWjzoOJAp7eVfu83pL3xM6REcIUFXz5/TQYRKRxatEEJ3p14n3x3/XvI7+sMMSkfPoRxuhH1MPaWjkMw7bRwXhDRRT48Bc2Fca2GiPppWcEMHvIEJHYHZ5rV9xAmaYWUsIhKt3tG6hKaOkj+ZkHRg3Pit6Fj+IZsZltIemkEfwwOui0PZ6dJMAT+kbP321BI8Qnm2PRdxAsiA+hNJDMLM/MLswS3ca55zwhIdu/zoXATSUCLDAwPhhjdyvuWeTeSRwaWRwaaRwaeRx5Ej/xf5E70yNcaRzES+d/eEg0O4RYLdb7gtDmPzGVNPd+z106TanDmvXeEjcltoVspfm9W3nHtHfG/JlEAI150f7uPdG8Jex9zR9G6gPapnHqTP0DH3YCggmk3GFYUQ6mYX5N3aoFWDSVUDigJnTe4B0b3fcHh6bumPoSA4fp7m4HcM3rwC6wVJKutKLARFwDnVlaVXwxF+wg1zEEwhBdWme3/zioESof5BeUPPh1cCenn5jo5vcfkFt+P4cHQvEEtnNqG2sLqBC8wkcwbUZSIBWAHNoyBXvh0E4XEAPoYqvjh4dI3s7syaRG+K2gOsUhjGOofI/B4+JEv36saSjUds4K+bGEQYNFe75H90PMRK6hsPFTYbdLvw/2wFfmRA/82VDbU8Tu/mFE0tA8/OAfSQRGXt3yExB6WEDtgpd3Ng5lw6xRe7mR/7yY+dHlFZpyGcDfZ+xsLIp/jd769UfPh91F5RfyqysrX8fhj2IsHS7q2XoJ0/AdK/cuN574MPPdl4LkvA899efDcF6jwlzvP/W6lu1Nekd9tn3434pGhrwj2gr6gwyMJYsSQgo/PK1InDyZwkM8/fH/E7xYf4DxD1BogDubPkKylDwFg8JMKvgf4kQUDYELIsLoP3nofAsnLK4A3DL7zWDnQXwsZ9yb7xkMfSfAoEQheiTeQbpn+ULpDAG/QcQ/SO8zDR8lAIM7QOXq3jVU0mFuCp9ekjqLnp8SMwb+4oRrQHKYqdOCwFYNlA5uxKgC3q4/GbLj4x80qLCiIBE76OtQVZE7YRD8jH/3wM/K+Q7nt+5IabtF+HnrxYUk4FP76GPuxE7bAE9wWVl02KH/fdg0t4KM1/6MSQzlBjW0w9AbpR30OK/5BCPzieaD4oxDl9sWMHiBRVubAtxDmH6lRQj0d2KQ9IzB8sCxgFUFwrOGEPy4D1ylAXkOGdwZzv/vvu1np3Zbfbm6o7nvXX5/ewWL4fm837qkzyP43O8PBs++M/jbIN29Shvq7OfrWAr9BI4OBuX945A1tyNs9IZ9eIeCA56fBnUUA+/r+tml/uisFrfnePEMJEDq+lEMnMob1ByXB/iAbLAlhWf2wwHA7cG7jhy+vf9Jx//fo8Eqhrs3iBOWyDKAchsEtCwU0RjMExjgoRbvoBMNo1KIdHDVxjHAJHJtMcMICE4YmzUHHIayx+VBmjA0BgWZ8eP1/vBt4usuBFIJT9HAsARWhWIulXAvHWQwnWIbEcIuaEC7FAJvCLZZEHdt1MZSakC7UEjioSVqkBRgWd6xB3qMRvSv39t70v8fojg5vsKmIg0F1G9IrTWCoa7q0jZvmhMBcYuJQjO0CBrA4ZhI0ijI3J9ynPuI0hPFu/5DIsAeFHWAzrPPrI+5DctIkHLkkS5G7f2ZjFjNpcnKp/NOooB1PMGf4HKv7GvdHmFxmZEzhaHvsdHDdLK47bUfPQzw2loJ/3C9yZrKYcdtw727C8W6yWuoYS4nzsTFfeLi6UC4ts5VHlCs664VoTY/7eH1Z4lG14E92MD5XE8ksVcck88h38V0zEiaxOrb6Sz+6WoTdCaMupb0oPB7Ra2Uvt2puBL1HM/vEnW02NK5Xh2hPAObsd2ugz5Wd3+C7Dtusjkcfn5vFVk9USbCzno2qdEdTnWTOjH2KWasi9uKqrIFLH2O1ZE/rq3A+7ZqpZFgiiemj6365rh1JMjbHoI+uptbhk5nsRYZIF4nTiPtNauHndRVg5LLhKc6UeF4JvOywd68gwzNA5fPdYboumya5sGOxObLudou7SlNg4/Eal04KI+yPx33QTimsOsrmMQQTfte2uNSHgd1nC5fORaE7ZZV0Xtt+BFuZ0TbRZwti7QikwCVHE7vWAigwymKPrU4kmaGCNkoOKc9lLYpv5ZlVc5NEvDitsW1FLVZOgpI5l4rG2YAicWPpUo5JnOOZQEeenqvr+dU3PMXB4G7qYJ01cZ5NQBsYaTfr5/4+nben4tyddoTCjXgjQUMCqJKdz2lhyRsYk/rnowDTSNhL1nR8zEFrdwANptxoxkWO2Ir70Cz5DvDknK7Fye7IxK1enRlciRhyn+mjyjR6phifuWrEYqBSFn6vzArxTCfNYj1tHbKxL/MF6YQmxSynqFWTp3TZXafARdelk0xVmiflYoExe4zGacWmtHZaUtfFApdLa0F0lLQgZbxLwogv9XDuHrKrml4EwjhhFR/VvUFneVUoZqFTSbIX96wmHToz2sridrQVd5RU5XWOBm0jRXlmis2mMGQxT+vDsa0Kyl6dT6rtLuyiu6qU0eTBjjqXvDG1rWh0kHSpOeN831gjjSn1faFJYuMf2gPWdIk0ml1s2Jyr5ChQiUu/OqRT1WjGBpPk3GXVie1Srrb2xNMNde7EtrCTtutjmq5LVNmr5LxA9WV+cJywULYSH3YhnhnH2gzm54Ry8kaIUvUCcE+LDs68XM5M0gXe1SESzsy0Uj3GfDil6UPs4U7hpXPBXx81gRfIo2BZykpWK+9Ii7mfzG1DOdt2W+MnjFu1pBzUM+CjpW5GtM6nGwle2vXYFoi2ZpLTFfcyTljPTO7siekqnQY8xm06XFyim13BFGRyOozFEUP02irtIJqSOAj4PKknOn9xlfLkj4matdDp1TtMwCJVaZLS11aLASLszL2gCcaGjGEnlJxGM0NfYAF1jWh0SrVlc849yTqvEzzc7vdrVjAs2bQMMgXmoT/wTCqVM2XRtc2kJvDmuutwbCPN00kZHJxdeW7Ptb2ja48aCYmwPJ9mmt05VrgD1WKLr2t8gWolYJmcDNuAN4tm7o7FKYblC94pzz11SaqM8QLAlhcMFU/oojhgxP5cOoLXzFUilbBjH2uxs+/69mLw0sHbF91CVzTeNif8cs1VXCxTLKCFZlsnhrJdWbh5keTUDorzarMmmxWpFqejEhajtNxaR5mnJe1INXtnsxQqvFcSWt6oYzbysIkAjteCXp1To13XE2E02RTk4rwgwc5dCX1LuGC2EA8gD+v+OqfI0EULMu3HvcboyakW+PlkeSiPy8060Cgiay/i9bjcHkzK6EahXB2C3oquheoK6nWUbWiFzWdGHGKZxlBzYb7fXKKAopmT4uGpvia3BkfNIx5P8NUMYMVxSuDzXI+lau1gpGMfQGesY12REuGIGdFhwolbaaFQZ4jhs3BDspi2PkzGvFbr6FRzRA6jSE015maUOsKhnRd0QK/8DsMYqeghaV1QaSpNi1MoZSjFKhlrgEqXz4s8FLc7deqxjrjGz1Kp4Hpz5GeUROk1Lo/T8IAfd9J1BUvDd3UVk0oePeUB3a2ogj9mnqzFW6etdcnpDFziyCg9zgHVmqE+4qb86kpc1r2+d6QxNRXVqZRm7t5FKVfeeQE6mZHiaaUeAr8JZj56XW7nLNVXWoQflWKVe6Ot1eR4te39+TZdhx4lTAk/O9Kj9JwuJH4Pziy5Cu1yDK66YbsCaUszQautautWM02OzuuzOM20ddGXOj+2SD/zokgk0nJ03KhekLSjlY/jQAgLXPaaS465cqLON/Fpva2PpbPXVlOf15W4iDWpNKKdzl+XcSla0YlzNuqGI0KU7FYYiOWz0GgOIxLroMtOUn4O0OYwPfrMZpf11WhFx9TuuvZE4qL6/pLLZBSjzqimaiq/jRzM8PUyVsa8vGG8yUXO3KvchMu2Ds6RFzLETNpzjExpSc8niyBTVlOcKiNYTb0YNlaaqEeGUpv5NHFcz5x3c43knKM10zANIvXaR4GxFxMrBEuRHlX7BeYHJ+LE+MnxEKihjZ5JtygjIl3yUt4WYy0y8iMnXwgVz3zxwq6Io6HscVJK+tliXMFMJGq8jf1osfYv3M6VZkoSSMfgapwPipOfU3YmzEiVzb0IY1QVFcokCycjyVmvL7Er5ZWszPGdJhLnxO3S/Yixut1qMmlt3MM58TznOStwgsM54ZVWmqvK3NsZhI2CM2dOjPawQt19NhPS2JB6Tyvnunzs9mu/3qgSumTnq04SlPFF3xVJrtcjdBeRacw3Us5ZG2u1O3XHYjfdBu4soje41/d7u+yIbgn8fVaOhUgNqtrbb/LjRgxlIF7SvNYSc+qQF0vP7YDNxeKca4dZdFh01bzVFOGixyDlBFVIeDJZ9St0ogEMVf2lo7rMsZnm0DZ2ce1RhsyJxdEPqcMo5qb9Sp13EddD3pXyzdoCZxzMe3ui7JbBxiD3vka7W3VXRJYzhW10G05YqZJNt+Z6G3qX2Oak7+CnOD0Bz4oJj6fjxU4Fqh+NpoZzOQtjntueQkYr85k0q/wjdqZENGPm0yJAGVqX5UtGpZVerVd5YHBLnlNLbo7ORQot1Jko0NYB9+LZ3KXa7MIZBC5LTJtG5y67OuloMXO80KusnSKyJ2562sTpIdjjVO0sjyjFnMsDpaGqgp7IuLI9XV2oAayI/iLkHdxB4Gq+US/7M7qoeMaVzvnmAlzNKhWaLWO1mi5C0ITM5Lysa0qRzYOPmht8IScUq3fa5HKK3FABjezO9u4MPyXomFY0mZOvedKy7oWxTuNsym5gj7PMGbtf0xffwgiS0HE1Fk1scW69idbkxgmy4bnslSVz5NaciNu5TEqOw5xMrCIABlNTMnXxMm+rtSEl18X4OpmY8x6LtHaBcgEtgfFkvScIdaS213IDqPWYDKkJ3goZldOTZBbQjoMH/cbaGv21VEfcpm/CyieBx0bWyOEEgyOu9L41p1IuNfqi7b3V9kqMR/TBZbylFa1g+1nz7FjoR2y1NVMwgkzIzFJjWWSaoeHC5bBFWQ5lJfF8DFdGtDTymYOVxmnMBytlIU6o0XWsmHtP5uK+iOb2Pjnw4QVs5FbwF4A67XB9dias+tRNIfMRQnqaxGgLLkF67JvppuXzvj5Uk2uU0D1nUBW92xhNK+GXBUudLwTZrtkm9+Nd3jWkdXE1xy8ZX5+MDzxXMTUYeZbBuZaMjzFZoLKNrEpOsRlRBE54+4pfRW1zHZFBaVcSFq9Q+pKYp6uJjeRxQJKkyhgrs1X3YOgJ/OtxPFs4F6JPqCSrU8fDVGW0Kc+eph/7c6/TLdvVlZb1OTX11o008pwrGir9SMZHO83yp5rXs31uWH6cTGaWZl/O2wMV7sx1M4WtgZJcJCZyZZbzBAPfl9sm3JWnKjge6SZZVqPpCE8Zw1C1JZrqG1pCyzNgW3oTshfJVMCquhJJtZwB8xhYzFS/8vk4Z4qGhrmbaLSY2gW7W6JBuLIatnMCfHo1wUE31pt5sqssO9b5fXfWUEXQq/GWXpiTixWvhMloFXWRM2Phbq6jSstcEjvMKsfNYdTDzsoINF52Czea4REtJuM5SGZrxr+Mp0QEGs3m8MW2CN1i1aDBrjomSuLsN7zbgKVjKftyc+ZcLb4uZr3rlyO6iC1iqUum6JzsxWYG2dSocI5QJinv8DxK1CdZdggOZ81NtZtQxTrKFWtnzgiJGc3BUeHaykVFYw73ZodE9dTdNrTGx2J9rsIsLkccG0BqzDO3JiktQmN6CZgdvyvqyYGxphp1lht2XuH4id2zGFHAGbUlqK50STK0WUapi26diNW1TbKkL1WyS+WCqOmRJbuq07NYtJlQ3vXKE+NLxq7SQmGsdmGd0NhRr/42XDqHg8opYB0o9KKXxqGrlscVpl9WZl3v69Ec7tYmS4dHUa5dH3z2NO5JklIWgRBXtRuSDhNTnTdmTOlqXaZ4NDkfvMspkGeRDpiUAz5hMBwnL9Q2Dk5TXNyMbbKayZpmsVW3OGnWuDH2bOXIjXwWQ3Oe6QJKXA8j2EnOTj4OkuPpxKYaQWvNdilwuiW6rbMWqo1iE3Cj3XknwzpclGCDQ1BIt9sKEItMt7HG0LGEJySlvyirpmPq0bacJeMx6W8Fw8UUHkzGuhAoJiVLGJPQ1aariBE2zSfjZN0x7VJ1l15BJxCaZX1pNt2FTefrbMxE15g4Kf1S1m330rSwFdf4CjgNPp2LSpj7XDpxbXJ5SlRRt/fXKYONFhk+GtNGDHEpI3QKo41VITTtKbH4yzQmI47j/v70/HR7efj0ylIM/vw0nA4/znj/B8eDXh9kbw95BEFOnp/+/51W3U+O3t8A3c58gem83lZ//bd1/eX5qbADqNf9XLGMau9xTvWPx3Nf/sWjw0FKd38hOry3ulbvR+aV6d1POB/H+7f/XVQNL/Dg77Su3lL37f7qEV5/vEAcNHy8fICK4cPbh6ff/h/zFAQ28iUAAA== -->
