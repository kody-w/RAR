---
name: "rar-cowork-cookbook-dashboard-create-background-job-schedule"
description: "Produces a self-contained interactive HTML dashboard for create background job schedule - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_create_background_job_schedule", "rar_sha256": "9afe79e15289dba2707c02e3f2aaf14715047420249f2113b2496d5a5edf5de7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_create_background_job_schedule`. The original RAPP
agent is preserved byte-for-byte in `dashboard_create_background_job_schedule_agent.py` and in the RCI capsule.

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

Create background job schedule Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for create background job schedule - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-create-background-job-schedule
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_create_background_job_schedule_agent.py` and embedded as the fenced Python below (sha256 9afe79e15289dba2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_create_background_job_schedule_agent.py` first:

```bash
python3 dashboard_create_background_job_schedule_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_create_background_job_schedule_agent.py   # or on stdin
python3 dashboard_create_background_job_schedule_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create background job schedule Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for create background job schedule - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-create-background-job-schedule
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_create_background_job_schedule',
    "version": '2.0.1',
    "display_name": 'Create background job schedule Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for create background job schedule - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-create-background-job-schedule',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-create-background-job-schedule',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '45863b4ef31448fb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/create-background-job-schedule'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-create-background-job-schedule', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'word:schedule'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardCreateBackgroundJobSchedule(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardCreateBackgroundJobSchedule'
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
    print(DashboardCreateBackgroundJobSchedule().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZOjSNLmX2Hz/VDVr6qSG6QaG7MFCUkgdIG41NVWxX0f4obe/u8bSMqs7umZ2em1/bAqq0wQEe4ej7s/7hHkry9mUwd5+fLlRXbNDNqYSRIGbgmZmQMt8y4vY/Arjy3wH7LzrC5Dq6nzsnr59OK4lV2GRR3mGZh+KnOnsd0KMqHKTbzP02AzzFwHCrPaLU27DlsX2l72IuSYVWDlZulAXl5CdumatQtZph37Zd4AvVFuQZUduE6TuNBnKC/crAJSgE0DZJV5V7nlJyjLoRVOkZBpA6UVlLmuA3RZA1QHLtSGbueWr8BItzfTInGrly8///LpJQTXL19+fbETswJfvazeLFnejWDfbRByS35aAIQkZuaD0cUAoMrAfeGWwPIUfOW4HvS8+zgt+xP03/8dd2bpVz99+ZpBz8/Xl+mf1GR34+rcrGpgq20WphUmYT28QkzSmUMFlW7dlNkdQ4B05r8+Zv6QlBfQ36dnHx9KXn23/vj1BSBUmpMfvr78BAFIv76UzXT9OkkpPv70muQAjo8//ZBTNVbk2vUkDFj9+u15/xQLBv4YGnp3rX8HUh8et9yvL79b3PR52D2tE8x8eY3yMPv4EFyUeetmZma7H3/6V2IB0HachFX9H8n9+SE4cE0HrOlp+E+f7iD/As2eC3qX+a/VFsCtf2UlYPibuk/QE6h/JfuO/z+ITkA2VO+I/1Nx/2zC7O/Qz/9ybf9uwifI+/qychOQd6VpJe4X6Ndv8olb/vzB+fHlh19+A6L/j2LkvCntu4RvqZmFnlvV3779/KG6f/3hl58/NAWINddMvzVl8s9k/jNc73r+gOBz1Mc/zgX6lSzO8i6D3iMd+jUv/kf52yukmkno/Pi++gL9Pl+mzwyaFvGm9AHB73KmArb+DsefXn4DPJGB1TT2/THI8v/6L2gf2mVe5V4NyXbe1BBwcB2m7mT8JQgBPVX33C5dgGsVAmCf40D8Tx6eLM496Pv/tO+cCtjxwanwOxd+e/Dgtx88+A3w4Lc3Hvz+Cl2A/LwM/TAzE0hiTqevmem7WT3pLkoXsGJ7Z8Da/Qz46PN0MbHm9/9Uxbe7tNdi+H5n//DBVtKSn5iqAgNep9VqgZs912aDguH2rt0ARUluA6u8EFDtJ4BClSeA7esJmSoOkwRywhLAkJfDXTZA78sk7Pv37xaw7mv2oFYcelSUCgYD3s2BPn8Gy/OS0A/qr5lrBzn04dffPkD/C/p3s+7CJx0nQPVP3wALBfl4gECuNSkYNlUVQMWmc/fNr789QQZiMlACgSdDL3Qfk0Gsxq7zhri8ZT5jJAVZLkAaoJwWeVkDvobC+hXiPejdXqB0ejQxepBXNeS4oJg5bmZPdcoEy3lHMstrqAIBWXnDJ6ip3LvW71Zp3k1MQdKb9XdovzyB+pEn4Mdk5n0QmJxnIYD/PR4e3wMh5YcKYt9EvEKHKTqhwizNIijNpw7PfPgF1I236UC4CSpq9zWbCqY7QXVPlQc8YBBAxn669PPkc9AapIAXnOpN932MOVW5y73alV+z6pkGZjm5wgZlASj1m9CZisPfniFVBXmTOHf8gKX3Uv7wgvP0yj0Gl/++ZeD/seF4L/PQ1wZDUAL6/7FZmRbGbDYSt2Eu3AriDhfJeAA+WTc55tGqgX7hbso9uX70EG8M9EbEX7MkBNFTDn97jLy76TnmQW5NCWyQGAl6W315l3sP4Skky3IKfvNr9sb4nwBcd3oDXgT5DvJhCsM3hdPTN0sDANp0/6P6310OQARBAsIUKhorASHkASAmLIFV5ZSGT/eAeHanlOyC0A7+sCoISAdhA+RDwIgQJBaoCnfoDjlYJshAr8zTH8PDqacqHt52INDYuq+QBjJpiqYKpC9ojKYxAIUPd1FQ6gKMgYnvCFeBWTyMmXrhp4Hm5Is8nULhdx54PvwR+3dbJvOBVNMxa4BlN3Gy4/YPz77b+fQVMDadsvU+6Y/ufq4V+n1p+tvX7G7jexkAJJBMVf134EAgntPqzroTh1WAh1L3GUAgEu4F/PVRgx9F/t2WL3/aAHz8a3uEe1VV/ui5L1BQ10X1BYYflfCtEL4CBoFBjISFW/0oip8f+fb5R759Bvn2+S3f/iD/AdcX6K/Z+AcRz+D+AqGvyCsyPRJD252i9/kBkCw/s8ZnYnr6NZPcH75+BsTEw8kwpfZbUXobAiqTX7r+NPhRpKqptnWgnN5ZGXjja/YeD89sAaSf+VNFrfLfZfG9OgPvPpz3XjzAo6wGup2pt/PdafeTTOZX7suXrEmSTy+Zmbr/+a5nqhMgcAEm05YJJBHomOrQvd+9d0/TzR83gvf0Arzg5F+mLPsETZ3uJ+i9af0EvW0j7vuzrAH7qJ+nhnlSCYaCX+9j33eZlvsCtm/1UEz2P/ZGU5/27J//bMSUXMDiO9tO1eyZrZPGPwkBF77vln8WcrxfmMmTMqranCp5WL8l+lsYfoKAB0ECgpwCVNmACX9WA/SU7q0BJdOZlvsDvx/Lyh9r+e0OQ/3YYP768kYdTx88m0kwHOQoSARQNGEQrUAhuH/EFXj2f91mPuUA0gPtDRC0MD2XXrgoic0XgKkxGqFtBHNxDzNNDyVolEQImsAQjFh4GIriFrigHNIkXccjHZcG8h5R+m3qEMLJNhfxXHyBYraDUxhJEguUxsyFYxK0aTrIfA5UeA6oCz+mxoAxnwt+LHBC873jnYB5rvvXF4siwMgtUfHM47OEF6pJa4R16K1FSXn+JYN566ZKyO26zs1Od6QuW5iCwIwNLbncriK7q5zy801M85tLbXYI4wEADWGRjLJNZeulVxj5uiaWlyEWh3nLwhmgZIlj5IgbUGKnRvuYalQ10dwqsm/X8HoN6cuOXbWiTK1JpSrKziJh2OW3i0K2HHMgLnXWtjC90dNUVfO4i1b7qGoURNEz4SqTspDbIoJZgZKmGi7CdbJLliRzlTf7GS4erFvv+wsDFNQLDVNk2m44rL9pS5ILSzwU5Vb3E1S05QNyZHPnhC9mXlvOZye9UHCLmrc6OQ5rOtK28sU9JwSqkWpy0zSq5puruRGs0a/sMd/oRKSpaiDfQmKjKQOa9O2WbgS5yxKYlfY3YTcgycqHT6GNKp6u3rrqjF+1c7nS4qobsZa1xVwphHGl1g67uRV9siuzJZXwKLZYgzbaNtnbyVtSWCPZ9CitmJrzldU86hxCj9XrKATyImRGJnT4/YYUVJc0NqVg1caged6xG9irhcSY3+2GfjvHj8qIKc16PjPyunZuSIyvZfFcZgQp14FkBDMsO8iUUR6XtpZat+B4iWYYU4SbbmsVt9Om2liHJeUKSOJoB4XG1L4evMq7HURe3rOUWyCEgASgRdoX4qm8sah3UNrt0bVOlxGgJW/IyG1MvdWzxbLcWo1fZweC3KqRCfNDbdGafY2OookuuVNn+d11k7WxSpg1qlgECI1MNZULY1a9k3LwIS/3mJEO0ohKVFhudPza8Xp0zNK9uPTqa2jvC3LL1AYZrFPkxMOc56n4EROrdjlu3LFfkntYzDvlWl35mNe6ajBp4UaNwg1LL+r6GuPleLztQOKaFQJfqmXLsvDOPp07L2Dm3Tw/7FlGu8HdYcy4wYNX/SLYb6VG8xf05sDETYon4jxFLD4fzcHl2q0q55V6MagqR3rDYrenzd5MSV6VuE6Z7UgeHVFveTku3UspyjYo+2Pqdc6VKuMg3pOyhl3y9cn1VY+tVktFuqimVKxpPnKixj8zTtJ0xJ5cjuc2vCXqlTAubL/Hs/Z46I4RcZy5nuliPhqmko2UyjHUlgolmjtt3w5Cc7luEcEfqSqjPHnNZp7UqhuvD8cNsV1iTt0u2hlPlNpNjANhQOYigheLQbU3twHedvx8x1jHQ7TPb8c2Ibrq2l919mgMO2Z7TJYjzPYKeUF2Gl73lTHH7cDe1H60SzTORzcGki9RRDHjqj3Ry/wwC/GzWM8zTloFvbA993oWHbiq93YWllS4rh2EG1xegsBApZ1hz07OYaEcr7TC0RKhIXF9ATxkjmWYt1xTCkS4Qtcktc26ra3X4vG6EULqykQwuh9Kvy1Djl7PZvNYLiSWUmGEX/LmGsnNtdMOJZVs64rrxYI01JpnWhKlGqWpUIpeLR0+MuUdEaX7bD8QSJHulHV7a7RhtcV3mDas5yGx1uUzEvKrrMSVRGhAxPawgLLpLSGsCNeTA98qK3MP7+XURuYSwdEhdaOl47Vcl1KTz9akhS5P5YgXlAjjKULdNoegXVUFP3b4mBho3MyvQp8MO88hhVgRAqoVEvdAHQLWiJbbAd+VHseS3DCPBRcGswYDa/ujigUBZXsGVbNDWbZHbYn0apbiWbgiur2hIMxuzFeqmOLzpZxGgbG3euTGsyslY0Kjac4HDltYY8gYI4Oy5+2Umo7M9wqxlW8YK6h2dc1WIeFL8lGZj+eLcJORcj7fCQRBX5KelVnVIvvMx+xyhblDTC76a7ZLCCl1HVhnMbstB6KQOD/PCx7farQ0u8iRsINjOjHLfWQoiw4x19nCG7vovLFxXbGxzhbDgt3qOEyPqtfz9HZONZtIWswbo5/nXrI9MyLrzEwK4c+byg+Q4mZuD3uSuJ6vTJEgzVVlU98qKbHsk61rEisxFzQbNmSPtaOUyuMCMWNXcWxfk5XDDmeJMO1crjBokLfxCpblQk0vghZKXgFkGygSzimbSvN2O79tBXt19R3B3BjesMfWzmW7VteyHrTrucJf5q4Y1xazQ0GXKZD5Tjd7UN8X2ZbpVG5TRLK+j6ucPrlRcCAuGL6p62W3NztV649ztwV8aJrYvNHrdN2EtHVuXeNMxTeBTywTGF3ix5nadA0h8Upa1ot0e112/tUdQkFco4cLz0dVaWDXvB3Gm3Gi9zXrBepSMce911DFdbfi8x1bpY6c4juTZwTHgpcYlxVixW3s4kYtbUPTIsq/nI29ZKP2aa4fVrbACzpSS8MgJ0x3vnIsoWGbbQfq7Gaf0MnglOIZ7spkFyyv4bJZY5oqV2p68NxrZVRcDuqot4Mzd3G0arvIlwRV9eerG9/wRb87WXqkbtagkQjpZKMjp+MidbAFR1z3FHo4z3ZyLcPnyEKqGs8DE+xLk7zPdRMrFXJLjDWaH3jx3Kgo2A6r48wnMkMXLrs1NgjwJU8Fat+LNbdeqnQu+zFicrN89BeoVBxCUo+3B65JV16e8HkSDnzM8NGc0dfmkfFRb7HzZxpHJzB9TgQQVCf94tHN6iLFhFm2MmL76wsVM7LOktiCOc4SKVOSvSopJs64cpDRBOw1SLuWh1shKBonulkKX2uB2EUogp6OPjq2e12mKVJpCtwdd53OU+5lUVoOZfrXY1pyy1V0HWAL8yWuOncKv6Evizrm8HPkX9FgXqnnVMul3SafRSHqxsJB6aMy5/zDZVSzC53cGnWxiqRTfDU7KYx3xxu5Z6WxtVLzrBR4Xuq8ecC7Yp+WvUw6t7rMZwzlMp20nJk4UZ8dNReKvkn7q59dlVl13ulWeFtuT/tRNVWtW60HY733N27ssk16lttaaLnDsamHNOy2smb5a3I/T4rLYgzK7UW2FcsKO4et8eNNPDicsi8yc02sfPoEWg1eVPqQSHj5KNuiry2kRtpfHcDlR1E090Z2EKW0wDCpktxu5ao3jzOuXmmGepduMrS4zLJdf85Z0jpG9QqRthQW54Nd6OO4TrkDXOwEuJpl5+xmeZuuPKfkapGT86MK+nV/fy1PhyhFKgOd141rWOpY79fWXJKVbFthUVkcTge1RyIndOBdUWL5DD26rtFmzMptQpkiQ1FKqFjgFrZy5PxzgTt8fz6oSJAXYYqw6DXIN2OdMbjNq6cVma/XK+Wmj3qkpA1dFiTOIpi6tWkDEML2Yp0Vc4FYuzjjVmYYmjOhW7UCcwj9gZbtmlEKsT4HCuYFySZ0qpDj8gzobYpxiTr7WXdA0sumvTEHTN/MuCHJK7c+n+UZP8odLDbYIqn6gO6yKyjgRG3GIPpRjO69uRyxS/c6cy5aacq93sQle5SDhTjf8gV32ShLVF4Yt5wufCEw6FWNJWAnsgIRcK4XhwhZR90G12dUbF8x2qY9Pdjk8sj42xJPtKAZl3rdIUscI7kZnGc51+w0NkgWi6KJ7BXMonGRXJFK9nKv1numbjrkBseRkI/NZhnFc8fUjXTeh5dyzw6dkzLVsN9fU/HY2RsUBKsfbDD7pvcxRWskVZ1vzZj6zIFZOaW3Wixt6tiXFM7srjHLyn3g9RW1WHEkqnF4rMZZwB33WFuFa7aqTHUmBfo1seHUriIHZG2xPG49VR+DarbxS2szs5krq+zrodZHWeXWOt4lKpWRC4UJVu7CxWqkx4dshwv8HJaqrKe2yHpGX/WxaekmNVeyviDsQ6u10nFOM/MmCGsaxW6r4Ir1xCUXE2ZXmHqObyuEQNUj5SUXDbPXsdNZdlR1BW7oJ8toDWPhRAe1vqzW/lzSh9iM6f603DYhPre2wqzbVGq94Zs5lnUmXXsJTnOrcO7XcDPLbbALxgRdSXLfkfUZcj2OV2pDnSIPRTXs1qJsLq5IsOnRM51N5TV1dreGDGu6O6I+rHbkLqNoGl6EwaIru66MPBi9wNvLoI2to8BMidFnqUiOQXBs27M45OqeWp56+7DasSPTWshZbmh65yFrPu6MJaLDx4rPZAbpKHvOri6rYTXEh85ieTuYWXvieOzqGGlwu6Qjo2KbQt/jxyCf09xW01pGWWV6Ni8K0Lsf8gt/IzlVSDdepwpepnGNLjJaB8AvNf6EWvtDj28cWRR5o6WDFeHUiaMOa7jw+JmMHXifMtxc170rjuG+sQ+4YUzP+Emqd/sIbYMcxXdIO+/KuQWj0VhvBqah8JECu9jljt5sMrzTtudFQ84kZOR0C20ta6vtz2K5Q6trZM4WCenSbKmOZu0QR+1wrJx+D7eZbdVzX0OWy5a5gLrnigdfp7f8db81RQ6NM8SsTyLG924FDyquiMvzmiaTgJyHZFzP5bpdd+Rc7k5Ivu2TxLZn62U3st65D0hslQ8XbOtkYyC2xznR2EeiAFsIf61zJ3FW5smsZP1hBq/2p7NnMhTH1aJrtXUlIydgRzSyFz8e2JpGQLe2W62MwL+p7aI517pqKYEIn0aRWIXB0GW0BsK5DnBPt/h1g2Dz7Ho4hmV67TRRWtllura7I+vwQndrwQZvsGJbbRqepg5lVpdSjYfnKhirLWrwArwyln1HbPrAp+fuhh810d9f6kKHW2MwFiRRigjhb0XWOCQsNir4crwdnDWcoBEYpdJeGJibY+IY65xoXGLrro6EMO9vjJ+dqLUvL+CUPEVM6HvM6O2E2Dtw/HGF2J4sSI5C4tKxI0/FAjnWQEuwteilX21xNNNgWGTadaZ5Zo3QdElp3briWJBZLi3nrsG2ZtiLWFRdVA/GRh0zctXEGNSBFykuziiZote10xazFUyLNJ5yZzyGuxTFRB3LfJgzXMU1/DRiFEzlXARP29mmP1AFxpnHwJxRbkmsWhk2s1yL/ZSV4zYkZ3CbHM+KTKv1Akhti9OebGaHK1EtopYTA+vsloMZbG7YUWG3Z7qeMYwZCYYcCCnF27RNOMvj5aCjdWjqjoWDzfiidtALbtCcwQmmiXiYPBt7lIkqwhMDXV/vL6dQak/4ngExsiPcZKlgK8xCrgopn9D6JqXnjYcN4XlFD61VKxkuZ3lrLkADmVXEGAkElpBIXa281kO4Zjk2ibucWZHiGcVBROF1uJ4Z2gJtz0MDG0M8Jza8EHmFcmmiszRgpDqX7MO5VU9ZlSKeRqfMfCwS/3RinFLozB3YQZ4N2QLtorbMrB5mdVziU8WVHLJc8JXFSgtcBymGqpFLb61sfgzGBTsK89lax3Znhnn59DIdVD+Pm//y++fp5O//2QHk46zw7TXU/ajZNZ0vd11f/rppv3x6Ke0QGPY4dK2Sxn8eTf7Dkevn//QlxiRleLzind6e9fXbaX1t+tOfLb2EmdNUdTl8q/KkuR/+fnqxmmr644nq2/OQ++W+yLS4n5i/KQbXppOGWTi9gP1W598ep86TxvtrTrD7DH/c+s8DaSBgAJ4L7eobTpHf3LKYFv18NQLWir0ir+jLb/8bdSramDomAAA= -->
