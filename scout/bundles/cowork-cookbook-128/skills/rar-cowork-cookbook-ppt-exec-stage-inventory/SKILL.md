---
name: "rar-cowork-cookbook-ppt-exec-stage-inventory"
description: "Generates an executive-ready PowerPoint deck on stage inventory status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_stage_inventory", "rar_sha256": "769cdbcd4aaec60e3e2e2bd8926c7447af43a00a232c6f46af7647cf37ecab94", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_stage_inventory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-stage-inventory:4967e34a17942442bae6ea0f8672e93f385bae32b46a888d0843351c9500c070", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_stage_inventory`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_stage_inventory_agent.py` is
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

Stage inventory Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on stage inventory status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-stage-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_stage_inventory_agent.py` and embedded as the fenced Python below (sha256 769cdbcd4aaec60e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_stage_inventory_agent.py` first:

```bash
python3 ppt_exec_stage_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_stage_inventory_agent.py   # or on stdin
python3 ppt_exec_stage_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Stage inventory Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on stage inventory status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-stage-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_stage_inventory',
    "version": '2.0.0',
    "display_name": 'Stage inventory Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on stage inventory status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-stage-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-stage-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7174ae9dcd7a9dde',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/maintain-inventory-levels/stage-inventory'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/ppt-exec-stage-inventory', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecStageInventory(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecStageInventory'
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
    print(PptExecStageInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6a5OjxrLtX+H2+WD7qKdBIB7qHY64gJAASYAAIYRnxwxvEO+3kI//+ymk7p7xtr0fETfiamK6BVRlZq3MXJlV9K9PdtdGRf30+qT5dg5t7DSNI7+G7NyD2GIo6gT8KhIH/IfcIm/r2Onaom6enp88v3HruGzjIgfTN37u13brN2Aq5F99t2vj3v9U+7Y3Qkox+LVSxHkLeb6bQEUONa0d+lCc934O5I3Tdds1z0BJVqZ+60ND3EaQG9l129ytae00ifPwU3kXkxdA1Quwwr/a04Tm6fWXvz8/xeD70+uvT25qN+DWk1K2HLBFm5QJ77rArNTOQ/C4HMHic3Bd+nVQ1Bm45fkB9Hb1Y+OnwTP03/+dDHYdNj+9fs6ht8/np+mf2uVQG/lQW9hN63uQa5e2E6dxO75AdDrYYwPVftvVOVgBWGANzH95zPwmqSihn6dnPz6UvIR+++Pnp6KcwATIfn76CSpqoK/upu8vk5Tyx59e0gnRH3/6JqfpnIvvtpMwYPXLl7frN7Fg4LehcXDX+jOQ+vCh439++m5x0+dh97ROMPPp5QJA//EhuKwLgKOdu/6PP/2VWDcCXk7jpv235P7yEByBUAFrejP8p+c7yH+HZm8L+pD512pL4Nb/ZCVg+Lu6Z+gNqL+Sfcf/H0SncQ7i/R3xPxX3ZxNmP0O//OXa/tmEZyj4/LTyU5BYte2k/iv06xdN4dhffvC+3fzh778B0f9SjFZ0tXuX8CWz8zjwm/bLl19+aO63f/j7Lz90JYg1386+dHX6ZzL/DNe7nt8h+Dbqx9/PBfqPeZIXQw59RDr0a1H+n/q3F8iw09j7dr95hb7Pl+kzg6ZFvCt9QPBdzjTA1u9w/OnpN0AMOVhN594fgyz/r/+C9rFbF00RtJDmFl0LAQe3ceZPxutR3ED6W1J/1bbCbveSeV8hcHdKd0ARdpe20Ka24xQC+TB5fFpBEUBf/697Z81P7htrwmXZfpn48Mud8b58MN7XF0iPgLqijsM4t1NIpRUFAkMAuwFF95BouuxTP+kCdsQPrlFZYeKZpkv9v0Ff/0r4l7ucl3KcjP6cAy/YwDWARP2sLGq7jtMRsidWcsbW/wQ4FDBHXaSpYwN2nn505cuExCny8zd83A9e96G0cIHBQQx49xm4uCnSHrDghFqTxGkKeXENIJlofWJugOzrJOzr16+O3USf8wftYtCjfjQwGPBhMPTpU1n7QRqHUfs5992ogH749bcfoP+B/tmsu/BJhwJ4/44TCN0UEjVZgkAedhkY1kBTEACSufvp198eDpisA5ULAtkTB7F/nwykfXP6tIKHV95dAtY8mejXb5p+jxs0RAAXKG4BWiCjm+fP+SSiAEPrIW78dxAfkx/Qv/v4oWfySfOGIfBTUBfZfew93iZnukXtvUBCAH0gBZYL/DpVSigqmqnKln7u+bk7gpl2+82FoG5CDciSJhifoa4BS50kf3WA6AmcDFCR3X6F9qwCqlqRgh8TQHf1YHaRx5Pj34L0cRsIqX8AMca8i3iBJB+gCZV2bZdRbTf+fVxgPyICVLP3+UC4DeX+AE1l2598dM/fe+Rp/9AfcO8txffNxGpqJj53KDJfQP9fGpDJUnqzUbkNrXMriJN09fwIq6lZmlb56K9ASwCBluKRI9/ahHdGeefaz3kaA1fU498eI4N7JD3GPPirq0GYqLR6lz/ldH2XG7cgHiYH1/UUw/bn/J3UnwHEwBvNxE8gbZOJBIoPhdPTd0sjkJvT9bcCDz1CbVo9CGKo7Jw0dqHA9717vLfRBO47/iA4/CmzQPi70e9WBQHpAGAgf8I9BnAC4r9DJ4GsAJA+QvxjeDy1TcAKr3OBtSBt/BfoNEUxiMQGcnzQ+0xjAAo/3EVBmQ8wBiZ+INxEdvkwZmpg3wy0J18UGQiR7z3w9jB8ix7vW7oBqbZntwDLYYoTz78+PPth55uvgLHZFPr3Sb9399taoe+rz9+mlAM2fmN60HNPhfs7cABP19kj6kBJTRqQ1Jn/FkAgEu41+uVRZh91/MOW1z907T/+Z439vXAef++5Vyhq27J5heFHcXuvbS8gV2AQI3HpN1Od+zSl3ad7Yn36SKzfyXvA8wr9Zzb9TsRbML9C8xfkBZke7WLXn6L17QMgYD8x50+L6ennXPW/+fYtACYSA8TqjB+15H0IKChh7YfT4EdtaaaSNIAqeKe0e2348P9bdgCKyMOpEDbFd1k7rWny5sNZH9QLHuUTqXtTuxb60w4mncxv/KfXvEvT56fczvx/snOZWBVEJgBh2ueALAFdTxv796uPDmi6+P327J4/IPG94nVKI1DBQLf6DH00ns/Q+1bgvqnKO7AX+mVqeieVYCj49TH2Y+/n+E9gz9WO5WTwY38z9VpvPfAfjZiyB1js+lONLj7ScdL4ByHgSxj69R+FyPcvdvrGCSDaJoIG5fYtkxtgpwe6o2fIn1Cb6g3gwg5M+KMaoKf2qw5UWm9a7jf8vi2reKzltzsM7WOT+OvTOzdM3x9l/xEu057yX7VkE5TvpfTLJNCept0bpzuy9+byC1hVPJXM7x6FU/3/8oi6p1dAKP7z04RfHYOO+XbfAj89rADmf2tLgQRADZ+aqQWAQdIASaAwl5PpoJ553ymYbsfeffz05fXPetk/zfHXxZIgfWxhz8nlAl0sUMf2Cd9GAoogUX+JBRiFg1sY6iwIm6IoD6EWGIbP3SWOIC5CTjZNfsvsN+XwfEIcmP0B67/dVz895oESgOIEmEgSS9dzXG9h275LID7moz7qeNQSJVxysSDtYIHZCGKjGOoSAbAvIIkF6QYY6bu2s1xM8t46vIcxX9676XcfPFL8CyDDLJ5MRW3bpVxyvvCWpE24PoY4mOvP0blHYj6CAzgoyl+A+R9T3/wwuemx3ikyQXMHWqt+0vPrm1+naCMWYCS/aAT68WHhpWGTJ9JRI2dZE/7ZMmHBiY8VYZ4dQ0Ia4lLKUsLqTG6hMSUYHSeNIjeXXDWU7aNXb+RotaRzUuT7Lvc3/FZKy24eNptKk65ihrszb5aDZ0eOO1zYRdUZIosv3apGRnx9CnrDEM1ZWonSzNqkp9n+FvdXnTXMRekHQXTujS2+PWlJbbH4cY8Z9rZMu9nQaqeMGc+HQKMctCKPh8RKpaRKd7GaenViX9OTxQvG+jB2yx1up9WQSdewwmhEzvPror81Vzd3GjSIScV0qNlyRZl2K7BaL6wDoUsr55h6TqNraSU5dpwcTvv2bCmujLGlUg+pdXBvytZb37Zu36UZeTlmpyo7c1vP4E/lMV/P3IaMS9fCT/bYHfrNGHbsOOd1Cjk6mV+ljaSuNXPba3Y0YHsqMQzQwmJnfLO5YSZSkaU/52yUU7JY3aZaMlpIk/L+muSzI8kdqwRJayZoNZts2vktAXubtBOz2lLmtzzhxL08JByGzi/spXPTqGndDU615jnNbF13LXFEjGUC1wwP3GGnLOXNbaPaNu7YxqmVOFmhXC7z7ICyl7MUofOoNuqTHkm6nLKHcre8HSwGcVziYl+pZqvKrCfYi+xQbW8ZUdiRMDf7fDTOMHkdiu7Ml7nRopjfKrFkyqbOkrC547qYP543JhqUjrgRyHbHCpVxwt14cyR6Uowd3dleh4ZyZsV4dFibYwKqMYxklywkHjaP2bY5w4sMhJR5DhZcK8k3nis8fZQ36SXbnJAIX+GXJRroR5MgiorkB1TDomjR+utRKCwhEcyxIbZFWWphguCRbbVsb65lt99fT7BesTDDzHBXoRcgDKmBKubymj5l8EK55AgBwzlJbA4WjxP1rVJ8XEylXj3f9npSghhwTrqQJ3Z6qtZHVEZXHLrb2YI5XC9HckdUyom4DTv6sMO1A+2BTE3F68jlcgQz7S09HIxwj6snVC84GD9UM3ZgsmKMKuSy3V7X0lUmxBWzsiwBJ9juEG1Pqqobmb/hBleXcHJ3cXfFjO3zC5pfOF5kVY4QUDpViYV2NWcXSUUbWDzs0dtcamPk2hWIM9SDYxkFMy57nYXH2YDOLnFRjApl9XG9ThRTu57MBaFSqyPVF2gzngoCzcP4mq/b0OFPasKmjAJre+zmrhkDpkIivM3m16IpucqtBcBZOO5YW+lwOwZrmDnlxMqjm57Yq5sAJqkdzlUxzLMEboRwWMfERltKNuaTaCkeGcs49Xx5dq5S7kvinlgfwX1vG3UlLBZyt4k9Y4zCE06ER2l1W7DNtpsnTX3E3V2ozogkiHWj2R16rjfHODbYvVTlVASXnGIZa7ZbIjF+UTKNWuSW4JptwTU+n+WNaHhItuUJVSuT9ZVpJc1KrrkpJ01pS6K2I/qDNQz5Blexja/HBTcvFH7pzLNauzg5nhwJrzDt0d4NcE1lu0MQutk6MzfHOUWvVmR8rUl1ZdcGqXdKdFh28mUF+F7I6dmWPPPc4ooL1FbbL6QzcbqptI+yriXHqZLp+Jo5GnWsmhert9Ld8hKvrrln9LPwFC4U1QgC4EP25PXndCsnhttjC2vvW9U4EgZu92IjIx5C64v9EI3DcUMcuJ7awCtvnu9NYeyO1CrJmWgRua15MVJphoqrlkV0mt0Ly9N6s9Gq4+aq77gU77b7nTqcD1wlAoLWL+JabDf+GqHOy5JAwlIgrZNqFW0ghpLee65/bm4JSCdSkfs8xf0e1KTiyoVRYlXXNApK75ikvLgcz1h2Q0RmsRVXl3mNFy58alaG6c6uHcrQXLBLKEtRSrAv1z0hp4oGMXT8AG+3YWR4/swh44SmT8OZOLbSKuvcsRGSyxGsXybC60FqYf6GjLF/OTNrZFN3ZijNigwkEqoeR0XrWb877MQya62YVNWzPJ4a78TIHUMY11RFSbmiddwrLfsMyuOSOBJpjK06HTs6XM91pH2w5MTLrT3TmORa2xZVyMwwTlnvHc/dHVt5IxNjK2fOuKlbXdFpA+uYQRSaFWv0nmiphY/zWjBc2mzfGaywtweVumYklaC7W7vIt7mysbdXwte7041XrOHCLKNddSi66GiKc4ECLYK7ctXV4nIo5RNJcvtxXdKjl25UV0T3/DYPUdtwjQQbgkbb872W06BfADVH0mKTQTlauJqSh2aVLciCuzJTs8LE3X7FRatut77qR2KXr+h8u6KrOqsdOCIPMA0AUtDDBtPWyuJgbdYqF9ADsRUXW120cCq3x4Wcro6lXOjKMApdpddHtVk44m2vrumI3oo1aVAVFt28MmkFg0szYbVbpLXs8Xadnvappm7Fk2gVFRLicHM7Ep164CnSOV5Xi3I735Fx21th2XsCMteGmg46rLsURuzA7uV4vrAidjsVlqaToJhySqGf+K2WX6ULQoJCE0adUG57bkemY4LEe0qilVOzk9arhtXzeEMyPXe6GOx8zShEPdidUu+rk8sw1WyrrsmZ1O16NNpqvETTWR7AZ/60jGD0cloXOLfLm4IOu9VYl5TbCrlc7s5dXIy2G+wOHkbBvt+SfmGrax6hrsy8sHLMjGars3065725mGPZrjTmboYd8d7qbutRTo9+23eSc2BX2jxmmFvteQHFLsSoopkoJAhnhsp1KioMHLGl5tAAP8pVVa+/JUQZXPMdV2jtwfYzxLZcSyXzowJC7Zi45tVATBGpZAn3Lgx7I4ktdstyd6zMbbWXO3NbXiUTkVfhZiWYN5NKq5Xfrvcyg1zzc8G6R0wTx+tA2Od4XHHwHjO3dELYWLHtDhYtV76lEJf5iHRHdOmfkgYTdqO43Gk5HK32iq65R8e2cj+84Pl8E3exuD7eUnpkRtfsk5FbifK5k1SubVL2Qu0UBVuyjEsy+yuqkLzFhrmc8QgWxA26YPBduz3xxNq7oJGwAISkEMmiZsPNtSECnb2ubWM+3kQiPXZ71NXRU9Xk/si3rDPs5rruiPSqsNCViWdY3cxDeYMHHSPvU7sRm/LgGMi84YNZkRSVfMUudSkpxvG6T3txD6+PGJm2rZgFicNTNOaZs9C7jjtU1GKXFY6pzsQnhOyTfcGP8cHZnis8FO3zKKB2s+BIhq7DXloSiYMn6sUjVs3ypOio5+61qPCaTdOtpUprt3SnlXYoEXStyvuERmYs3TLDkgniVnd3BJIy/PoQ+0fZ1o8jrldovtux8A1H54fFenuK5H2O0fEec05amLlSpguADZJAk92BFDxFFLcJ5mnn+oaUwagB0CVrKdc2PoqujWSGlyyOM09eHbVYordKXJp742hvBkmNrXC8GEHa0de85PlAKSgapRjfgDsctDg1L2Pzhbbl9oMQEHhqFGYcxksZLU6zvsoxe5205vFCDzERIbAaDkpD9hTo3FhRQkw0E4ad63qi6SbWikuvDeLmFyQdy57mIi8KQe8VDkanRytJPe914sZGh5slK3ucbXflElPElF/N1UQqZOKiGKcZ7fIWYuX9TqBLxl+zNyYOHHVOzVbaFhHH4rZS6LO2lfhAFjfHyrbmGms6c+o4V5GckjCFpRw6vxwNYx1sin1oMzZpX+YlgY/1QjjY+tldbvljZKILb7fXlkPb9F0nr07FnF8uzRDFkS3mjUKrCnlHyasZgc1qr0/Jjok7fpefs25oVi5q7gOhxBnK6zytiNCcSxIzEBxvc7yhFsVeRwHbYm7uehFNedlc624Gnh04jbNYWz6aTSSHDdxSLIUckGY/MlUvEtSyo/ttXtQdfbvyNt1XgRwOLLwj8hW8mos96W546VKQBSvB5/l5rD2/Pp/4Wze2vdywTeMgxUwaRDLySBnZEDAvNLNlEPQLMUA2+b4aEbhrgkVG9amDmYrtz7pknVt8U+qGPmfbeIN3bkHxipoRK3NHRiJrDPXVgg+ipjOh4AUjMWSysNIv5W3gJFkRlO0ZYxruOvJ4cwsJLM2yFCXTAKQeLdnETcIKW2EGhlBOWmUN1aoz5+SY8/K+3frWRhPTlFoDtjL6rC/d1XlNutJpgGGjGTDetSShOZeqh7H81fdazxyl2RbbeOVKNMI8gdVcnY1929ODRUvrXo6608VGCD9eepsZforg3AuqYNYE3uJ6WOeHdXDQdwdGt0IiCBjXW6Fkjiv6XvW6OUGe2WulbG+1Ht5O8yW5G0Hp8OtM0siBSuzlgoytbuZdO2xknYOwpdYy5keL5soGsRslgntu9MZSCvPsmg0giwa+SsjVYAeBw3ccHET+9oSKslmNvn9FOGIvEtaAcwrj22i4cq4d74W5oAf6Jd1hvO8GPk0dd+xpUNt4PSePyBWu1AU1g/XD/gD7DJGwTebpqDxfgKomLIT9cDoLY2gFbnZaXQ5nnduvPRvO54zkqT0gbRjeXyKR2BGMiWmkV5t5h3RXbueLLaZo2o3D9vOwmSU82HWY1uJ2TcN+ZeMqD3ZiRqzMr3x3s3EMNC1ktDcP5XghKI4LcFlpfJlpzmcZVkzOqplhY13R3ZLHg2zn+9VIsgtmHE4r6+i5Qju0RB9surGcl13eEabWjCvF6Eo1lne5y/YqQnHyGdRwM1/uGtZveDdXQ/WgJGc4i5CgPWxlfeEHGqMuE2yepLjuK2Tj1dFaYVmkI729rFz8psVMKpDQU7BcI4JSZ33QnSM6IPt8hlR8RjvzemG6TcBn8xnWGH3cRWJurCSspujG9E4YJpLu2GELBaZKV18YoMRitFMTRqAdQkuYUcLxSkv+pmqIjJjBGypbJY6hZFvE2889zMmxG0+ds9BmtSNfEbMdz88oQ1XU/HbA+MLtd8nsunEqBItnp1OmwUS1ndeqGMX5ECDyTr/QaDjISXGwer0qOFfaXHbGXOo25sqZt+Vs2UqYXkaz3fzMDpJw66LlLa9U5TzM+Es429lZT0f+2bdolGW2Cy1nUZSRncE6WkZQ6b6ehRtP1mJ9xY+Fs3IzRbuUZmuNFDsornhNqe1Idv5I99jMY03GUtgLA5+ZUmkOWUqQl6tOgv0HgQr7vkfdUpGZij1jhMGRFcJpbacHm5wr9Cq/7XQ7CNxb6J+RkeLzUEKShbQGmoq9JyLwkaf1Gu5DBy6SVaUIHYXAFcYhPudkvjxovnSC17J53PsXeFgJObJds9MOg/7556fnp/tb16fXOYIjxPPTdIb/dhL/7xzohre4/PImASMnAf/vzh8fZ4Hv7+Tux/K+7b3etb/+a+P+/vxUuzEw5HH026Rd+HbU+A8nqp/+6nR3mjU+Xg5Prwqv7furCjDsfugc517XtEBpU6Td/cgZwNk10x+DNF/eDvyf7ovIyuntwbvRT9PfZbwb3BZf3v6K5X57egPme7Hd+m+X4dvR/POTNwLPxG7zBSPwL35dTkt8eys0nb5Or4Wefvtf+lNpm9omAAA= -->
