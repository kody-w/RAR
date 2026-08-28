---
name: "rar-cowork-cookbook-configure-release-goods-for-picking"
description: "Applies a bulk configuration change to release goods for picking from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_release_goods_for_picking", "rar_sha256": "e208ea5cd5b571c8e15369388a86f0c91e842436b19da84e2b4aee8ab37bb50b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_release_goods_for_picking`. The original RAPP
agent is preserved byte-for-byte in `configure_release_goods_for_picking_agent.py` and in the RCI capsule.

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

Release goods for picking Configuration Bulk Setup — Applies a bulk configuration change to release goods for picking from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-release-goods-for-picking
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_release_goods_for_picking_agent.py` and embedded as the fenced Python below (sha256 e208ea5cd5b571c8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_release_goods_for_picking_agent.py` first:

```bash
python3 configure_release_goods_for_picking_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_release_goods_for_picking_agent.py   # or on stdin
python3 configure_release_goods_for_picking_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Release goods for picking Configuration Bulk Setup — Applies a bulk configuration change to release goods for picking from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-release-goods-for-picking
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_release_goods_for_picking',
    "version": '2.0.0',
    "display_name": 'Release goods for picking Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to release goods for picking from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-release-goods-for-picking',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-release-goods-for-picking',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cf924e23a2ff7814',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/release-goods-for-picking'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/configure-release-goods-for-picking', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureReleaseGoodsForPicking(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReleaseGoodsForPicking'
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
    print(ConfigureReleaseGoodsForPicking().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6ebOb1rbnV6HP+8POk32YB/nWrWoEaGAQkkCAFKccZpCYBzGk8917I+kcxy83r2+6uqpluyxg7TWv9Vt7o99e7LaJ8urly4vm2xm0spMkjvwKsjMP4vIur67gv/zqgH+Qm2dNFTttk1f1y6cXz6/dKi6aOM/AcrYoktivIRty2uROG8RhW9nTY8iN7Cz0oSaHKj/x7dqHwjz3aijIK6iI3WuchVBQ5SkQC8VZ0TaQ0Lt+AgVx4n+CuriJoJudxN6D26RblSeJY7tXqG6LIq+aV6CQ39tpkfj1y5eff/n0EoPvL19+e3ETuwa3XrinRv7hocJq0mCZV7uHfLA+AUoCwmIAHsnAdeFXQMEU3PL8AHpefaz9JPgE/ed/Xju7CuufvnzNoOfn68v059BmUBNNxtp143uQaxe2EydxM7xCbNLZQw2c0LRVNvmqBg7NwtfHyu+c8gL65/Ts40PIa+g3H7++5ECFuwe+vvwEAc99fana6fvrxKX4+NNrknd+9fGn73zq1rn4bjMxA1q/fnteP9kCwu+kcXCX+k/A9RFYx//68gfjps9D78lOsPLl9ZLH2ccH46LKb35mZ67/8ae/YutGvntN4rr5t/j+/GAc+bYHbHoq/tOnu5N/gWZPg955/rXYAoT171gCyN/EfYKejvor3nf//xfWSZyBMnjz+L9k968WzP4J/fyXtv13Cz5BwdcX3k/iG8gOJ/G/QL9903YC9/MH7/vND7/8Dlj/H9loeVu5dw7fUjuLA79uvn37+UN9v/3hl58/tAXINd9Ov7VV8q94/iu/3uX84MEn1ccf1wL5x+ya5V0GvWc69Fte/I/q91fImMr/+/36C/THepk+M2gy4k3owwV/qJka6PoHP/708jtoERmwpnXvj0GV/8d/QErsVnmdBw2kuTloQyDATZz6k/J6FNcQ+DvVduUDv9YxcOyTDuT/FOFJ4zyAfv2f7r11fnafrRN+a4f+t2cD/HZvgN9AR/n2bIC/vkI6YJ1XcRhndgId2N3ua2aHftZMYovKr/3qBhqKMzT+Z7Dw8/QFtEvo13+D+7c7o9di+PXePuNHjzpwm6k/1W3iv042mpGfPS1yQSv2e99tgYwkd+1HM64/AdvrPLmB/jb5o77GSQJ5cQWMz6vh0Zrb7MvE7Ndff3XsOvqaPRoqDj3gooYBwbs60OfPwLIgicOo+Zr5bpRDH377/QP0v6D/btWd+SRjB3r7MyJAQ1FTtxCosDYFZCBYILygfdwj8tvvT/8CNhnANxC/OJjwaloMMvTqe2/O1tbsZ4ykIMcH/gMOTid8mRAqbl6hTQC96wuETo+mPh7ldQN5fuFnnp+5A+BqA3PePZnlDVSDNKyD4RPU1v5d6q9OZd9VTEGp282vkMLtAGrkyR0nnygCFudZDNz/ngqP+4BJ9aGGFm8sXqHtlJNQYVd2EVX2U0ZgP+IC0OJtOWBuQ5nffc0mhPQnV90L5OEeQAQ84z5D+nmKOcDyFHQDr36TfaexJ2zT7xhXfc3qZ/Lb1RQKF4ABEBq2ALEBJPzjmVJ1lLeJd/cf0HTi9IyC94zKPQcPfzkhcD/MFItpzNBAJymgry2GoAT0/3sEmbRnV6uDsGJ1gYeErX44Pbw6TU6T9x/DFhgF7mLvFfR9PHhrLm899muWxCBFquEfD8p7LJ40j74FKt4DfeJw5w8SAXh14nvP0ynvqurujq/ZWzP/BHxz71zABFDUIOknh7wJnJ6+aRqByp2uvwP7Pa6VN5kOchEqWicBeRL4vnd3QhNVU609QwGS1p/qrotiN/rBKghwB7kB+ENAiRhUD2j4d9dtc2DmWxTeyeNpXAJaeK0LtAWjqf8KmaBcppSpQY2CmWeiAV74cGcFpT7wMVDx3cN1ZBcPZaZp9qmgPcUiT0EW/zECz4ffE/yuy6Q+4GqD2ANfdlPP9fz+Edl3PZ+xAsqmU0neF/0Y7qet0B9R5x9fs7uO720eVHoyAfYfnAOBCkvre8pNjaoGzSb1nwkEMuGOza8PeH3g97suX/40wn/8e1P+HTCPP0buCxQ1TVF/geEHyL1h3CtoEzDIkbjw6+949/lZbZ/v1XaHrWe1/cD64akv0N9T7wcWz7z+AqGvyCsyPZJj158S9/kB3uA+L06fienp1Ge+h/mZC1OfTQYAsO+g80YCkCes/HAifoBQPWFXB+Dy3nVBIL5m76nwLJRHxwGIWed/KOA7+oLAPuL2Dg7gUdYA2d40sYX+tJ1JJvVr/+VL1ibJp5fMTv1/axszQQBIV+COafsDSgeMQE3s36/ex6Hp4scN3L2oQDfw8i9TbX2CptH1E/Q+hX6C3vYF971W1oKN0c/TBDyJBKTgv3fa992h47+ArVgzFJPqj83ONHg9B+I/KzGVFNDY9SdYz99rdJL4JybgSxj61Z+ZqPcvdvJsFHVjTyAdN2/lXQM9vXZq6yB4oOxAJYEG2YIFfxYD5FR+2QI09CZzv/vvu1n5w5bf725oHjvG317eGsYzBs/pEJCDyvxcT3gIg0QFAsH1I6XAs/+bufHJAnQ5MLQAHj6GML5Nuh7pkDTqMj5K4tQcZxiboQLEnaM+Q2AETjno3LMZwsccwvZ9xnZw2nFIxAH8Hrn5bcL9eFILs22XcWmU8Oa0Tbk+jji466MY6tG4j5BzPGAYnwAeel8KFPOetj5smxz5PsJOPnma/NuLQxGAck3UG/bx4eC5YTsm7BwieVYls77HqT3u54lmNbehNfY9bgzsOUfi9dZaSjQr16nR8Nby7KTX9RmNcn4W32gOJkXqjNvHXMtse81S60WaXK50O9bwbhh55XIwBMSXtoNoI5qGKYPU26lQGqqMm/1S8lNTjZIjk9gpsmGcQJRdmy6LSIPh2yCrXCZbXF0VwiU/OOW4TXDxVCaCczygBXxYnr0zt7xurDNgV+N+MdQGR2L5tcrMuZC4A0qmupg3isE5O4FMfK5pj4WdlYO56JjbSKb0LhMxeHeLxKyaU7OZScR4SRwlQ6ryyB5Kw0+Rm7niKdTC8uKYXOSDquO8Mx7NLWU20mBZIdplid1hlznKHWOl7k6btDo30tmXt8OhNoGdkRTZFUUkxPG47QxHaBZpc6Y25jDfR1hrSIYYGOMVJeMt0R0upYrv3ZnRcDfqZo9KohXXq1adZN4wDo3rE+tUJ/nc4KjjcMtm8zDXFMvgTvswHYWtW2U2idGxErZeuXdYYeltUBgM6ydatBbwSW4wxiRs2+iCxr4iazWRLscDTpFX2S7TmhMPrZOmW+cyu7Km2JzEpkaWlSm3WuHtBEP06zTW6ZQ2a8MLyvnKLk58x4xkpxW8JWhOZPMlGc01UafJLjNhjHEp/roqz7jTJGhFM5F3afDOHzHmtECvSDsoWQ2P2JHrMaLZpIVRafjaoChZGxrzXKLMTeHHoky0hV2LrkvAAJKU66JgUGN7kaMdIxK0ujzKpHqi9/ViLtMcE0WoS4XGtfS74QzPRxQ9DjVVlUg9uyLkCSvw0RNHq5TiLZfUjbo/m1XNYJXi6+ZqSNXAQHFxvIYjY64lT7OIlUiJEamsr51HMLShLl0zh7utnG2oILgEMzaeLcTlDcCUV9W3YiUumghBSqs5YyvRWbpy3KKFcuxnTKQOIcqt7Hkv8UmIsDard/Fayk7CiOtDIpE8nOltWLRy1+gckRgHYhYp+3mnOfnAeieF4KOr3c8ksV1ke1GTnCpa2MixFxJtlBW7HvsTdrlaTTCAysFmK2u8WBdCbJsdJt8u5GUuuEpQB8EaUW5dEu/7CxObhJWmzjmT9cOoztYs4cTH4oxt4eHGOPlma8thJOYdI3eg3pNrK+MHj98LKh9uLwLa7reZXruxudZMiesbfd1JjAnP2Q6u6tYO0mq+p+GcDVl5OLfENlulbpgrc7IP96ujXR+imTXmNGLD50VJH8oTAsNzJTihptHRiSUrFiW6+gHViynrYDvWIivpq97z1pty5rBXmAuv1RxVIwkzQsPAdd73b5tjKKziXm/zWXBIes1EkIOdOYUbB6OmM3rVpL3Ss7NZUWvnQ1Edd8zCcdeiYTSLtpnT5GVdKbOTUzOubIIWg2BlukB1u3BdkbgsD6I8LG2qGUV9UXrnTitN+2iVSt3mY3jOHRCLhbtxXPky89ryaO8alXZnaHEdUYEy+SCwIlMvene2SI6YgTAiXcsmLXlh1mTp6Ekls8TZHZ3BcH1gWGrv7SiVF7uO8hlJcvfbnOI6g9jdOP+sxstdq+147njm49Oar7dlJ+W2cpUOZIwt9qfBzfIyw7ur211TL827Czkz5abfpbq0bF0MCdJBDsbFYjwtT6tuz5hHCjtIu/kK2UdCqFgb7Cos5Os1ivVwG5oXZ9bgpqd4G7Y8sp6ZLAXjdCaWXjmEWJRWwNJFuJAOR65VouGs+UdaXbXMdtYRNJNE/F6cMQjXiye/o+xMxSlPrBKxyHSL8tybXs/97Dw7aEu2Oo3WZbx6onhI0WDlSvWc0l2Oa6mtrNdresg7c4NbJ7ft6sNaleTbSFP7C05ZPGnLOyCM8IKZwPcpaLaelWUtWfBsGC5VdFPuySZTKl8Kl5vb8lI0bsi7zmJuuERqr7pNGyWnkdlXzNKETf2IqpdjNuanuRDy4XDcquUy59esyvasw/G+INMtL6XNdWut9YG6YPXIt+GMHoZEzeRsKJNge7RzkT0tCEfs/MxTxyZFl0LTS6zOmzYcz3YBWrS6gHl2AjZpsmnP3GZP53OxDVl3U19W7s070zpsUisp6BP0qrTSarNhB4NxNDocY3nRLFx8zyTX1EUUMCzkq0UmHV0UjefaDO9VfEMLWR5fxzxz6wVr1d2gh3Z7O+W7cWmjR6S2aWMWK4K5NMZ2I+lAuWI8esXJN41NLONWaKUYjyLXMzKwRNiwVdnf5FKLx/xKcIGL5nyDarq5bquTHaYtF+d11mYS2ipH099RV5KxDRPZUNcTOy6527U7N+I8uu2tRYq6veHchrkYXpTEhqlSLu1jFHM0b54MRrvtz/qSI9dycY0sKyIHtOROySVfhyN1S5HOUfbI1dEq9Ygd1tudPC/a2a5C3bQY1OtZk3NRX8qbowTTZ1cXzSbNaZFzECui2rmS8eoSzk6uLuxipDAzocTmKavNUFk/yqt8MaN9So1MMfUQdREqmyxY+j228Nz5MtIR6RbbK6mA9TwSCWUpSpdKMeS5wpH7ImAuPB9WUrXfOcKVJC5NlKRyKSZ2zF9MYm30wepg3HKO7wRy5eyPFF5SyY4+XPfxbR80LDwbYAe5GVesv+4WMUnYoXKK3BbXLfNm4KdU3NMqKTLMXEVgvaGpbm9fLPYshE7Irx30FhwEV+3xeblVEbEHu61A1s7irZ+ftfmKbz0phZ2bTfq51KwvG3Z+awp1z2qGUIbsycEPbMeI1VJUF7eGP3POclvz3nnBBbeRoAuXbCSu2SN7rjl5FVuIzKnMd5RC7ZNquaquJVUpnbVuZ9f9scz12xFd0BTqluK44mVD3poA9xiOP/GcQCOFb58XkhmmAFZP41GTWi0oNwuNdo/hnkRbPx2MC8tZYmhpm3PrM8PBdkgRPqqqnwwpcdILMHKtmDjgkAIm9iM/INnSxtJzKyn9IGVLK5KqssCi82bZ7uGw3KarEwmLC2d/OHOL4aBVWiWv92Td5GKsYaf9xpitj17vDYGjAvjT8P1hQ1d1KuAFDdCapUskd2r5ikaGBeJbkv5yFNHlWWpv8wKPd3qh11ph2JK8CTxeDW2mNusgVRYtfvbGRqwLY7vMxMZuZs01mRmrZItiKuJ5UoF0SN/FAWnOV4NDR0lSXQM/XDElmedF3ghrIe/VhSRJF70/2AEebfKVdOkc6UgRs6V3GiRrhbkLj636C5rWBXUQEjTe4CjVwalnNkGowGiPzXFztdGuW31Jy4V3MstYPLBomWM3IWDpy3592uwiJDt1EqbRSmxkOtJyR71AtCwRzGrclMLptq3GBUZtwTSg9GovZL1BhUvJ3i55rVE3XRG42GVr4CzOKUNxHPVzg1/73Y6gxWA4hlcAYjPXMZ3BFXxqzXYkdVREvSRQNj9r4amw9qm13rbciS3PHuOxmwu8UnZqrFNas1fk/SWmkZovr7SL+duS0xeXHX/TWgc9iOPISplHSa3nh157Kpb8ebWy8CTBFHbNrPg9rpF5I0VVryZVeB5iLTsIeUjUaJslWnpsjIUQxdFsxXWnlbgJ4WyzayXkXBi5GEarGdi/LEuKtkgs3tvt2F6XJsvbrmo4UtN7Bl07J6FYqKLQES2Al+E0q0wJMYcKP8t2YAq7ddhLq+TGKRxoElm6nBXBsKHG9ICZfuq3WE5vV1h7K7XV0TgIqlrOpLgJMAFrzkgxF6owUrz5omuQYljgMbzudkG+XeCeQZ1bbxVRaWTjNeLTFV5zN5VcMdgaIekZ7K4CHt1mjj8P3F6N82uxRc6DrN/K00VjtmoXU7sDHObECk60Fs+O48FOI4o4OxsmHUd1s4nzQaGUfB2toz6YO8yCEtkt4t4knqQ6hp+h/LjWjHC1pTi4IKh5by+CY+a0FZtR5q7qNyveCeETJjC8QtJEc3BalVZHBj85VxYz1z2682rZ7T2yrRfEbseDsfDsB8zBFyTGUykcnlsBqCHZwts08JJ5kGdml7WnTLFC+YYsCO9gEU1b+BtyniEh1mIzLkAEMzuCKLiqJs0JZ38R8YEjj+7eP47txZYvXJCOO77yMftkOa1Xj8yRxahTiW+bBT0TVLPEjqO62HvD7OYfXbJPF2DyRqLzwTngKLdxyNCzYJ31M8KZ5euaRtcwLoCd32U5gF3PYSaPTVO2+wzG3bOZMmW92GZELM+0ddV2istvk3zXtk5Mnua+JtrrGepcato62LtZA5M9Sl4219q5HWhWOYjC3N8ljbcd8My4BcphG6EgG/koljGWd+KLOs4dC2eyMShXpOduVtZ2Frk9hbu3E0OTuuIK6IrN6MqrsbDdRYoVI/FmNR822VELWis/MIzgYehsfYsEji/7yA8KbAMGqqOVkn6rkWt7zxNksl3vkv1JJmR7AUoToJoexLqK+WJLUSNPdmuAELF/xZSOaCgmw0dCWV0O5E7sdyjrafxBX2v0Tl9Zi17whNVZroVo3+i17oBZ7+QRu6VnwynKRe3teI6NOSycsetWXId0pxJR5VzADNgvR79o8J2t6StcKapdi6zPwVVCepwql+oKHQYw5Y/BCFusR2+r6zkNglpoXG69Uqssl2HVNfx14CqoE4TOzMN2e0wuZZ223K2/2fT2iGHZ4cy2dozTYA6WKtdRG3ys6sJBsC7zHbBnXVzKUUJOl5jE2AoFMeQVtlssndmlWsJ6NIOdVczyUs+ku0PkraszfyGYJS2kVmBwcN71lx2oRXFLhOto52DCeHaDFezQlWueWwzs7b1gPiNkHLnub0HUjbCPzy/mjlooCRxrYo+2tDW7RfY+R6u0tWfBen1YUcP8HDnZEoMPMJwskS4NrCzoVhiT0KSySTXuxm2Vva6HpbMs1f42WgNCrpYWHW/X2lYPXGm2ps1b39qLfCOGZlERbRBUhSVsV0VkZ+s8WKdgq9xs57bTWxtntLesfeM4DuxOGIJVI/zMsCy+SiJRcbPtFozFfH7AztztiF2VZu/Qt7PGuHMuQE95VgqizlF01wYFQoYLwt/xRFHZjEyTCzTlc3ZZRZwvV/sleVtEh6Uxy+ekYmeAulwoyo2L6ghV/ITXMntMiCXeEnosU9Kt8daKDG+xg8gskqBkhPmI3czDzLHkXCXhutvScBDGA3waWpiQwt2lNpK9f9EO5UAo/jGQIq4M5ivLkZ0dbQ9r1UMHgs9YLxMQfJ7LWtgh/HGzwdQUDOusZRkby/UHr28YXbWqIFHPhBBJ1M6PRY3CL53FsH3txWATWLIs+8+XTy/TEfbzIPrvvHSeDgb/n51PPo4S315L3Q+hfdv7cpf15W9p9cunl8qNgU6Pk9g6acPnoeV/OYf9/G+8z5gYDI+3udM7tL55O7hv7HD6SdJLnHlt3VTDtzpP2vth8KcXp62nX0fU356H3i9309JiOkF/l/ky/VJhOqnOweIm//b8Xcf99vRuyPdiu/Gfl+HzfPrTizeASMVu/Q2nyG9+VUzmPl+STGe601uSl9//NwJWh8gBJgAA -->
