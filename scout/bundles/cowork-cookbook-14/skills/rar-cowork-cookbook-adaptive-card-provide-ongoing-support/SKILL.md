---
name: "rar-cowork-cookbook-adaptive-card-provide-ongoing-support"
description: "Produces a reusable Adaptive Card JSON snapshot of provide ongoing support status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_provide_ongoing_support", "rar_sha256": "1260ca1b808cdb91fe0f6acf901715ebb3b62176b24e210e24260b2dc01df066", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_provide_ongoing_support_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-provide-ongoing-support:7b8542b7e8ecec57e9ab3341dc8d3f2211d2fcd96b224d8d9daeb976711f3021", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_provide_ongoing_support`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_provide_ongoing_support_agent.py` is
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

Provide ongoing support Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of provide ongoing support status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-provide-ongoing-support
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_provide_ongoing_support_agent.py` and embedded as the fenced Python below (sha256 1260ca1b808cdb91…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_provide_ongoing_support_agent.py` first:

```bash
python3 adaptive_card_provide_ongoing_support_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_provide_ongoing_support_agent.py   # or on stdin
python3 adaptive_card_provide_ongoing_support_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Provide ongoing support Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of provide ongoing support status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-provide-ongoing-support
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_provide_ongoing_support',
    "version": '2.0.0',
    "display_name": 'Provide ongoing support Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of provide ongoing support status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'adaptive-card-provide-ongoing-support',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-provide-ongoing-support',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f9151188b581d751',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/provide-ongoing-support'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-provide-ongoing-support', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardProvideOngoingSupport(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardProvideOngoingSupport'
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
    print(AdaptiveCardProvideOngoingSupport().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZOjSJbnV2Fi/qiqUWaKSxzR1maLEAIBEohLEpVtUdwgcYlTUFvffR1JEVk51dXTtbZmq7AIAe7+7vd7z5349cVpm7ioXl5f9MDJId5J0yQOKsjJfYgt+qK6gK/i4oJfyCvypkrctimq+uXTix/UXpWUTVLkYLlaFX7rBTXkQFXQ1o6bBhDjO2C4CyDWqXxI1JUdVOdOWcdFAxUhVFZFl/gBVORRkeQRVLdlWVQNVDdO09ZQWFRQkLmB70+DSQ75Th27BSBVfwIDTpKCbzDHCJys/gIECm5OVqZB/fL68z8+vSTg+uX11xcvdWrw6OVdmEkW9cFZeTDWH3wBhdTJIzC1HIBNcnBfBhWQIgOP/ADI+7j7sQ7S8BP0X/916Z0qqn96/ZpDz8/Xl+lHa3OoiQOoKZy6CXzIc0rHTdKkGb5ATNo7Qw1M1LRVPhmrBibNoy+Pld8oFSX092nsxweTL1HQ/Pj1pQAiOJPBv778NKn+9aVqp+svE5Xyx5++pEUfVD/+9I1O3brnwGsmYkDqL2/P+ydZMPHb1CS8c/07oPpwrRt8ffmdctPnIfekJ1j58uUMzPfjg/DkzCB3ci/48ac/I+vFgXdJk7r5t+j+/CAcB44PdHoK/tOnu5H/Ac2eCn3Q/HO2JXDrX9EETH9n9wl6GurPaN/t/99Ip0kO8uDd4v+U3D9bMPs79POf6vavFnyCwq8vqyAFwV1NefcK/fqmqxz78w/+t4c//OM3QPp/JKMXbeXdKbxlTp6EQd28vf38Q31//MM/fv6hLUGsgYx7a6v0n9H8Z3a98/nOgs9ZP36/FvA380te9Dn0EenQr0X5H9VvXyDLSRP/2/P6Ffp9vkyfGTQp8c70YYLf5UwNZP2dHX96+Q2ARA60ab37MMjy//xPaJt4VVEXYQPpXtE2EHBwk2TBJLwRJzVkPJP6F13ayPKXzP8FAk+ndAcQ4bRpA/EVgKYJ3CaPTxoAqPvlf3l3MP3sPcF07jzh6M0DePT2hMK3JxS+PaHwly+QEQPeRZVESe6kkMaoKuREQd5MXO/xUbfZ525iDIRKHsCjsZsJdOo2Df4G/fJvcXq7E/1SDpM6X3PgHwc4zYeaIAPDTpWkA+RMeOUOTfAZIC3AlKpIU9fxLtD0py2/TDY6xEH+tJwH6klwC7y2CaC08ID0YQLQ+RNwfl2koCo0kz3rS5KmkJ9UwFhFNdwLD7D560Tsl19+cQHmf80fgIxBj4JTz8GED4Ghz5/LKgjTJIqbr3ngxQX0w6+//QD9b+hfrboTn3iooDrcjQaCOn3UKJChbQam1dAUHgB+7h789beHNybpclAhQV4lYRLcFwNq38Jh0uDhonf/AJ0nEYPqyel7u0F9DOwCJQ2wFsj1+tPXfCJRgKlVn9TBuxEfix+mf3f4g8/kk/ppQ+CnsCqy+9x7JE7O9IrK/wJtQujDUkDdye2TR+OibkDwlkHuB7k3gJVO882FOajVNcifOhw+QW0NVJ0o/+IC0pNxMgBSTvMLtGVVUO+KFPyZDHRnD1YXeTI5/hmxj8eASPUDiLHlO4kv0C4A1oRKp3LKuHLq4D4vdB4RAerc+3pA3IHyoIem4h5MPrpn9j3y1D/pJvRHN/F9L/K1RWEEh/5/Ny2T3AzPaxzPGNwK4naGdnoE2dRrTTo/2jPQOtwp3zPmWzvxjjzvmPw1TxPgmGr422NmeI+rx5wHzrUVCBqN0e70pwyv7nSTBkTH5O6qmiLa+Zq/g/8nYBrgm3rCMZDElwkSig+G0+i7pDFQdLr/1ghAj8CbEgKENFS2bpp4UBgE/j36m7iacuvpChAqwWRfkAxe/J1WEKAOwgDQB0YHooKv/uHyHciRycz3gP+YnkztVfnwrA+BJAq+QIcppkFc1pAbgB5pmgOs8MOdFJQFwMZAxA8L17FTPoSZ+t+ngM7kiyJzmuD3HngOgvicqgzg95F8gCpA3gbYsgdOALl1e3j2Q86nr4Cw2ZQI90Xfu/upK/T7KvW3KQGBjN+KAGjZ74H7zTgAtausvgMRKL2XGqR4FjwDCETCvZZ/eZTjR73/kOX1D03/j39tX3AvsOb3nnuF4qYp69f5/FEE32vgF6/I5iBGkjKoP+rh56lKfX5m2ednln1+Ztl3xB+2eoX+moDfkXhG9iuEfIG/wNOQnHjBFLrPD7AH+3l5+oxPo19zLfjm6Gc0TPgGMNcdPsrM+xRQa6IqiKbJj7JTT9WqBwXyjnb3svERDM9UAWCaR1ONrIvfpfCk0+Tah+c+UBkM5RPe+1OPFwXTFiidxK+Dl9e8TdNPL7mTBf/m1mcCXxCywCDTpgnYH7RNTRLc7z5aqOnm+23fPbEAIvjF65RfoNCBdvcT9NG5foLe9xL3HVregs3Uz1PXPLEEU8HXx9yPPaUbvIANXDOUk/CPDdLUrD2b6D8KMaUVkBgAeT3J8p6nE8c/EAEXURRUfySi3C+c9AkWAM+n8giq8jPFayCnDzoqAOPdlHogmwBItmDBH9kAPlVwbUFB9id1v9nvm1rFQ5ff7mZoHrvMX1/eQWO6fnQHj9ABC/5aGzfZ9b38vk3UnYnGvdm6m/neqr4BFZOpzP5uKJp6hrdHOL68AtgJPr1MxqwS0H+P9831y0MkoMu3JhdQAADyuZ7ahjnIJkAJFPNy0uMCwO93DKbHiX+fP128/mln/C+R4JV0qQWOumRABV7gLciAdlwMwxHfo3wsRFEE8dHQ82nCRVHcp3zadwKXJgkSQUIMRhEgyeTRzHlKMkcmXwAdPgz+f9eyvzyIgBKCLghABUEJ2HMQl4Ipz3dpJAzgkHC8kIYRElkErou5BIqQQEw8QBE4QHGwwEV9D0b8ECaIid6zX3xI9vbem79754EKbwBMs2SSG3Ucj/JIBPdp0iG8AINdzAsQFPFJLIAXNBZSVICD9R9Lnx6aHPhQfgpg0CqCRq2b+Pz69PgUlAQOZgp4vWEeH3ZOWw6Bye4tPs5GIjwVZ6oQ3dvJLdHM3x3Eok5aZb5ORTmwz1txuaZYHWPOXJ/GzPbaacYST4xFlBPHUJETnJP8VClpRdTwS0HusrGdhUMeUDVokZY4h8RVfkjibXbQMl8+OTW1g81SvpS2lTqeuNp0tGvqJSlubiw1n+t9vwFxa59MM3au9XktW5d5Rd6C5thnp6EZGoOttvuZgVQHOeT7WGMrXbHElV5sF+tNixdba3fRlldNobR6cBeWh1Jp5KkyNQtzm1oomE3PNjXidyM5CxPZq8SDZKR6UcXOKKV6CrcHnl6Ypct5jaedr6k9T6pYYC2UlJj2wl8LeHPICF/xpPWNZyk2AiX5Cm9SvBsv+c6SAYazSFAOm5QwzXVvZpf+dtg2W3mxb7RxJTf6td6V6cY4DmvUscr0qmpBSVWCKM/EVikM3rlFZ+TMzDtRXoLqoh1SJT7JpQ1slIYnbtzja3SfmahxzBYHxUK6nPOXnstF2HmD+Hjj75alQm/PUXiW62KUC+t2ucip0czFTErZs6lhBHKRTsW1HkT96l5iXrvNh03FHWoeHRzmVq0xEVMwbr0OqJ2Zozu0sa9X0nIOenla9ZRB95mz8/fibWcPNberRDwlKmy05e2cvN1q7sLvFdevWzoIOVnxW3SJzjCDCRY7uT6LpArDCz1t5WS9sRy45W9xZaeaWdXIaXZslwvzdrhFzYFrFVYdTTvDG6M3zdmuPVV9Pia4udoYI8lzcYecTsiME9ZkwfKnkmTX8DxTXWtUblLdeePVNTI25MMGv+zautxc5Hy4EKlBMrdNgtszrHcev+OVyO0sK1IVRRbHCJ8nmZE4qlhQfZ1gSnoyyxAPXYEj5l1FUhp1U1bxsTo2NMMnwwy2OR4Vzvs2SHP/lBRW37KkecFtlrbZcLGs+e1Jv0lyHMGbYGlsUlJ0pQvD0Da8LQ/K/rZAVoVyrvuBOY28mVoREXm8JGq9zSgef7LOubNMpBPGkQW35XYpHrcbyWaZq71A1WCM9/nqYrequKtiX4gtCl/gdEGeTZ+lLudC1UTijBvBBla6m9/q6xWcObSrcig2WjzJBqWlMsGOjzEZpcNqjs1BPFH1eqNgBQxLfZ7OpdI71sPAM4W56V1OrOCiVBRtEE+WZp9kHrGFyEOazRiux1w8Yg5VIGS9c+ymPhP1So8H47J1zGUeM/srbKPz9HaGh2HvBpwr7LpxtYZp1gqMVQugf6VmqWTYcFcTnt2FnXTJmfXCduo9vGeEa2wFCryv0MqX1vVVFiulPVDewWmZjWafpZIdcaWT2CG/uHvCry56sBNCcxDQ+LBN5u2h0su4KLl8Ic/2AnU9blj01rYzeXEWKml2cmvKqw4wY2JuelwWF+RarZhggxwTiYiyM6kq151Y7ivWwQUjvfGeKQ5blBzl7dJUDEo4z5rr2bwukZG68llx4LoBd0gvP1xpXizOqGaVrIEzcomK9BFlD4gjH/JAg4X2GMHhsUuMk4B1fIxwSlBEbNSmy51xODgZT6yw80lDzXZciKZ4jm1BTmrxxDdSEVsiOWJx7URjtFA1KwyHWc+yPuYuJSUvvQ67ECfFP1rZUFOr0m/tIiKLTbNkipW85rvLUNGawhdEz5cXQmeWMaH3mjQe+kPiSs3C9GtfdrLNkmkU0DNwp6u3Mg0Zj2eCdFj3eCVv1weLt8RrlOCasDsEwupEBYyuX68b9eAt7Uur2r5qyB6tFLTGmWNV0bv6WKJBJ9eLjbhPDrVW5ljYE5Wjn1OF3tnNieQ7m1vHCHGoGzWsDKZ2W+VE+nGUiBcqCM4i7AtHDLfVMB8kNTcuwzaUhIUOS0w3YrfQu0RMeVgKehbWizLdVrpUI5t2fb62MMbc8pZiHb0xfKVd7sVLnlGOKhzxPsSDYCPubEv38B2x3/uNkeumu8NXnn2OVP7U7+JYrdfzwzI20IS3kpt7vRGmjSDMnKRi3XbT0F8XB0phcdBL9VuAlsBIJ/4QWgfW4a+zEe7Og1+TddnVEqFGI7lfibXtlbsxyi3kCmcttrOrZjRDo6P0nc6oUUOiSeuXuRGhKLe1FhVyUdodvxUvnA82ILfFySY6hygDbE9lcHaGGQTXC5nJJavO0/OJ7GtRbbV2s1zbBTpjSfqywReNGjl8rsQrDcb4oy0ToBvjpUxgJPi6t8aDn9KkxVX7fbVUKLM/NvEosBx5XMlDZclcrC0vy3RW6fz6WFDaJlHPLGIZu6Oorsc9nBhSSkdmwMD2vjBRrd7nJ1bozXzNLgRJKprjMab1nli2C6NAbspw1Zb1rTJyzVqPXC810UKsSQwfg4q7STocXXZLt8/KaM8JfpvRu81gS/hx2Mu7lXwJcjo75dyNzuZCc0g3R3ccLLe9rTGlTRclNzob0+P40SL9NX5ZYhHFMXrmUSkiHKl5pJjamhj1cXCwEt5fKJ7I0ZpKJWrJ7XZrq9Lt3j0FyMl01trpgu04BRUOzDpI1slme9nXEdn7h3Jf4yynRQizok96I8/h+LKPxWjWaZVPsiW39Rt+LE6twpQrn5HkjCLR9eJMXG5SZtv6DKaCWbvoRHROy/vNyrA2FttWaLOdgajRelc+qgVMCAIP97RTVxd05HeIip7aM2oJZ5esjD2TwPAp0jjSskhMZza1y60lpUNm/qAdiIO36hxB54atc2L3g85SgbBD9Qumm0s7Cg1LRxyYLvXW2J+Csw3Hy4O0MxUNPh4YQ2iJ+lSu9znYM21vV8S7ihoxa6SUj8PAJhh3uzyz/nDodmHk6p5cJkrKMap9muGRJZd9EcXjcHUuupWzrLA+5zrnEAHHEaJYzK9huNHt0PWXOyZA7Jbp0nEfXLqcX59y2cY3AzLawqpP5coWbf4Ix6lktysEbNR1Vt+my2Xg8KvGZtf6VrqupWuoXPqFYBmXuLmdh9Qt0Nt6yRkLPqW1OJ6x3mZW1IqC2sYsZzfYiTVdpap7zqn03aEdgjIXkXXK7brOMjp/FQxutBgrltxfFyuyGWdsO94qrhy3px23Co4XfRbVF1a4LY6c1fCqlJBlsBlQ49z4vm/e+qRbmAvh5BCEv+1MzNiuuiLZZ4thoyXIZluUM6qsl8uoimmDiGcFzw4XT9oQ6GW5P5B4zmDexlqZNo1l59CW7Vw/L+bLCvWz3MTxYifo8d5wKOmoidKJqS0Txs/4yvKs8obBnbGyQN3eni85C+8aWC/hlZCuDthVM6W16woxG5KUoct1AoqVsk1RJtmOxkGPBEpLRlGTuyrUea8nN40qKhJ5sMwrnPj+THJm5ma9wgY/vmyamauL/ujvSQLerA0dh5nCZ/NTbGmZy1lXsWUky6cEXBUC7hRQVD6utGh7UBeJiHaVJaKLxrTNKJdmgnUWG3HYsGDP5eguQVzdoJi1yI1bRic7VHR3g+Eq7J/Q68EX+JxQCbi7HvdSSIvjNbajom6UPDUztrUQbcWt6u3S6X0+OQ9edNlWWhYGTG1uUSNa164Iow1Sc7Hl5f6GuZ5x4qiY5Nru/THEDksx1jl2wZ3VVXkreMEgtvvj6SapWliLIFNNe7YpHG2mRceT5bVOt1xjFO0L1Q02OmHJURLblORis7ys9xImIgGtmeo6lFkTNDUVcqRZm0pJBxMFX/LkkFqdZ3g/E6KuLqkWOWAE1eJa1xQBGWMZ7dCU3HlCOWI2SvpFaGZ+7RLULdLWtqy7DYLtFJCzStrCLutGNN8ul4OSs7nve3TDUsgKQT1EX6gYb0Qaf8psU9fVRDGSeY9EZ3i/Q24jI127Q967vW8Dehs2bvojkQcwxaoDmTWlU0tqidAOr+47n3T5W4fe5BknNfVxFWY2avsowlgxM1fEW710r3IXIJGq3XCjI+VxnMfLYV/dQDMwn992c8HQ0bzztzO04uea3JRqoPFsFwkpSBGclfFWEf2lPV4RGV8W9bwAPe1+QZDqzSlja8ksbiguaupGwJn0FF6whMFzkZlTuLqqDimBH1zFT/ttL6HSCJrhIJphFA/2eIwktLm6yI8eehvjLY9tz42YrqmlZ+JIk91Ej+5FMkQMhKGaIOpmeHJlvVtQzztOjSiwbyc3x1njlbN0a+nM+UacTzSdh27ARAPnjrxPeyDnKXddhLJWKVYZ2osjgc0rQQA9qUdWvlos02IDgCcQsf4ghP6FmJ0Gl60ytCMN7rDdS+j64Gc42nWLMGtBp+GRe6lzaWZxLlVPLWh3cdzWHMIyOVnZNcq0ahwcE5jdHBbjpjP28Xq8WBTF0TA9Nzt9Y5LiOg7Dst1khGgdMzpojYXg7lf4ItUENd6ftrjsLHdCvlfPonpLxnWedK1aM20QRJW5weJVRUlXJSSiQD1WVLACUMzQ5nKQd7YcuktstwDblcAGHe2l1/x2DJdg50CPahv3XdeJqeZj4dW7bZtwmXg3zJR7FguPN8Gm/CHP8LOL+gVOSsHpEs0zil8YO3YR+fNU5ViJboRWCBPqhvXYoXdt1a2O+UrOufi2ynAyynGr507KrLevszkD0h3tTpmMyxqdeTNsXYEmbgbvGON0pKWT3yjIbUsIxvZAd61h7QKsxVzzwBfewl97qrawnGiH78i+6vlCYb0ObP1I0nVBCWWlJZWruHQSzpq0iihBgBPzaCl0oXpefmnJ9QHXVv25AV3QYVXhoxs2FePusgNIBrhQRyINZ0XshWSXt4hKKgxW2v1AlzOurGZYPYabHTsGrQPG8dVpIMdjJbkegQLgm1Nx7V1IYoZgjDsSVuf0kb0JqI15Y3YBf62ddr6aCx5GX1xLzjawv0V8Qjn2oZ7OtuN+txQVFtmBXdtIutLpXCDB1T1jyDFLwvLs307uzZUrQwvnCC9bRN3PdFwlhGVx68P9SdbNkyg5/EzeCnuyGdaa76LNcPBD1+1A6a99ZEpNIeNL3ofVzKMNsElf9bhPIoaJ4KZK0Oet0DPikeWoYxZJYzjyiRTPFu5wQlTjOlqDZwfruQ2aHMKiFbrij91BIyNl00XZ3Obr/jgDG92854+zgnExzSltYdF4bUTm7chgIZ2wlUyfpYHuYSYUSLY4+/wlsZrBAXZZsztzbjtXg64ynzbY/NDj1BJN1hGWVjJ6Swrlco03rN+lBRfSXOxrDo9lObU7DasVyCOBI68pTxyU3BV9A1RaOsFN9lBLe4Z5+fRyf9f78orABEF9epleDzwP+f/y+XA0JuXbkxxGYoDa/7tDy8cB4vuLwPuRf+D4r3fur39R0n98eqm8ZJLqfqxcp230PKz8bwe0n/+tk+OJxPB4cz29ubw17y9LGie6n24nud/WTTW81UXa3s+2gdXbevoflvrt+Zrh5a5eVk7UvlPnfp8leQI4VG9N8fY4+w9epv81mV7LBX7y7TZ6vhb49ALQyckSr37DiMVbUJWT1s+3U9OR7vR66uW3/wN/w5/kricAAA== -->
