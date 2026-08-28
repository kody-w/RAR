---
name: "rar-cowork-cookbook-turn-source-content-into-campaign-storytelling"
description: "Move from raw inputs - a research debrief transcript, customer interview, or campaign brief - to a polished storytelling deck, with iteration built into the flow instead of bolted on after."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/turn_source_content_into_campaign_storytelling", "rar_sha256": "bf8156eb5b6d3fb2f5698610e720291905310576a629c58b7fb5d475922fbb67", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "beginner", "integration", "prezi"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/turn_source_content_into_campaign_storytelling`. The original RAPP
agent is preserved byte-for-byte in `turn_source_content_into_campaign_storytelling_agent.py` and in the RCI capsule.

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

Turn source content into a campaign storytelling deck — Move from raw inputs - a research debrief transcript, customer interview, or campaign brief - to a polished storytelling deck, with iteration built into the flow instead of bolted on after.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/turn-source-content-into-campaign-storytelling
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `turn_source_content_into_campaign_storytelling_agent.py` and embedded as the fenced Python below (sha256 bf8156eb5b6d3fb2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `turn_source_content_into_campaign_storytelling_agent.py` first:

```bash
python3 turn_source_content_into_campaign_storytelling_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 turn_source_content_into_campaign_storytelling_agent.py   # or on stdin
python3 turn_source_content_into_campaign_storytelling_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Turn source content into a campaign storytelling deck — Move from raw inputs - a research debrief transcript, customer interview, or campaign brief - to a polished storytelling deck, with iteration built into the flow instead of bolted on after.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/turn-source-content-into-campaign-storytelling
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/turn_source_content_into_campaign_storytelling',
    "version": '2.0.1',
    "display_name": 'Turn source content into a campaign storytelling deck',
    "description": 'Move from raw inputs - a research debrief transcript, customer interview, or campaign brief - to a polished storytelling deck, with iteration built into the flow instead of bolted on after.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'concept_to_market', 'beginner', 'integration', 'prezi'],
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
        "upstream_slug": 'turn-source-content-into-campaign-storytelling',
        "upstream_url": 'https://coworkcookbook.com/recipes/turn-source-content-into-campaign-storytelling',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '62562f802e94aea9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'prezi', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/create-marketing-material'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/turn-source-content-into-campaign-storytelling', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.4, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TurnSourceContentIntoCampaignStorytelling(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TurnSourceContentIntoCampaignStorytelling'
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
    print(TurnSourceContentIntoCampaignStorytelling().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6a5ei2LblX6Hjfqiqa2SIICB5xhmjAVFAFAQVpPKMTB6b9/uhQt36771RIzLr1jm3u273l46qHKGy93rMtdZca2/jtxe7a8Oifvn8ogM7R9Z2mkYhqBE79xCuuBZ1An8ViQP/IW6Rt3XkdG1RNy+vLx5o3Doq26jI4fZtcQGIXxcZUttXJMrLrm2QT4iN1KABdu2GiAecOgI+0tZ2/tj5irhd0xYZ1BflLagvEbi+IkWNuHZW2lGQI48dn5C2gJLKIo2aEHgI3FP3LYCm5gEU6yavyDVqQySCMuzRHsTporQdhRZIG0K70mK0qWmB7SGFjzhF2kI5cKHtwz1v0BtwgzpT0Lx8/vUfry8RfP3y+bcXN7Ub+NHLoatzvehqF3AQBJC3IhTNPa3UfzAHSkpt+OvzS9lDYHP4vgS1X9QZ/MiDvjzf/dyA1H9F/v3fk6tdB80vn7/kyPPny8v4n9bld9Pbwm5GW127tJ0ojdr+DWHSq903ENkWmtVAZBoYlzx4e+z8Lqkokb+Pz35+KHkLQPvzl5eifKL05eWXEewvL3U3vn4bpZQ///IGwQL1z798l9N0TgzcdhQGrX77+nz/FAsXfl8a+Xetf4dSH/nhgC8vPzg3/jzsHv2EO1/e4iLKf34ILmuYRbmdu+DnX/6VWDeEAYeJ0P4fyf31ITiEgYc+PQ3/5fUO8j+QydOhD5n/Wm0Jw/pXPIHL39W9Ik+g/pXsO/7/STRMJtB8IP5Pxf2zDZO/I7/+S9/+qw2viP/lZQnS6AKzw0nBZ+S3r7rKc7/+5H3/8Kd//A5F/2/FPCpllPA1s/PIB0379euvPzX3j3/6x68/dSXMNWBnX7s6/Wcy/xmudz1/QPC56uc/7oX6j3mSF9cc+ch05Lei/B/172/IyU4j7/vnzWfkx3oZfybI6MS70gcEP9RMA239AcdfXn6HZAGJpe7c+2NY5f/2b8g2cuuiKfwW0d2iaxEY4DbKwGj8IYwaBP4/1nYNIK5NBIF9roP5P0Z4tBiy1Lf/6d4Z+JP7ZODp6O/XB4xf3QcRfR1J7us7YX79kRq/vSEHqKWooyDK7RTRGFX9ktsB3DVaUI7MXF8gtzhwxyfISp/GF5AnkW9/TdHXu8y3sv927xvRg7k0ThxZq+lS8DZ6boQgf/rpwlYDbsDtoLq0cKFtfgS593VsFkUKG0k7otQkUZoiXlRDSKCyu2yI5OdR2Ldv3xy7Cb/kD5rFkUdHaaZwwYc5yKdP0Ek/jYKw/ZIDNyyQn377/SfkP5D/atdd+KhDhdz/jBO0UNKVHQLrrsvgsubHbvLtt9+fUEMxOWxmMKqRH4HHZghQArx33HWB+YQRJOIAiDfEOiuLuh3bWNS+IaKPfNgLlY6PRnYPi6aFba4EuQdyt4dSbejOB5J50SINTM7G71+RrgF3rd+c2r6bmEECsNtvyJZTYS8p0rGV1s/eAjcXeQTh/8iKx+dQSP1Tg7DvIt6Q3ZipSGnXdhnW9lOHbz/iAnvI+/Z7n87B9Us+dlAwQnUvmwc8cBFExn2G9NMYczhUZJAjvOZd932NPXa8w73z1V/y5lkSdj2GwoUtAioNusgbG8XfninVhEWXenf8oKWjpGcUvGdU7jk49nHkkdfIM6/frf6YOf40XSBfOgydzZH/r0ec0Xtmvdb4NXPglwi/O2jnR1TecXhMgnDAQGBqPirw+9DxTlnvzP0lTyOYYnX/t8fKeyyfax5s2NVQvcZod/kwkSACo9x7no95W9djhdhf8vcW8Qr9v/MhtBmSAiyaEZN3hePTd0tDWPnj++/jwj0vam+kCJjLSNk5KcwzHwDPsWEA27AeYXnGESY9GCG6hhGM2Y9eIVA6zC0ofwQuguGFbeQO3a6AbsJQ3MP/sTwahzBohde50Fo4N4M3xIDlNqZcA2v8HpNmROGnuygkAxBjaOIHwk1olw9jxlH7aaA9xqLIYBX8GIHnw+8FcrdlNB9KtT27hVheR/r2wO0R2Q87n7GCxmZjSd83/THcT1+RH3vZ377kdxs/OgZkinQcA34AB4G5lTV3ah6JroFklYFnAoFnpb09mvZjKviw5fOfzhc//7UjyL0NH/8Yuc9I2LZl83k6fbTO9875BmlmCnMkKkFz76KfHqZ9eqbUp7GOPr3X5Kcfq+8PWh6gfUb+mqV/EPFM8c/I7A19Q8dHcuSCMYefPxAY7hN7/jQfn37JNfA94s+0GCk77WHb/uhf70tgEwtqEIyLH/2sGdvgFXbeO4HDmHzJP7LiWTOwP+TB2Hyb4odavjdyGON3snz2Gfgob6FubxwJAzCenNLR/Aa8fM67NH19ye0M/MUT09hXYA5DYMYzF6wnOG21Ebi/+5i8xjd/PHLeKw1ShFd8HgvuFRmnZEi47wPvK/J+BLkf8PIOnsF+HYftUSVcCn99rP04zzrgBZ7/2r4cnXicq8YZ7zl7/9mIsc6gxS4YZ4Xio3BHjX8SAl8EAaj/LES5v7DTJ3s0rT12/qh9r/kG2unBOeoVgWGEtQjLC7JmBzf8WQ3UU4Oqgy3WG939jt93t4qHL7/fYWgfh9PfXt5Z5BmD5yAKl8Ny/dSMTXYKUxYqhO8fyQWf/V+OqE9pkAXhUATFOf5iRpDAIRzSw30H8wmSXpAzFFAYitEzGiXwGUpQpE1itEssHMp3CG9OETSG+Y5DUlDeh+4si0YLAeoDnJ5hroeTGEHM6RmF2bRnzynb9tDFgkIp34ON4vvWBFLo0+2HmyOmH9PyCM/T+99eHHIOVwrzRmQeP9yUPtnUmXJ2oUNTpB9U8WKB0mWfZZhcOzvLW1aexWxR21pKTrraLvVFih7OVFPp+hHyxVlkJpo0uR4oOTfLjS4v2zJpzIktMVibhMBsSdVdTFKBNzVyfYq5TJBvlbYp1yetIkWjq0JZPB6rljCP9nUwSy8/bRp61mi2pVfTFUVNJ1JJGjWhnTNTrGN5YLOqKmsL9rfTytCtXbddHm9GNeMdQwuPpFKDSNbZdoP1LZP19aCT2TnSW7UlTtaWNdp96mTYmjh6dsxoO6oGHINaTXtOZ/GRpInaXE+iU0rqh9oyt5qc6LqVm4moSG5xnC2MEKUv8S2aXwSrX1wuIW8OM3Iy4XhDHoDHGdrBQauYJGbnvdOSRT871ms9cvFq7VCadKRzeyMnHnEobmh3BZ2Y1LndXFlNsdv1fEvnxI0u5JU+w4MJpxkzajU/Jsr1aq/bZKO0sqptDCuUotTfGMvybFaOaYizIQSzYqdERGJaS7xvls5N7wMW7PSkO3CnNBGH2yVJ+/xcnY5pEszrdn5ugpio+0DWbJvAjHhe5QvAuGmmUbJ0ZstONhabTLlZka+yDBhQL5YUOzxgA1EcQUYej44w96NdfbZqLkr0m9RfPX/Rc7eVw7ZtVuzsweu3ZXkMC9Mo5cbEiLT2S6Mk1rNNE8eYGJ3EDRoeMrtPq61jyLg4W1/y/nSeUrdr0Z3NMj9dMBy0aq+uOKqQLeq81cjeMXN2mUwPvclpg2Mc90Ei28ZSROkoa+pdEDZCP90QN72RGj3VyUnQr3o3xYfjgtosDhfOV+T02ISc2pyN9fQURy5TELgS8FYsYKulPG3BpO68+OgZZt7M8g03U6ZyQsnU/qoVepta83h57mo0uxRMlsrrA69iB78lZu2Ux4ymw5Opegn2/pCrN9u8Xi4F0BzcqDargRZuceqr9WxJq+p2GZLFoZhO0HhPiJynCw4nnjMv1FO5O82d1nYkHbfN2G68IqyXmKQttkYZX4G37kphZbSJlO802TgUSnewg0LvN014NvaosasP251rtPMdIzVx6cjJZpBLMyicxEOjbZStUc3asUBLTseZZZ4yReBRFygrnKu2cU33Zlmsd9SqTjMqLk1/B/NnWG4Ii07Rge42i+MRTsJWPEOnzAKlnA1hzK320gTJerLaGN7tQq/99cVZZqfrAsUFIJPycpJWnXyy/HjPzxUpt66mR+xv1U7CNu6OPZ+dCapXUhyZsF5iuqvKZMEcDbNgrnpeVZW5UCUjyy6rYp7aJCld+UVo2Li3l1CZLhpXrtHNJlhNl6qgi3ijGTdr4eh2RNSyGQVXUWwTjJWwNXc8LPB1QjhVJ55yw9QmdasHOz7SjlhE0Ctzte0GbVV5XaDL052u3lQFo7aHSO1X3XaOu9Vlsiz5jZ65JdNNZyTpqVdGd8tcyVaOzsuKk5p7FBPYXRgqyWlSeu5eNs3OWolMI26HYubNqJ2y39/wTUdpqJzRGtPQfpZAQovXPliWQ9iW8uAL4UVijQANiG29vSmQgrjBwVdXk5LXOKjXuTe5CtjxtJrW27VwOoM4m5rXaL2eqH2SX2RfcQKhjOf9YSnj+o3qj4W3XFLgYLhWsAtXVhwJAxtOYmawN260oaf8LuKToWi3czIvURrcmoFnwja4xUwb4Vdc6/f9vOA2K9u0xHw2YcwzD5pVZClYwIgg2fMmGl44VIZzU3aWY+W8LgKWmxVBzPeBs63JG8aucYV1pTDkTsFBKqKeMHYbMF0aQNi47uRkX8OSz89hIHtncO2dHEwIIDmJddjEzYKc+KY0WYChDxKda6STkQzN9MDVUqWYcF6NcPa2UUI28EDoZLeBtua71BsogbryvLZoTHqgJvPLtHYu/qXqF5MkSafkXl3LRWjNADDrLNlyHXOkjoW0zFC3b6/lxsqrGZplB2bqZJDwbZ04dPz6JtvLvTksOHHrSK2dy0VSH7rIrvapVGVAZ7GCp+aXWEsNr7nN9opKnpQkdn1UMxYgPeMxitl745jF05XLa1aLeeU56kA94ZeruMBM5ZriV5nf0iJjOnynCmSKpbmyCTn5WBqLlNwSpCzeKlq+EUwlmidKNhV3qFPKC07Tg2CuovA0CxJ/mqdEsRgGvpYK9KSuLEpWjlthfZo3lC+Yne5k12C/lLpIYOeLPsgKV5wUsaV2obIENt26cCg6VVw7540o8W1MqOzrxVDay9TdyEpsSmgwR7eWHpZX/rBkg4usVXVS62pI7YfM3cym2yN/RW86wxvWTdCW1y0aRSBaXTHNqW+LMnJzCZyGhs/kSZOhpHFmrfONJ9wy4Th7snS27RzFs2GTy/Y+JVNprp9ui8i7YY6hc/2WtTRRPvPGjfQxq9rP5MIhfXbH7TvcDzaYV8mGezscTqp80vHJpDHz2iYUTRddj1Q1jpfzi+TcBlZthSjZg7Q7laHlo+R2ALGk132W3FYKGtYpt5hGBbspvbW4U4LoSGj4XiYiNLE4bqnf2GBpWvQ5NSZBsdt7nNuGEoG5k0Q9nNOSrYL51NzOsbV8uZJEKIgzd7Hbpw3DdBRe7/b7S3lYV07VVOVRd1Xfn6oNASb4xG+Gdhnv6V7TWg8PmUi5HC0c7do0uWGGn588q76Uw7mnO2FPro2pE2CWWezSVSwyRxU0HRtooXjSmYZfCUONDSe3ls7CRKz5/rbcJGZM2ObQT5Xq3Fj8fGUyOsHxCyJJz5HJkAu55IzmaHebuGoG1gWUfoPsxtFkNpfX9akvc7m+YNXRTilN2Cj763orwaZOl2dm2IW7rYYSWcHv3MR3Re6EzasgHIYFnDeMLWO5GeuIWlZyR4a0pGJaeb6oW74zk5XD0BStKEy6jYqtttebKt1Ol3J9nHA16RypjpDScq+gqsREmg1UXVnb/NW1DUmwlBXVGP7xPNMUx1h7y6jHwkySrYANd/OTgQu+2DbD9cLWibKVBNPZlJdDTijnHPcES7PSM80XTb+XLhaAg3Pa0q2l0rsSlQDXnECw6wXqEGOlKRf5sZlE6PpM+7XkVmxz0HqSWLq7JlU3FV4CsccOcYnbA7EGnDfdlDUmHMB2e/Hw/Z69HG87wS3X4kFP1tJVbJVAFDggo3Hj4aZsnvVtx0dEzmprMswZ3BVPrERMcSxS9+mWqrXVlK1xTz1wR/d4LFfxmp6faYkVGUMv7WYHyeGmuFcG3bBJy95mjFd1/Ty7lYbWbsLjvHTQqJTm0cqoaOyy5fwLivHngbcjSo3EJbdpCnRLr6hzvEyL4eBtu4IlJGxPZraza5tMytUlOEyMGR8cKjXMnYMCjwMg7eVOD5Y3dN7urWG+4/JzedpnjrBbxZdlynaT7XYVq5yiTsCBYOM9NxXSWSIfwxM8RNbX7FSIBWRrfEvOQnfRnaSOZs3d9GgLtrUaSm5lHsoc89YMTQEWOFm2GazVjsAUNoe1uJpK6zMfdbsoSnoAJwdrFXAstmbmZ0EKikXOKF5VnPNTAmky690TycU7tlxSO2knsLNDoBSTLshSsGBd4YyieQMJpmQ7ibleO5dib/NJbDnFcnboOC+5Jq6t0P1+KwHeWhmsKYOkutFonsetQgcHCMJ1aJoGiIdLSVbFJU35I3ted34ytfvOq5RoJdmSKNz0aQbnVji2pWZ0aVOgDkpWEIJD1scWb2fqrget027pwhXaGUWvqaqeusLKVUyw8rzgbNBNJ861I5RHeYS3H1oltPYdg7YYGPZELvLMnqFOcFvaFmrVgLbAKrRch6HI66ml2L6Yh8vy5tMOI01EZrdw0U1ZtN1CmGyETpnVzHF3ZadznnR6lA+JDYnlTEAed/XNgmNjQZ2xFY1aZm/NTuV8pNC+hiax7VYdsh19lcHNIyaNRCoq70+nDjw6aCDZLLwNCc98Gx8eoduWwg/qhbxd0ANlm0SiFfV8zdrSShHjhSkcBz5dCOj1cHKnDByg2GKHqUWdHVyeN5d2pG3BeVpImkTqgFSLHWdNTxHIweKC9hXmClRwZvgrji+v5Doe3CuJ7ZIwccmGSndgUd6ocBvViXbMzqephq8m1tlatEfmynp4ofviNOR39Gy2OmvreAJEJXCnMnUpNpN9t93NEnt/dRY0J5BzQ4XTcDNfy7J2jufoCp1RkxWHqnGFCgp2iVCH9qd4HIeCHGWkccAYK+IkaqHqFClohTKAqdU7XJ1jF+HAG9u9jq0MLyOxy4VwjfDoYYs5I14ceg8H9Y7wbyTe9/5ZqkRGhSMinGc5n9vAZsbv2yHQlHkKNLzQIpp30nihXvQtL0j5cnHRPHlNSpaZEaCTCaHaL+dEGuZquD8z863NKj4dkNtkyjnyGki7G57zy0hdbW4nWrqdI9afLbZ+htc4RU+2cy+cFMtIt3tjMpVx6+LZYnzNrisryEm6gUV5deHgYofXS43zfXlsex5f+MqlqJWjE5nzk5PWdt5Nupsou1ZLKiSgVwKcnRdGJBCHtp8vlkKm6eHOncTTJRyTbWF+qO12kbd4Xd5yKtjPy36xToZrOpmflRt6tuGc6/UuFsyNmpRv1NKd4GtVNc40tmMsXWabVulymzC9ZV2o3olKhgMOnNYgVmElePjNZNFW8wsKcNqWWTArGQvM3tn3kxiaGTB948/LmWhKJLZHaVUT+sOmsDOAss1qIHMoFYjsXMPoqSiyA31uLzTn0/MO5rwEQEcuRAIsFXmpHmhXafeLonWj6bLiayrG/KnA7fr6OKypEi+mvufETr33XbobKNUvfB8eeJaTE81S/s24VF5oMdLlLK7LiLEXso5WdeMvqAmpsOUpnMcaGp/w68nXIFPPUZpBef66OaYLU51ScLznIuva4KILOmU77ddUNuBRbxhYN1lWmiHPg6JCtwBV1H0cTIIrCApI7wfaJNV1sO9XoGxFCYT4xR5SyqLWanXTGFTUMRZVb+fJgcAZISDh6cY0Z8V+muTAVfaM0fHSvGsZI1MUhz+dCI3CrBkzFMNqbVkKG1uH7kxvomRHbYwC8whu4VmaR6M74uotVHBR93wXUd7GZV120fNYZ+49+UqEzmWFcZS8yCt8EUrbUGEdk7VX8poSorYaJueEK6bRbMhNU6XMnlH8WT9fpsxuSG1PtTk+2u1OvchTquaIaiQvq0wmPJGKzQXn+nK3G0DuHuPWazpBblJFmy5W5BlnKGdfMgzz95fXl/Ge+nnb/N/8vnq88/t/dvX4uCV8/0bqftUMbO/zXdfn/66B/3h9qd0Imve4em3SLnheTf6ni9dPf+1bjVFW//h6eFx7a9+v71s7GP8G6iXKva5p6x4anXb3i+DXF6drxj/CaL4+L7xf7g5n5Xh7XrQhqMcb9QI6X7ZfoWuZXSdgfOaAIBq/gn0Z/1aiBcHzQvp+qTpEo4/PL0Wga9gb+jZ7+f1/AQbjPCuZJgAA -->
