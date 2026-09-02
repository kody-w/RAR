---
name: "rar-cowork-cookbook-ppt-exec-create-knowledge-base-articles"
description: "Generates an executive-ready PowerPoint deck on create knowledge base articles status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_create_knowledge_base_articles", "rar_sha256": "4c70c784753dd2e19eddc75812c046cbb60d83bf49e2e7c993f3afdc2f1698a3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_create_knowledge_base_articles_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-create-knowledge-base-articles:e07eb2d2cc3ec4765dbac475adf59e1aeca62f4d3f21b4f8b7a28233abd16291", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_create_knowledge_base_articles`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_create_knowledge_base_articles_agent.py` is
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

Create knowledge base articles Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on create knowledge base articles status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-create-knowledge-base-articles
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_create_knowledge_base_articles_agent.py` and embedded as the fenced Python below (sha256 4c70c784753dd2e1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_create_knowledge_base_articles_agent.py` first:

```bash
python3 ppt_exec_create_knowledge_base_articles_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_create_knowledge_base_articles_agent.py   # or on stdin
python3 ppt_exec_create_knowledge_base_articles_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create knowledge base articles Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on create knowledge base articles status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-create-knowledge-base-articles
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_create_knowledge_base_articles',
    "version": '2.0.0',
    "display_name": 'Create knowledge base articles Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on create knowledge base articles status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-create-knowledge-base-articles',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-create-knowledge-base-articles',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '679a940a1c11f601',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/establish-a-knowledge-base/create-knowledge-base-articles'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/ppt-exec-create-knowledge-base-articles', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecCreateKnowledgeBaseArticles(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecCreateKnowledgeBaseArticles'
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
    print(PptExecCreateKnowledgeBaseArticles().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8166XPiyLbnv6Lx+1DdTy6DdvCNGzEgQCAEEpKQQF0dLi2pBe27RL/+3ycF2FX1uu+d7hfzYXDYaMk8+/mdk5n+7cmsKz8tnl6fFGAmCGdGUeCDAjETB2HTNi1C+JWGFvxF7DSpisCqq7Qon56fHFDaRZBVQZrA6RxIQGFWoIRTEdABu66CBnwugOn0iJS2oJDSIKkQB9ghkiaIDd9UAAmTtI2A4wHEMkuAmEUV2BEkUlZmVZfPkGecRQAObIPKR2wfDihvwlVmFAaJ9zm7UU1SyPkFCgU6c5hQPr3+8uvzUwCvn15/e7Ijs4SPnqSsWkLR2Bvv7TvrOeQ8ezCGJCIz8eDYrIeGSeB9Bgo3LWL4yAEu8rj7qQSR+4z853+GrVl45c+vXxLk8fnyNPzIdYJUPkCq1Cwr4CC2mZlWEAVV/4LMotbsS6QAVV0kUB2obQF1ebnP/EYpzZB/Du9+ujN58UD105enNBsMDa3+5elnJC0gv6Ierl8GKtlPP79Eg7V/+vkbnbK2LsCuBmJQ6pe3x/2DLBz4bWjg3rj+E1K9+9cCX56+U2743OUe9IQzn14u0AM/3QlnRdqAxExs8NPP/4qs7cMIiIKy+kt0f7kT9mEYQZ0egv/8fDPyrwj6UOiD5r9mm0G3/h1N4PB3ds/Iw1D/ivbN/v+NdBQkMIzfLf6n5P5sAvpP5Jd/qdu/m/CMuF+eFiCCSVeYVgRekd/eFGnJ/vLJ+fbw06+/Q9L/VzJKWhf2jcJbbCaBC8rq7e2XT+Xt8adff/lUZzDWgBm/1UX0ZzT/zK43Pj9Y8DHqpx/nQv7HZICFBPmIdOS3NPtfxe8viGZGgfPtefmKfJ8vwwdFBiXemd5N8F3OlFDW7+z489PvECUSqE1t317DLP+P/0B2gV2kZepWiGKndYVAB1dBDAbhVT8oEfWR1F+V7UYQXmLnKwKfDukOIcKsowrhCjOIEJgPg8cHDVIX+fq/7RuifrYfiDrKsuptwMq3Oxq+faDh24CGb+9o+PUFUX3IPS0CL0jMCJFnkoSYHoDIB/neIqSs48/NwBqKFdyhR2Y3A+yUdQT+gXz9i7zebmRfsn5Q6UsCfWRCx0G8BXGWFmYRRD1iDphl9RX4DOEW4kqRRpFlQlwf/tTZy2An3QfJw3r2R0UASJTaUH43gJyeYQCUadRAjBxsWoZBFCFOUECDpUV/A3lo99eB2NevX6GQ/pfkDsoEcq885QgO+BAY+fw5K4AbBZ5ffUmA7afIp99+/4T8F/LvZt2IDzwkWCJuZoPmiRBeEfewGnl1DIeVyBAiEIJuXvzt97s/BulgzUNgbgVuAG6TIbVvITFocHfSu4egzoOIoHhw+tFuSOtDuyBBBa0F8718/pIMJFI4tGgDWB0fRrxPvpv+3eV3PoNPyocNoZ/cIo1vY2/RODjTTgvnBdm4yIeloLrQr0NRRfy0HOpzBhIHJHYPZ5rVNxfCEouUMIdKt39G6hKqOlD+akHSg3FiCFRm9RXZsRKseWkE/wwGurGHs9MkGBz/iNn7Y0ik+ARjbP5O4gXZA2hNJDMLM/OLoSEYxrnmPSJgrXufD4mbSAJaZKjwYPDRLbtvkcf++85i+d6bfN+VLIau5EuNjzES+f+hkxn0mHGcvORm6nKBLPeqfL4H3dCEDTa4922wnUBgO3LPoG8txjsaveP0lyQKoKOK/h/3ke4tzu5j7thXFzCI5Jl8oz9kfHGjG1QwWgb3F8UQ4eaX5L0gPEMHQF+VA7bBpA4HiEg/GA5v3yX1YeYO99+aA+QeiIP2MMSRrLaiwEZcAJxbNlT+YOt3d8DQAUPeweSw/R+0QiB1GBaQ/uCGAJoTFo2b6fYwZ6BJ7wnwMTwYWi4ohVPbUFqYVOAF0YcYh3FaIhaAfdMwBlrh040UEgNoYyjih4VL38zuwgyN8UNAc/BFGg8x8J0HHi+9RzA535IRUjUds4K2bKETYK51d89+yPnwFRQ2HhLjNulHdz90Rb6vXP8YEhLK+K0swF5+KPrfGQeieBHfow6W47CEKR+DRwDBSLjV95d7ib73AB+yvP5hNfDT31sw3Iru8UfPvSJ+VWXl62h0L4zvdfEF5soIxkiQgXKokZ+HLPx8z7PPH3n2ecizz+959gP5u7Vekb8n4g8kHrH9imAv45fx8EoIbDAE7+MDLcJ+np8/k8PbL4kMvrn6EQ8D4kEUtvqPwvM+BFYfrwDeMPheiMqhfrWwZN7w71ZIPsLhkSwQMRJvqJpl+l0SDzoNzr377gOn4atkqADO0Pl5YFgZRYP4JXh6Teooen5KzBj81RXRgMcwaqFFhsUUzCDYTVUBuN19dFbDzY9LwltuQVBw0tchxWDtg13wM/LR0D4j70uM28otqeEa65ehmR5YwqHw62Psx3rTAk9wYVf12SD9fd009HCP3vqPQgyZBSW2wVDd049UHTj+gQi88DxQ/JGIeLswowdeQEgfwBsW6keWl1BOB7ZZzwj0H8w+mFAQJ2s44Y9sIJ8C5DWs0c6g7jf7fVMrvevy+80M1X3x+dvTO24M1/eG4R47w1r1b/Z2g2Xfa/LbQN8cqNw6sJuhbz3sbdpQe7975Q2NxNs9Ip9eIfaA56fBnEUAG/Prbdn9dBcKavOt+4UUIIp8LodeYgQTClKCFT4bNIGlz/mOwfA4cG7jh4vXP2uZ/wocvIIxAyzcwW2bADbJ0NRQW0iGMh2XmgLMBLZJ4y7pEC6OWaQ7sRgTn+AEYVoORuNTDMoyeDU2H7KMsMEfUIsPo/9Pu/mnOxlYS3CKhnRImxnbzATKRjgODrApcByboSYYbo9J2rYseuxMCMslpwAHjD2dEi5huo6Nuxg9nZjEQO/RSN5le3tv2t89dAeHN4iqcTBIjpumPbEZjHSmjEnbgBhbhA0wHHMYAowpyGAyASSc/zH14aXBiXf1hzCGPSTs4JqBz28Prw+hSZNw5JosN7P7hx1NNZMmNlbVndAr7cz210nKA1VRo31ygBC4FYQS+CmzrqKKz/ftvp7VCsubQnUWCk7WUyqcyDzZqlOhIYUNMS62jhrb5gXvVBZdeOSqRyfduEx7z0w0k+Umy5oldCfA2wrn+aI9+ZHBp8LVZkBQHPBJmLcRmpkai2rCrGOEPS9Mq7JpGAiA/kyL4oZje4vF2GhpFE3tpa2eb7aRg6PxQgVYUsyPll3ZZ3GL7ee1bl3YuVMGZ9KNI2FvqeMwrVZrU5RpUc3GI+lK0aBZUMx1R8FvZrTRzWbf8iwb7Npg6sRpn2VO3Efb+IwfC/EYEW1mEzlHtG2M0Ud8zI2ZvtZ7sjrVqVGTYRFujlfWV0PMCc69k1CdNdGuAboyy/1ixRgBS+aBbJwZNfK1lrcUc1f2lWyeE5Xq82nH5Ze4xtK9GFDkKVs0FNBqf7MSMGG+zbh8m4vqZcROTvW5N5TSLwN9Ldo4d+WuznHrsztBC7CuNqykSM7G3GaOHh5rI/Yi5rS3i8CW7xtd2GuZZVUG34+XlTfKMSmtZU4L9gnB4dRZk4EpHPW6iEPxckFxr/L1VrCMfMGVRLNQTHOTr3rOZrYoTkm6iOlRyOi7xB7nB8xfrHc4Q9LzTBeuQoclcT+2J8x8nNXnU5FEBcWMDnGHF6FgVLYkY2eiCc6Fjo4SEcpZmtgqnq81LNXOQloJV9XIt0Q/aSUxL6LNPL+u8T6hyhUfX4+4LoG8OFIyP8KdZeFpMhkE45Dh7GiRg0Pb15S/CnP30Bsj9MqYJYl3mUxLWR058TrHJqdN4IfBITPY66RQVDZxs4C+ZCHGqUp8yQLuUldbJwVWSXZqqTTzTuJcgiSaTjp3kyHCbFCM2nmejPEpGq/peetwlDknysOYVaiTU9b6ji50OZuy3U5xffp0DjH1SJcJIduMvxC5nRlTG1letgd0e55tOy2dCYKaU2zq+MQ1P82M06qd8dlldeS43pkZeL7XWmPmRpwib/v9MjlviPM1DfdLsRp7zXZDBbBSRZFYXL02uQRG3Yhzy3PWHTYhp2N05k7CiJXC2FYpgePbhOJnIcqdSorI0pBOxN4gAqBoROzyYOmeyOawcHtfEHECbUYza7swAzJUzFpiJ3lLNCwMt1zY2WwgJ5dymRN9HJJ0Uiy6srJmBj1WN6t8O0JDQ4op4XydUtZ0nURSd9FWW55JipTFDodBmhadFvGOlIxrRSrbM4264qLplWBb2kKB6VtUrzQG+Hai6nssnuZqwJ45NilxnaMtjfAUwz8EEAN8lua3WyYFm4YL6eNs658zxWunF4aOWZ6Yb1QeM2WJyg20jcZjLXAiqSkPYXxUuZhHD9swcPK8907WaIICmTZXOwlaZGUpS0Gqaa3bFnsLbdtE4YtxWG+oC0/sMoBdF+I23fbKtpMYSuApFmhOWYSpud64V2x6qoxgfMYpdHPZJ/mKYS+um+zVRF1Q5GKHlnlGRsSBw4ijNZfSZk+roESX64nUJ5cR5qP8xHMI2l4IowM9wZchRVoGHnn5xtVZ29gFmiQqpwV/NKHP15dyX/b1uJN5ymLkCniYB1P15I52bBvYRKlxR9zLyBHoMGvrn7a1QlBH7BTW1yhYTNkgnCmzC5cLvhQSdHjx5th5t29JyV56W9VWizrl8OPetI41ulHimXleKPvtblNoZ5HOT/z6srsYySX2PP6w9bQurI/HCstaTfI7whUCLlxnmWuCucGVkiFIahJPkx5rK4NQddxyJbWcQjxOL6E+t5Wwth3XZTJ+s2unaH6ICYKf9xtBLcbCrpfc6XlWTmvxPKoOB3ndk7u6QVeOS4gSMR41hNaOasIFc9J3VgtXNSMd3S8OobcC3WZ7wKqkmdtsy+9qreCrHTl3pP3U2Y2pPplt6plsXp1QGK/yncVVC4jrmwlJk8sc+lXLF91q500M5YDPltPziVK2+mkcc+nSc6/HHGpJzYETaLJAXFbNPCy9IFeBKoXeHHeb3u5XjjpfaXNh2xbeYo3ucVzstvEVg4ibKTWQ48N4t95LledvZuRCbnKFShJnR1v2ISdyQJwx38b9LNanjVfNzfnKwKdqqJbM/LR3iU1P8Y6lT6U57yVbBUKqoU/VlFs7sJ+xWMaf+YpdEqhbhQI7j5jdJqrAEbOP1+U1Z8g+VdJRqeBLbn6cJzKat1NMJs3FkuT7MgD9OIaVwD84DhGpAZ6t0cXSJ2thJej1GHCsMde55SrZn1bN6qpaHruoVfywjNVobh8ybiWvqshfrgT8IuoTodruo9YRtpiSH2vDy/PpLjkmKyNdo9d9UKxE76ieuoYiGpkmia15qMXp7sidsm00Wyo2PqXGgXmZ6ceFuW0OHbXuRkadVcc6aLLJcsyzjIMuCgffNUqOAiXLc+1szUcpXamhfpEY3Rt7FUud9LLDMolcXDTfjuq8L+YNvV/ykhzy85WT4WtpHDPRTB5ly5meSLmXOUF2Ctf7ZR0v7DY6h5rSbfhxdghlrAi3V2+TnUZKK2WdSLnomFfORrqIx8SI8cbjKdjLeArbEbajL94Sa4HTzBZNphgY70S4JhLqlKKlepQwVzxqPf1sbemlPyfSdYPD3oFNp/ZUvab7SbJdZ9rUzWMIyQZlCL0hZpPCcnJ0YdSBt1REzwhGJt4aHDprtQ13PVBVzZ1mjW+s/FG57CN9YyrcBlW0fiSpebTgmt1WYqczDVxK4XyM0dqeTWddxurl+ejwnaFYHljb6gHFZhyDYQcgmsVYFgUL63LdEpi5eGA7b0dajQ9Bc3fRLZY+X7ILDzlRG7Q88CcryNm1tL9quqO3yyhVxAuYg/iguBXfLDWxrvo4aBeKbnkrajfRMnV69Yu1qthaUQTjYg6rW25ozhI7dteIncx4LWlSYbkKzp2t6HxKiSumPErrpOOj4yjE1hdlYvs13ytkKbShs7PO14UhNoswUoUJpxijg226eizRYbGSvY1a0pK2FwQzLbbjRHDs1dXoJGCyvcMI9ZhvZo0MfLnfrA/XctkIXXFKm8LwapbuTa3dn1cnV6zzwKRPEtkcx9KyJC5F5uxtLS3VmlpOV2OGvgpKIo3ko0rylSk3M5Qjm3O05du2PGj+gVI6MXSOo2h2tWROyUw8jkxMINbivCYPueherdLh0GxjEADiPFfS4FL4wXK/mnZR2KLVlgtTltpG6SxJ2WpJXQ8LZbMJxuvDcYWy2Ml0uZjkYVunstFV2UYJ5+gYZpP1RHSaY706RDurzPaecFlusPC8BEu+Moz4WnbGsTzvST4+04lp4ZWNk5PTiRCF9njRJTfDRSVoVMsX6opdNcVhew7Hm+UsRbeRLZjJAfaJx4vNHTmidLwJ0Mo5c6Xd3ZmfmaVb6KeqXxkUTjesfPRhX4gS0sLuxF5rjCyD9Gi+ooPxVIOd51KoSVUs092c6SeGzehxfK3mKzoQ2b3PRScyMlpFIbktLBt0iW2P6czzDR/lZu15JRxkRmyNeNXpoJiVxx2u+qdOK1TTBdfA0VrnSC5yqUnN9NSo6zm+l5TpXJ1FG6w76+lVcloSdedpRK+yJVMn3o5fc5cmLAVDWRqYwp4sbKLLOb0khJPcTDbufK5pfEfuk8sximSXp3cpm/E2bZBj2UY1m9wextujREdUyUw3olZr4gpQOimtGU3uJSLSHYvIMXF65fZgk4zAem5oBdHVaCAx3rmoOydux7pTmhzdtzGbKxFTYf1e3B8lMeqPWrSWKWkKAYAqS5NUKNpaZdd1UezzKrBGOuovLU7O1WI52Zhbwe2aTVLMZvjCXMraqpFaJjjQGKHtWNZqGwyghc26BBNWWV6ybjbFzPWsa5x1wXYNLgjMQjPPKOfvrmVhTetZsVhP6cWllq1caE50u04nE2E0qjBs1M7orXamT3gzIn33klGMRdS4a0X7UxoTdtRsCu50WOBj+QjkhKxr3uBXplOf+oVmTH2J9q8HcycdiqQCy8VpYYbyDpxHqSzPYUtFS6nIGqModNeNrvWUZolTrN31W7xoU1yce1PGE46ytNkvCCueUD4RwZWXeo7pZbSKVu74SDUFV6LcZoafG2s8c0KXrDmUpoNydwmm6Eb3dPREnM7axLczhtmM/SBrx6Gb4u3UIHDCOy/9dTBKDqeFWo0VSUe5i2sXykjgiq4Z6ZI4tnYKU6hSykebTVGeTdeVS2eBMwm1Vney0+hTp5yfu1lcFnoX7wsGP0VMyU1Pe7Zn2kloOiQTGCNXJE8qs9jDKgvzzZLOEx3e4eU5PdcTji942Gaa51MpB9PzKBHG7JRtN0tKy+jJxQn3EyVttDE5acn9+Cxco9XSRlfstZhbSodS4wXZq/jVCK6dUItli9rzttC3ScY3O1EAjXxxwQhQ1GhtgxY9wgZSCSuiZvBWOExKMZjvIpRVYB1qVGFOprt9wLGZPsIp1gcpzrMaOgq1cVjxe39NJIxfGJd6UuMbwcn2jGgq7orYdWkJPM5wJdM4T2aakrD5ZHIZ7etDd6LJS5PiNYgrjgA826/FsaN5XjGadNNL1678xZwgyVIOy9NSTxi3mgBI0LpedcLnZ7UetMzWr0KjXCUmTRUEX8TNmSvw6Yodiw7ap4LcgemBm3ALUqZm20WaCDAnWJTAu91lFnguSaGasCHNje2u05Ed9gWdJRVnLY5oTBxIIpiBpdM0Juu5rj61RkbJTnTHmEYnNambhZi0RNBeCfd0LY7SVjjtRiZ2EQidTqZYB3HvCBcjmVWi6IRZEbo3rTaYSKAj2R2F0SXxUuZak1eTjgS8bZtQBUvz7HHN/Gg6axC4cWN1/S5PiKUpBmY9la8FTYx2i8N+zosstndX6nXkbEk/xUrB6ehVcTWkSVyj4z1Z41dLmc7yAxBIWJ1UUqLX87Rr3cNZUI6bHZNlx+2a8w79CmTVhgc+kZjXiDGYlZTDJbh3iMpF6gbdJLnk87XcolIQ1PkhaUICnMXDTLc2p9bZLrPdxiY2dAEXY5l1vIjernWiMF1KEcC8cSoqRBmZi4yJFil9DXyacKi0mqztRvSWdXAtI9glKteze6b2PNbsg3Vtn5xVofYiY/VLkubI1eWgMFt2L68FK1KprM2XdDSZRFjCnHaTdbzfVXO4Pqt48SLrZbNdcIozd9h2ybjCeTuiYWQpc6HZS00U0Dup3pbUJYQoS5RTu4owSUqlmKvxxJ5ls9nsn0/PT7eD4KdXbExPJs9Pw0nBY7//f7BT7F2D7O1BkGDI8fPT/7uty/s24vu54G37H5jO643769+W9dfnp8IOoFz3LWboGe+xafnftmo//8Vd5IFIfz/cHg4zu+r99KQyvdted5A4dVkV/VuZRvVtpxvavi6Hf3Up3x7HDk83FeNsOMN4V+m2AQ91qNK32z9BvM8NkuGEDi7noFCPW+9xPPD85PTQiYFdvhE09QaKbND3cUw1bOoO51RPv/8f4qN/LNInAAA= -->
