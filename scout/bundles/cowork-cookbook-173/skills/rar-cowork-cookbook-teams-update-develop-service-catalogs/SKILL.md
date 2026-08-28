---
name: "rar-cowork-cookbook-teams-update-develop-service-catalogs"
description: "Drafts a Teams channel post on develop service catalogs status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_service_catalogs", "rar_sha256": "4d71688f91a7057d6e04d456cfede9379247f440952ab3768d668db3212f8d44", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_develop_service_catalogs`. The original RAPP
agent is preserved byte-for-byte in `teams_update_develop_service_catalogs_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

Develop service catalogs Teams Channel Update — Drafts a Teams channel post on develop service catalogs status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-service-catalogs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_service_catalogs_agent.py` and embedded as the fenced Python below (sha256 4d71688f91a7057d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_service_catalogs_agent.py` first:

```bash
python3 teams_update_develop_service_catalogs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_develop_service_catalogs_agent.py   # or on stdin
python3 teams_update_develop_service_catalogs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop service catalogs Teams Channel Update — Drafts a Teams channel post on develop service catalogs status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-service-catalogs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_develop_service_catalogs',
    "version": '2.0.1',
    "display_name": 'Develop service catalogs Teams Channel Update',
    "description": 'Drafts a Teams channel post on develop service catalogs status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'teams-update-develop-service-catalogs',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-develop-service-catalogs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '868d68191755aec1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/develop-service-catalogs'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/teams-update-develop-service-catalogs', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateDevelopServiceCatalogs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDevelopServiceCatalogs'
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
    print(TeamsUpdateDevelopServiceCatalogs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716eZOjxrbnV2Hq/dHtp+4SYhV940YMIAmhhU1swu1os++LWCTA4+8+iaSqbj9fv7memBiqVMWSefbzOycT/fZid21U1i9fXk6+XUCcnWVx5NeQXXgQW97KOgX/ytQBH8gti7aOna4t6+bl04vnN24dV21cFmD6qraDtoFsSPXtvIHcyC4KP4OqsmmhsoA8/+pnZQU1fn2NXR9y7dbOyrCBmtZuuwa6xW0EmEJx0fq17bbx1Ydoz67uJ6xde1BQ1tCli90UAkLYof8KRPB7O68yv3n58vMvn15icP7y5bcXN7MbcOvlLolWeXbrrx7sTw/u7JM5oJDZRQiGVgOwQgGuK78GjHJwy/MD6Hn1sfGz4BP0n/+Z3uw6bH768rWAnsfXl+lH6QqojXyoLe2m9T2gXWU7cRa3wytEZzd7aKDab7u6mAzUAPmL8PUx8zslYJx/Ts8+Ppi8hn778etLCUSwJxN/ffkJAhb4+lJ30/nrRKX6+NNrVt78+uNP3+k0nZP4bjsRA1K/fnteP8mCgd+HxsGd6z8B1YczHf/ryw/KTcdD7klPMPPlNSnj4uODcFWXV7+wC9f/+NNfkXUj302zuGn/Lbo/PwhHvu0BnZ6C//TpbuRfoNlToXeaf822Am79O5qA4W/sPkFPQ/0V7bv9/wvpLC785t3i/5Lcv5ow+yf081/q9t9N+AQFX19WfgaSo7adzP8C/fbtJK3Znz94329++OV3QPr/SOZUdrV7p/Att4s48Jv227efPzT32x9++flDV4FYA6n0rauzf0XzX9n1zucPFnyO+vjHuYC/VqRFeSug90iHfiur/1H//grpdhZ73+83X6Af82U6ZtCkxBvThwl+yJkGyPqDHX96+R2ARAG06dz7Y5Dl//Ef0DF267IpgxY6uWXXQsDBbZz7k/BqFDcQ+J1yuwYQUjcxMOxzHIj/ycOTxGUA/fo/3TtcfnafcDlvJ/j51t3x59sT/7498e/bG/79+gqpgHhZx2Fc2Bmk0JL0tQDwVrQT46r2pxkAUpyh9T8DMPo8nQCYhH79t+h/u5N6rYZf75AeP3BKYfkJo5ou818nPY3IL55auQCE/d53O8AlK10gUhADhP0E9G/KDIBxO9mkSeMsg7y4BgYo6+FOG9jty0Ts119/dewm+lo8QBWFHmWimYMB7+JAnz8D3YIsDqP2a+G7UQl9+O33D9D/gv67WXfiEw8JIPzTK0DC3UkUIJBlXQ6GAYcBFwMIuXvlt9+fFgZkClDXgA/jIPYfk0GUpr73Zu7Tlv6M4ATk+MDMwMR5VdYtQGoobl8hPoDe5QVMp0cTlkdTefP8yi88v3AHQNUG6rxbsihbqAGh2ATDJ6hr/DvXX53avouYg3S321+hIyuBylFm4M8k5n0QmFwWMTD/ezA87gMi9YcGYt5IvELCFJdQZdd2FdX2k0dgP/wCKsbbdEDchgr/9rWY6qQ/meqeJA/zgEHAMu7TpZ8nn4N6nwNE8Jo33vcx9lTf1Hudq78WzTMB7HpyhQsKAmAadrE3lYV/PEOqicou8+72A5JOlJ5e8J5eucfg6q86hEdDwT4bikc9h752CLzAoP//XcckKs1xypqj1fUKWguqcn6YcGqPJlM/OipQ+++T7+nyvR94Q5M3UP1aZDGIh3r4x2Pk3fDPMQ+g6mpgJ4VW7vSB14EJJ7r3oJyCrK6ncLa/Fm/o/QmY4w5VwAAgg0GET4H1xnB6+iZpBNJ0uv5eye9OBGoDt4PAg6rOyUBQBL7vOfZkg6ieEutpfBCh/pRktyh2oz9oBQHqIBAA/ckLMfAQQPi76YQSqAlyKqjL/PvweOqPgBRe5wJpQf/pv0IGyI0pPhqQkKDJmcYAK3y4k4JyH9gYiPhu4Sayq4cwU8v6FNCefFHmU7z84IHnw+/RfJdlEh9QtUF0AVveJoj1/P7h2Xc5n74CwuZT/t0n/dHdT12hH8vMP74WdxnfUR2kdTZV6B+MA4EABAE84eiESg1Altx/BhCIhHsxfn3U00fBfpfly5/69I9/r5W/V0jtj577AkVtWzVf5vNHVXsraq8AE+YgRuLKbx4F7vOjAH1+ptrnZ6p9fku1PxB/2OoL9PcE/AOJZ2R/gRav8Cs8PToAdlPoPg9gD/Yzc/6MTU+/For/3dHPaJhgNRtARX2vMW9DQKEJaz+cBj9qTjOVqhuojneQBa74WrwHwzNVJswJpwLZlD+k8L3YAtc+PPdeC8CjogW8valJe6xhskn8xn/5UnRZ9umlsHP/31y7TJgPQhYYZFr1gPQBfU8b+/er9x5ouvjjSu2eWAARvPLLlF+foKlf/QS9t56foLfFwH2JVXRgNfTz1PZOLMFQ8O997Psy0PFfwAqsHapJ+McKZ+q2nl3wn4WY0gpI7PpTHS/f83Ti+Cci4CQM/frPRMT7iZ09wQKA+lSV4/YtxRsgpwd6nE8QMCFIPZBNACQ7MOHPbACf2gdID9B2Uve7/b6rVT50+f1uhvaxTPzt5Q00nj54toRgOMjOz81UAOcgVAFDcP0IKvDs/65ZfBIBWAf6FEAF88gFsVwG1MImYZz0CB/GPAwn3MD3fAolKQQjAwyDKRyxHZQklh4BPg6KLJBg6WEYoPeIz29TqY8nwXw48FFqgbgeSiA4jlELErEpz8ZI2/bg5ZKEycAD5eD71BQA5VPbh3aTKd/71skqT6V/e3EIDIzcYg1PPw52Tuk2gZCOEjmzmvDPlknxTmxcCIMgTcOgLmKDITIjcG1SbUqtbtbCsFsvBFcJRVvzak6MVhRdkDup87qAzhEtJxBasyt+IYzVDV/MqKVFyCG7tqT+YPL6kYP3eyrjs4Td40TVGvaV8aiLV9eRf8IGKkOUZXq5oSiJZypczez6lBwaPdZbZb+B+8yRYKnkCCwzWuSMNEI5Fqpo6/ttdhqMK6NmOz9nKNG38iE71Va+KHOduF12+uzgrmTCD5xmLo7W4HfjbjY2uH8dt/AB8UNJYZPDEF85ArlEJz3pxtarePuoHbZNdyw6DmXLay1nbiYweHaMcbwz22ZD4Onuejsd9rF6ifHN0ODSWC6wQyEoXM0NbFuMbHk4aOHlLFH1YO6JdX2xbr2jle1Z7XPt0jWH9jSaW3jRdThmVqtr72dddMbHGedpsbzfXY/Lrb/Bt4Y7nE9NBFexOlNa/sSjqotrhypzGisWVdVd+kxTZEl+UqlBi0sEHzpxyMICxfPLYt8asHmjdidMGmD1siqUSo4tgbr6R3Mvtm6jdEpn0+hx27eMw15DBFU1cWNdfW690HxD186IOqcMA75IiWdexk1B+8XFM1iPt7EkHOIz1WGSttwYVLtjrpS5ZUOcAciCbKuI8qxYgBFwjwyS29DFGxPjNHV+GpOjfHD8Uo4QnG3dlSoO+yWMEHHrSjk77DtCZROFOzQ3abT3ByGujhfb3xeajo1LpFMYHkVcTG52c6Xb3VjZWGarrat1ZTJIQ7clmg2yUPRSCUbf4JFdjgf5Pmm3TBqxxLbY6KZZr6yFgAobwQSfQNgsLL1FHSXcEpavY4cDFurkZovZQVmi6IxuhuyAMiSGFSZK3Wa3q79KCcAEM+Udv7x2Yq92ebrgjcwiyZ2yCWq466vGUGKLF+MeOXE21e95PVzsT/T+VrCZY8ra8pRrRJauUlNjwoEZC0E/nhemfzYSDWP40zlUaKHiNF+pBb4+H53GSxWOUROLr/MVE1a82btDecSCzc07zcZ5ZmAiiu37zs3PMzHRopTv93i8lju+4qRBiHaug6WyNWdybL5cLtQL34nksJsPcpA4LLM1bj5Bz8dl7MN6M1ZrcYtbi6CYbxb9hTwsAzqM6h6FddtSTUuwiMHV+/q2nxtrma5vzhxeraguxqoZUdqr4OorF+bEpot1DG+EZLGxU/iCxCjl8SfTW3fpMbT2+0RC571/UvfnuofzZrM7X9D91isMxBPK+cXJo62g7M5GvyUMsjaPy6Xc7unzTJdTN74OZzWD0YYNt+HQC/DaLP1grVciP8OzMm8Tl27n55iyo2ozbPHBPCn7nXuJZ2GxCKWyjPuDTamdeyFW26rG5YNGnjf1TlZrpNNJa5MwQn7EFc4NTcXkLMPKxsNhpe/0Y6VvnHJ/bLQtbiw2iNaXbDRKJu4v8oNzJaWKr1pLudqlTRLzsVI3fEkfa2LcJ5E8C23TVyl4ljZoJcwo7HAOqb0vBcz2pibMcl7yfMJgMyJOeMYyBgo/rchbkat8pt60tD8J3JrLeZ6k7JStuLWUdh5HlSeUTylBpa6atOL985Diml0fij6QzNLY7K8ZaAwSXPUdy+HFGX24lRtaxE9Otm7msJ0sRTSIRU7v5eP5ZOQ7UzJ3l13XoaYyDPBxmcpMZGuyEuxTe1zfdHHgl4urdKRDI83WSSwdkfXqUoRXG+GxQ6jeVGO9OHC7grZPtYLIo0aRqYVu83NdWOJ1mc/8whqW1zENU3Znnta10wUVpdGIs6zdWvfSORu6t7icebMgiEemWnkewI3oVuxTdjafrQ4U1rTbAL3Ci+Vyjg+Hvnajlo3qUlCvgR6fs3BzuPG4NrbbYn8cYP4g6peddSToZdhS1XqBzeJR6taxfdDDw3JjLw3L0XtVi1fqNWZbOar2hnAKl/Stllhea2FGyhVCP2UKriZzRteI3GLmUWYN20VaXI3x7G8YtNmhKMCeoR1seXfIFRXXE9qXjzZm6oeWzY64Y3qXoU7Cxdnyt97qIjlr5paclhVBpVnFbdrZcU3rktP46cWhb9vedW4a1a3W7axCDonZXxZK4rlXZxm4MOeqtHUzSltM7Y2vE0abwq7AdFU3MLDCa9dMoGLMOsGhhRBD76c+wKlE77l26RZUyoT6rbpVjbVvpFGjdWburlpDkSw7r43z/tjy41w9gZx0t/yGW6UzZOOecXqVL2+7fa2ckSPBX0d3fcCzm6nonqrvcHnHzmhH241cI6tz27WcUUwxRI3QSrY39mY8MvyBKInsXAuS3NkN1qx5Rj+islrsGsJJ3LpkeezShxsxzdeMsls5rCob6Ipd5jv/rMehWhwX61E5lDUS+MJJ7hAnMtAAdA77m5lW9kV3zXAOW+Zl4PuCvCo2fYpYUjLlPZwQ/QK5dSdE48zN9WJtQSVJdwKWl5fkzMKDnrsrFyAM4x7n+3Ur8qkhr2ADPwtcrMeRceDDwt+sNfXg8Dpdqp2EoPLcjrwTCtJQC2tZDKpijpiq3mBOHgiwG+YqodGaHOEicRardF5rGWwq2nmUUrOcoTP/urVMRrZKuC619dYLlcJZ7Xb7RBgESUSE2/UoGTWBa1119cY1rPFEqxLmQAqDO47Hgl877JjNEI+OxXMUlrIQJfnoxW3k0IO66s+XaNfIiHtUqO3mQgpqXqrclVb1JZFkOOoDex3pw5nwy9MYJVqpWXv8yMi7K7loZa1Cm9oUiHqe7a3VCdNJByjvUWyJMdGwoYR5b4e1qpxC2RMtZKCLTIAvHocdy06xdklgO5cFHWKyvGjYXk5Qmwi3m10VRLurZolImxfuDkc2qLbqzc0WP86ac4P32lXc2mvuKJNYzy0Src+akog7L1wub4u0XdE70GvshA28jFbYhtTmLNWm2y1Y+h/VPKpGbKZ4W8TgLo3CiSYmZuqyOOcmlzW9pHJ2wid5X+xjRxbwPWyK7rLpyShxyNNQ4Lw1K1dRwKzYUpOQrLjhZqoidN8dEVHiTkxyVhv2QHFblZMULxjGE1sOI8G2mUaihopvx3Uh7rMaqa2M9X27S+WVb2kmPBrneHXR3GLFw8Igi2yjXrb6YZSlI6yWVQwvKlBjFGGY1zRXcvk1B/ULL05+u/awJmTdS+8FGM7rPSqQ5pY/wSbKiaqeL3aGzpxKg1qnM0YtC+NEOxKzRULSD4vSvCSrBbxgjgI9szTWUPiGUolCrAuvCCVhr/UXrll52e5auZfOqAbGOEarRFx36sHU1f32RgSpusNSynHEeG1YzWJ+2y/XPJ4tcKHWqzrtsFrbBdmJsNaitedzo+T2EdV7CubRMNfPVvvEybmbcVyWfUy4RckGoThcqUt9XsyWLHo1st1UxULeQSMj8kfWPKYwt0Dma2TZz7ky3kns7RDQsKSHLJmXyopPOuKmeDlZ12xVeYTu7qPYFYT2yi/rSNOHA1pyMsuEAkVzArN2cbo6m4xNHFlcHnFxI+FGJS5mc3NjlzJR9kFIKxEcKe35vGrzuYBx3Y5XtEbmlqToRYpgGgzHcdYar5KwqZ1NJtdrZjOfHY360BYza+gpbNVpXcLCja72C7U4yN4CJA9Px0teuO4qGJZaAfGOR1Miz0eE25V1ywtC14pad1vg8zUm9IRE+le9rXGJFMmIm9Xq3C/Y3aJGi242zE0aR6mcFJmoIUnMIVfr836zNzvTbGCSyHW4MuJjvhara1OvtytN5fRrYOBOw5COazdgbbC7lszJSu1yYwV7zWbnMxReYdk2pYVb2iyLmjxbq6tILjMmtI/GLAm0WcDoNX29+LDo47uZQ7qYK6w8WpkBGQMN3TeLbYRxDSmNdYryXNMUCrK+wgbaUZa0sEXlPMtn83m5n5cb2PLyGiX6eewQfmN6skeRBHGTT5k404VMOu9z3o1sZY+1VhTRVWpaVbgjj1EWNDycyvLqWpBCg19CWuMcQ1xHWboMl2XCcjdly7vGmDPjom1yHXWKMzuu6XYAyyv0DPtCsrpgaLiXdxfS3NseCARxPewR1U9HtsZEvO5rf8tnN4k2WxK/nFaUMtJLrzcxVbapDPX44CC19aWTuwWCj5SA6ed9tM3FVJoplI+xG16Bmw0soLBzSM6Us7YFavQO5NGec/PkvFzwM3ljmjsJY0AbV8zOuBkwsMegXoFu1bPize3Qc5lzT3fHWsMzoQYdZjZvxdZvl+xuWGqu63bk7pqMaLbub6rG7wOkRQ7nYzoDLUUdHjaOwZ1YZUdlYrQ9wCrqmPOiWsu8WK+2A75BeafMdNHJBuIaehUtJStbPHcb+VYwgdxH+GLFnzP8erwRWEGOQrodw6Ng98aSb51IYdC5sZ0ThOEHkbEpA4Kerdftyqs7tTFS6bAKQ5XxwvTC1FRvnUWBiUTtppfoDC23Pcqh/KmdY4O4BsDU7JZjTm6RlATL4vyEnhxxhPOiF8f9+VA0u9wcRffmz4dUrTZ+oJCxpOAOSaj1ZTY7AbXn7u5ErMWdVN/kAxoDnN2CQifIYzjrRefmWrorVLMon3dHxRJ6oSTpITRXB0tASg5HPNYqg+bSEnhFziXCTOTb4pBTx4KBEe0K453BCJJLb3ajuujrkp+hxjmX6YUhYQ1+wCtmM3grhVCIbdPNSjzwxqg7yBSmOHgoKJ209FnMvDqzdskZK9XpqmUnOYkUUAeJuWZRMaOuW6P0QR+H4PXRdpeFPicvx04Xo6lhFNB5HvYReZ2b52RVUB0dzHHFRW8Xbun0a6TB/Vl13GDJoUzU9RrB9sWprOHIXcwtcRfpMyxR4JVO9robUpFJ3igaXq/7vda6pjTHsXrYxPr1iG4xtxO12cCRpDrGqJ0Ih1yuGE5iKXYTNMvyKEYHZU6HwuYUJowqLE+W2I92GheBMyI4JSGIQS5g9MAFPcL3PDv4cICcuxGU/qTBgq0im8JRRWPzetyCXmMXipgfsTBCi1vY0nAVXQgXJZc5VxxiebtFage9aNudhx6MkLSX4WpryLqEJFdxc43JDb6ks5mxWncjWvXWyjkcMjEjuxs1Dmd5ac+URdDJhsqrSa6PeXTCxZ7cnPVgqJiLRG6OeI6Mc9BJrgrP62hMPjSYcXBmYcQnJ92NGBCFyemwjrEBLMFPeLnLrmd49ANdGDfS5eSUGNE2+kKQSsk1tohbnSuapv/58ull2o5+bir/vTfG0xbf/7Odxsem4NtrpvuGsm97X+68vvxNuX759FK7MZDqsa/aZF343ID8L7uqn/+tNxQTieHxOnZ6L9a3b1vxrR1O3yx6iQuva9p6+NaUWXff3P304nTN9BWH5ttzE/vlrl5eTTviP6ozEX8q0pbfnt/OeJm+hjC98PG9+DFmugyfG86fXrwBOCx2m28ogX/z62rS+PneAyiKvMKvi5ff/zfKvJ4OuyUAAA== -->
