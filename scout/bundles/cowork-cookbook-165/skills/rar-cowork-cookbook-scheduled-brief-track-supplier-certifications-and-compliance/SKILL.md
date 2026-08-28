---
name: "rar-cowork-cookbook-scheduled-brief-track-supplier-certifications-and-compliance"
description: "Schedulable morning-brief email summarizing track supplier certifications and compliance for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_track_supplier_certifications_and_compliance", "rar_sha256": "abd17072847e8bbad46740f1ab99e279551468c713ecd49f6472e9f4256b709d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_track_supplier_certifications_and_compliance`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_track_supplier_certifications_and_compliance_agent.py` and in the RCI capsule.

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

Track supplier certifications and compliance Scheduled Email Brief — Schedulable morning-brief email summarizing track supplier certifications and compliance for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-track-supplier-certifications-and-compliance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_track_supplier_certifications_and_compliance_agent.py` and embedded as the fenced Python below (sha256 abd17072847e8bba…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_track_supplier_certifications_and_compliance_agent.py` first:

```bash
python3 scheduled_brief_track_supplier_certifications_and_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_track_supplier_certifications_and_compliance_agent.py   # or on stdin
python3 scheduled_brief_track_supplier_certifications_and_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track supplier certifications and compliance Scheduled Email Brief — Schedulable morning-brief email summarizing track supplier certifications and compliance for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-track-supplier-certifications-and-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_track_supplier_certifications_and_compliance',
    "version": '2.0.1',
    "display_name": 'Track supplier certifications and compliance Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing track supplier certifications and compliance for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-track-supplier-certifications-and-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-track-supplier-certifications-and-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b671e8e5418187c2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/track-supplier-certifications-and-compliance'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/scheduled-brief-track-supplier-certifications-and-compliance', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefTrackSupplierCertificationsAndCompliance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefTrackSupplierCertificationsAndCompliance'
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
    print(ScheduledBriefTrackSupplierCertificationsAndCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816abOjVpbtX1Hf/mC7ybyIWcqKingChEADSCAEwulIMxwGMU9C4PZ/74Oke6+zXNXvVVR9eLIzUohz9rD23mvvA/nbi902YV69fHnRgJ1NVnaSRCGoJnbmTbi8y6sY/pXHDvwzcfOsqSKnbfKqfvn04oHaraKiifJs3O6GwGsT20nAJM2rLMqCz04VAX8CUjtKJnWbpnYVDfD3SVPZbgx/KYokgrpcUDWRH7n2KKq+q3bzFN6zMxdM/LyaNCGYVKAu4O1oVJB3Gaj+MoEWREEGvEmTT6o2m3hQUT+B6zsA4qR/hUaCmw0lgfrly8+/fHqJ4PeXL7+9uIld1x9GA48dLT2OZmlPq7jvjFpkHvduEhSb2FkA9xc9BC+D1wWooJ0p/MmDHj+vfqxB4n+a/Nd/xZ1dBfVPX75mk+fn68v4nwptHl1rcrtuoBuuXdhOlERN/zpZJJ3d19Drpq1GUCY1xD4LXh87PyTlxeSv470fH0peA9D8+PUlhybcLf/68tMIyNcXiA/8/jpKKX786TXJO1D9+NOHnLp1LsBtRmHQ6tdvz+unWLjwY2nk37X+FUp95IADvr78wbnx87B79BPufHm95FH240NwUeVXkI04/vjTPxILw+LGSVQ3/09yf34IDoHtQZ+ehv/06Q7yLxPk6dC7zH+stoBh/Wc8gcvf1H2aPIH6R7Lv+P+N6CTKQP2O+N8V9/c2IH+d/PwPffvfNnya+F9feJBEV5gdsI6+TH77pu2X3M8/eB8//vDL71D0/1WMlreVe5fwLbWzyAd18+3bzz/U959/+OXnH9oC5hqw029tlfw9mX8P17ue7xB8rvrx+71Qv57FGaSByXumT37Li/+ofn+dnOwk8j5+r79M/lgv4weZjE68KX1A8IeaqaGtf8Dxp5ffIXNk0JvWvd+GVf6f/znZRW6V17nfTDQ3b5uRgJooBaPxxzCqJ/D/B21BXB+s9VgH83+M8Ghx7k9+/T/unWU/u0+WRes3Tvp2p89vd7L89kaW374ny2+QLL99kOWvr5Mj1JlXURBldjJRF/v918wOQNaM9hSQQ0F1hUzj9A34DDnq8/hlEmWTX/8Vtd/uGl6L/tc7eUcPVlM5aWS0Ggp9HVExQpA9MXBhqwE34LZQeZK70FI/giT9aST5PLlCRhwRrOMoSSZeVEG48qq/y4YofxmF/frrr45dh1+zBwUTk0cvqlG44N2cyefP0GU/iYKw+ZoBN8wnP/z2+w+T/578b7vuwkcde9gknjGEFq41RZ7AmmxTuAyGFyYEJJx7DH/7/Qk8FAMb0wRGHGIFHpthTsfAe4uCJi4+4xQ9cQBEHyKfFjkEFvbEqHmdSP7k3V6odLw1Mn+Y1w3sdQXIPJC5PZRqQ3fekczyZlLDuNR+/2nS1uCu9Vensu8mppAc7ObXyY7bwz6TJ2+9clwEN+cZjGnyniOP36GQ6od6wr6JeJ3IYxZPCruyi7Cynzp8+xEX2F/etkPh9iQD3ddsbLVghOqeMQ944CKIjPsM6ecx5mOnh/zh1W+672vssRse712x+prVz3KxqzEULmwfUGnQRt6Ye395plQd5m3i3fEDj4HhGQXvGZV7Dh7/mcnjfTqYLO8jzH1ImHxt8SlGTv5/nHdGDxerlbpcLY5LfrKUj+r5gfw4uo0Rekx7cMB4qoFV9jF0vFHWG3N/zZIIplHV/+Wx8h6v55oHG7YVNEZdqHf5MFmgc6Pcey6PuVlVYxXYX7O3FvEJpsedD2E4YeHHD1/eFI533ywNYXWP1x/jwj32lTfiBfN1UrROAnPJB8BzRnibsBrr8RkemNhgrM0ujNzwO68mUDrMHyh/Ao2IYIVBdO/QyTl0E4bLr/L0Y3k0DmHQCq91obVwNgavEwOW1BiBGtYxnKTGNRCFH+6iJimAGEMT3xGuQ7t4GDOO008D7TEWeQoz/Y8ReN78KIK7LaP5UKrt2Q3EshsJ2wO3R2Tf7XzGChqbjmV73/R9uJ++Tv7Yy/7yNbvb+N4jIBs8kvoDnAmswvSRpyOZ1ZCQ0o88fXT810fTfkwF77Z8+dMZ4sd/7phxb8P695H7Mgmbpqi/oOijdb51zldYRCjMkagA9UcXfRTl53sJfn4rwc/fl+BnaMbnjxL8TucDwi+Tf87u70Q8E/7LBHudvk7HW9vIBWNGPz8QJu4ze/5Mjne/Zir4iP8zSUaShqXu9O8d620JbFtBBYJx8aOD1WPj62CvvVM2jNDX7D1HnhUEO0IWjO22zv9Q2ffWDSP+COh7Z4G3sgbq9sYBMQDjoSoZza/By5esTZJPL5mdgn/lMDW2FZjeEKXxbAZLrRiXg/vV+1A2Xnx/4rwXIWQPL/8y1uKnyThAf5q8z8KfJm+nk/tBMGvh8ezncQ4fVcKl8K/3te/HWQe8wHNi0xejR48j1zj+PcfyPxsxliC02AXjqJC/1/So8U9C4JcgANWfhSj3L3byJJa6scfGHzVvdPCWzJ8mMKawTGHlQUJt4YY/q4F6KlC2sMN6o7sf+H24lT98+f0OQ/M4t/728kYwzxg8Z1S4HFby53rssSjMX6gQXj8yDd77t06vT9mQLuGEBIXbjocxUwafkQyYOY7tkTRDTn3MduZzgDNzisJIeuYyGAFcj5z7NMngYO6TcLfDTOcelPfI5VFHGo32gqkPiDmGux5B4xRFzjEGt+eeTTK27U1nM6jO92BH+dgaQ659gvBwekT4fZAewXpi8duLQ5NwpUjW0uLx4dD5yXYM1FHDLVIlyO2G1kFLmfladomN4vGm569Z42JLNeXp9oFre9WcNme9N9m1QhdhziPRleFQak1bBDAcYesVDMlWJHfoPcLCvYT2V1ouBXW21SLL7C5qkhrJKdLVU3NiClW26V7CD0ArtXNeY6nmbUzu7CRH29JqUzi1xc4XrKJRNyi61waTEm5FreGluPEqxL1VfZnKOwzf9Ne5RNFbJMEVkzVOJe9tTrtSN2RrehBXxxIpb9raVOnbwGGSkadJHyurIDuIyAUTDJzrwbGmvb2JdbO92VAzJyWR/TaJ8Dk/Uzdw0N9cTydyi3uakzdbbAjx6KKH8cZQvOlxP1NbFy/suFo74HjcgVMl2vstEDaHjhIXuZSWVr2Jq44EM7EuzvZyEBwzN0MjIJaCA1g8pondXC8tENlxK9inzj4Jp0g15yGDKEKFuSkd4x5/tU4nt6R6TC/TuBS2GnY47tPhcoxOQZG4doybOc9HqbPW5n25qhPncqbxw9BKM47CQ+G6OAhTR48qXU5NFpCiROPlualVkoY6r0kRT3nlYhf6ZstY/bqaOrFW1+1mZYv8fHPcaUZnekUhG7Vxvmh9s9ZP+M1eb6cmfksqv7ALysCC67bbb09cLKvBGpOtfhbLzZrO6BzHLK71dx29DLd+gkU3fsbkzrlyMQHNbLLLtusGxJZjIdYFJ6dklJ8cAzsWWYHuSunoiE0mS/rR0nN7iUsaypy5SjpQ3cmfO7DK0+1M0IGptU60OTOHKTsfxLVy6LTaO/T4STk4e7/DmkblnDZiZLI9xOQZX+M3NzKXTLB0Cp2qj+Rya4Yy4gUp2gRph/DOgSyoBO/mZ2SKJ63kUQo9zJbUfCrNeBZZ8gzfhzqpKzbKLG6GNwwo411JVojc62nlYdQN2MN2eZzp9LmQ14mjkzNNO5r0tGwieBInqbQjdqJYn298f9wcsYvsFtzBSW3klLpCfD1wKU1xYaViITp0VztddYnskkpzChrSmi/gJk09UlNpGrla0a4JbR3stXniChy71ut+SLcuKTnsoDBZ3TZdW011vB3ao2dbdCTxqnHLtfW1XIV5uYg0tcDDIqcpfRBvfndI9uhxr+PE5qiQkY8G/hGVGgs3ZFJn5v50YMzkWHXakCgo9ANDt40rtidsF2cLBzRSs4uPesyYh7TIhEusKHJkLU5L9LYfUPZmzJ2pbaiuXx8QoYE5v8u9vbegKNU+2dfohhKYp5nzRZvvMW+1ia4EMT3bWulWxdSNhYudYLrCFJYznVVzpFnpUSnbaWTZyiKebuUNapaJeXFtkGO6HxOEwdjpVj1pNkUHx0YcSGHf02v5vCqI825Ru/QJFTB8WnC1SVQxJZS6vcS82aVh2fJ0Sth2tZQ9VyTT5e4UAHB23OU2PqZ5iRkmT/Ccv6Dm68QL+FPjZNnqUlMHzTtXDmYvt2pzvsG8Z20PDwb1RKLVusQ2N8cdHLXhDx4Lwmk2o8XpLGT4ZIGfoO45cqzQyL5mszAerApHrWXsF/ytml0Hgg58lkRbSgtaVoR8xJVcfaywBvAL0KoekBFuc16wprTe7a+m3itCyRXnK7LMm4u0NjML2Q4MeVJ2WpJS6pzx0yHplxeZnIHVStxFw+BsAZd0oit0welcNnlUZ9SSugpdKGcSZA7FXG/c1ZppTA9MN5u1IIRnExgLfiEbfdsIZ/u80CNiLdKeZKty5J6jCL3pOLDqcpmwxMw0xLPtIp09sMX5YucHb+201I1wL2SHLGH2+8s14ZtxhPuZgM2BGbLbxXbgbPmGzdGWXOZzmCZZf66uInnm+al92u9FggymotEiteUVod4v99FloJCSp1SRYLrZWhEzonf34kYhL2fBsZw0M+alF2SxrERqEKLafr2ydEu15occEKsj5lTV+ThTLFUSCT702E1UtvyNmssi2pH+oIZT7eYYee/EB4LeLpul09u9SZRZJGNDn2D4vFhY2qaMSgnX+7ySE3NH42uFNUQrp8VNPZ1xAXKSOmxan6JyODsXtTgmVDFlvboi1p229o+lwwDDt3XPYOJUKTeE0ARr0BNXPg0cFt1KyOJ6Xq0Gy1R2yVZgjhrrnq9NorSndLlZ74xWkg6Vmt18x7FkJkxsj4i4q1MCDbKTw2L2Vt+sNWyLwKaseozJMIRLLPdaN9X8nEYGHWgEe7t54WalZqSu700ar6aZjXSYTC66ub44JM1Qikq1thdFvJmTedQch9uerPSTWt1gx9cu1rDmel/C5RUWsGceZOFqq3eJ5aDy7bCsS72ca3myLjlOGna8w2rd7rq4gY3Vr7Tj+nYVeUw45gvOUAI5uJa9c2L96LZTyiXOSsV2HVDXQsF633ekcncpOMlTh0DhV720H8DcxW9xwYpREhr0VpTYee9xqp7GMrq7GqVkOusb5aAnYabA6auQIkxvztLaOEV1FNgp0xsHrgiuoO8ya65K8xu3nzZRXxrZbXWBzazXtbl2Uq0IcQVwBDSlucL0uhZOtmCdY8ZYyvhKta5Hveajjbyh1EC+WYKGB/lqsVlZDX+8tLYS7+OzugwMmkebBvpxFW3PDY+9YwCQc9GhSxmqqnR3Xp9AHk0TeAQnEHA1DzxfU3B62BU1fz3gx3bBt+7Z29uDed0BhuGxKV1HhItdj020iS2jcKvKoxGaJWXBt6bszCTs43IprkVus8CNYNm5Oy6njknnnw+2JQQrpMgUKW6vDEkWU6vZRHUsUSiLyhrbFSe10HEMsgNrb2RjfcLMoitXDbaLQuG4B3Ohm/IhXyXqiiQdOwwrk+I8ST0tzoToXqrB6KWTyNHr0k7UNXL0btkgsokGxDjfIZt1qq8s5szrxcHdsDdtsFB9NdPiizG19YLf9SkZAJrMUel04tfKMeJ9bScHq3TjwQGQXGNz1dCPazHoWbc6xJROrrvikNFwCADhen6ITwfLc+ZTxdvaK0eUV+6WnIc3cWlYbLbPmcNVqKT9zDJNRymzIyGsdLbbbi4tWUdyWdJWzOi3WbazYw2fpdUWGWirPGz0/urOLZ6SLFS5DsKVt5IFPDds3Xpm43Rh9HHSOHrcHVGa09KSEXHP6gvG0ZAu8qkVJVjC/Eb29SCjNw4tqXKRZcYSI4S0S7DjmeYXW6EPsQOqL0NLO4m7xDlzkg9gg/LxZXlhoinNCDHSCCiOxCtqEVXmdIvzRRsBan+m7bNRhppdE4lNFhuWg6RlditnTcSRkOiYguRGbIpbQVfd7Dbt1qqwQDyd01RpN9c2mVGJxrxbpQlPUrwZtlJNEMrpugrnrD1N+VQ+m75yOALvgEi9vrGUGD+erbPWIQiTzvR8q10X1718sag0khthX+bejlzu5q69jffsQdErKhG4BdVl+S6Xj2TWrXaoFEa0uw9846C3HQ7bmch0WzC3YaJtdW7RXC3BFslCytQWW50QmCfDUWcTYbmqzmxWnsXDbCGrWzk6nuSV6sog6nBSpC2/VwMgY+E1p67iyVwlboHo+Iojc94Lqt2FWx04gswGWSr4fSzRg5TMnLbFEF+KV0VN5YtjsBgcuXcORFuV15CF0OobW1KAf5xJ+hxbWEa4tkTrQGKXWK7sWjgMu0zY04rmKE2mkMeIVvf7qic979L5hx0Y9jx2hVapJ8Lytgec60SFoEzCEOCkPIsyFVmIbMnbq/3+zBjbhEmcAk7iAD0iQ0GtsBNqWocZOu3qI9bLSQcuPkEvZo3ZzcwEKNAv3rdxoXYYRK7LkIOzNzu1PVDQ8rpuVpzIrRxGEDk5vmgXZ4H6xdUoHA+181myV5SMC+fr6HAkUYnkdv68ife3HYI5SlUyg3VNmtuMvbCHIFRwDFdxdp8R5eY20GklEa3rp3NPMfkDcVh6LZn4faLMT7V8OaMWTmS6gp/5Gc0HLtii2NVeDWI8c7MrmlAU2i1Izjjb3u2KkoWflTemHFp9X514M2+mZEMtqrnZS1RekCSnkk27nrNUb2D787oe0FxDpC5Z9XvKtgIi4W6Xpuel/cEkl0ntxUS0IPk6BZQn3s7wUIJb+Hav7i7y0Ts5iZvlJODXW0vd5SeWcXCX4olQWSnHs2gLoRAL/tS3rqk+RY1SxwuPuGZzCb2tdgM2FfxwnyFA98Q1QhC+LriNYjd4bGs3o2O4zEbjvd1AwpVXGkcZm3obScxeNZqLf8ZUxK+ugoga6PVsk1oPWxmzPB74U3nYr6vZ9lIDukYPc/kktqukaoKtJCkM1yr82jGGutqi4GS36YxTe1QDMzrJ1qRIXDfIEKTSwkUbpja702a2xehmEQmtq+3wZYVXntYbMePV6LwiUoPtAsmhaKc5EOwWcbMBGziBdZdAsZDbjRJ6dnoUtJS4nNuBbbsIxSvOAV5BzG9iGpw3OFd1qa8IdkYM+l683GhBskNUZzFJPu8itJ7La1dcqrfAiovgCEeBprPOynodKub5lFQzX9/S9OW82uTE7JRx+rQDvOlszyzTZG1yijb47FgoIBXSjb5L6hbRGesa+NZCt0w4I53JrsJdA9AMjWt5PL+y1zT2W4FfKU4Olk5A8ELAwCGhcna8z6e31QrzWeC7HmtR5FYot563g4crsGtCDKtMg8k9r+GnZnuSZRnNLZvij3pKyDclyzF3r+KzM+cg3UG/buC85XEMApjVbMFtbignHlpP3Fr7CzlLr+yuRMqCUenbTqyV6bpBF+J+RuBeA1nl2uMdvfWwDFl7YIaglC7sfGmPEDeUxi59IJPszKl9MXfla8cspzevdBl3KiEHUyHO2rwInLwUvWBAyZuldoMyq1IJHqgK7xBKnepR6pFcYKQRXk6Dt3VPGKSt5oTc0kuYhlOYTux865PT3WK6iKlBx1yTIJq6ilaXAJWGeMpfptttqyrIXj9Xl4JqluHcxIEKc5EkFyCsLHKxwFZsl3HVNggHeeCnrLVDzKrqbOPaoEReAFmBTGmUNyGYnS9tOx+E0jDP/WwvsvMUk4FoIiy24uNga3JL11wF20EReW5TzdQqtjBpCIblChQKy1teW805LmvojREQgGIRpQ5qhLGNyET29UWPNJNypi6z93mh3bvWTsba5rZ3Z1dGdi8zwBQ9u/Qv1Dr0KUv1jHx2aqYmlXTlgm5m/RTPCIK7rRTb8/mwW9FSxFu2e+V4UZVZJLwtKf9y3szptURf+nUm78m2l8VrpsRuODAKjsp7xz14R5TkixWiqDOpXCwWf3359DI+7n4+tP63vPYenxb+2x5aPp4vvr30uj+yBrb35a7ry7/H3F8+vVRuBI19PNCtkzZ4PuL8m8e5n/+V1yij5P7xBnp8p3dr3t4XNHYw/nuslyjz2rqp+m91nrT3h82fXpy2Hv8NSP3t+VD95Q5GWoxP6P/G+Y9ntE3+rbDHKETZ+KoKeJHdgOdl8Hz8/enF62HMI7f+RtDUN1AVIwzPVzPQe/x1+oq9/P4/6YjLOREnAAA= -->
