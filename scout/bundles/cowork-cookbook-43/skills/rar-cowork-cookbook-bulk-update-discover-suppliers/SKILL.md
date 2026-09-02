---
name: "rar-cowork-cookbook-bulk-update-discover-suppliers"
description: "Applies a bulk field update across discover suppliers records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_discover_suppliers", "rar_sha256": "e62abca6d07946b404132d793cfb907af58fdf71a1ffd440e195a3a507eabf6a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_discover_suppliers_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-discover-suppliers:758e84ecd2fdc40593e969cfc400d92e0622e026e0aad8e8fd5269e85064689e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_discover_suppliers`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_discover_suppliers_agent.py` is
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

Discover suppliers Bulk Field Update — Applies a bulk field update across discover suppliers records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-discover-suppliers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_discover_suppliers_agent.py` and embedded as the fenced Python below (sha256 e62abca6d07946b4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_discover_suppliers_agent.py` first:

```bash
python3 bulk_update_discover_suppliers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_discover_suppliers_agent.py   # or on stdin
python3 bulk_update_discover_suppliers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Discover suppliers Bulk Field Update — Applies a bulk field update across discover suppliers records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-discover-suppliers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_discover_suppliers',
    "version": '2.0.0',
    "display_name": 'Discover suppliers Bulk Field Update',
    "description": 'Applies a bulk field update across discover suppliers records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-discover-suppliers',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-discover-suppliers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '757d5d3848941378',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/discover-suppliers'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/bulk-update-discover-suppliers', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateDiscoverSuppliers(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDiscoverSuppliers'
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
    print(BulkUpdateDiscoverSuppliers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6+ZOjSJLuv8Lm/tDdS1aK+8ixMXsISehASFxCqGssmyM4xCkOCejX//sLpMys6u3u2RmzNXtKq0wBER7un7t/7hHUr09O20RF9fT6pAMnRyQnTeMIVIiT+4hY3IoqgX+KxIX/EK/Imyp226ao6qfnJx/UXhWXTVzkcLpQlmkMasRB3DZNkCAGqY+0pe80AHG8qqhrxI9rr7hC4XV7H1zVSAW8ovJrJKiKDK6JxHnZNkga180zcoubCPGr/kvV5khZgWsMbogLgqICUJUsi5sXqAXonKxMQf30+vM/np9i+P3p9dcnL3VqeOtpCnUx70rM3hfXP9aGc1MnD+GgsocQ5PC6BBWUnsFbPgiQ96sfa5AGz8h//Vdyc6qw/un1a468f74+jT8aVK+JANIUTt0AH/Gc0nHjNG76F0RIb04/mtm0VT6CU0ME8/DlMfObpKJE/j4++/GxyEsImh+/PhVQBWfE9+vTT0hRwfUgFPD7yyil/PGnl7S4gerHn77JqVv3DLxmFAa1fnl7v34XCwd+GxoH91X/DqU+POmCr0/fGTd+HnqPdsKZTy/nIs5/fAguKwhm7uQe+PGnvxLrRcBLRl/+S3J/fgiOgONDm94V/+n5DvI/EPTdoE+Zf71sCd3671gCh38s94y8A/VXsu/4/zfRaZzDuP9A/E/F/dkE9O/Iz39p2z+b8IwEX59mII1hNDtuCl6RX9/0/Vz8+Qf/280f/vEbFP0/itGLtvLuEt4yJ48DUDdvbz//UN9v//CPn39oSxhrwMne2ir9M5l/hut9nd8h+D7qx9/PheubeZIXtxz5jHTk16L8j+q3F+TgpLH/7X79inyfL+MHRUYjPhZ9QPBdztRQ1+9w/OnpN0gPObSm9e6PYZb/538i23jkpiJoEN0rIPVABzdxBkbljSiuEeM9qX/RNytZfsn8XxB4d0x3SBFOmzaIVDlxCvmpGD0+WlAEyC//x7tz5xfvnTsnIym+Pejw7YMH3z558JcXxIjgokUVh3HupIgm7PeIE4K8GZe7B0bdZl+u44pQm/jBOJq4GtmmblPwN+SXf77E213aS9mPBnzNoUcc6CYfaUBWFpVTxWmPOHf67hvwBbIqZJGqSFPX8RJk/NWWLyMqVgTyd6w8SNigA14LKT4tPKh2EEMmfoburov0ChlxRLBO4jSF3A+pHhaO/l5ZIMqvo7BffvnFderoa/6gYBJ5VJR6Agd8Kox8+QLZP0jjMGq+5sCLCuSHX3/7Afm/yD+bdRc+rrGHleCOFgzjFFnrOwWBOdlmcFiNjAEBCefus19/e7hh1C6HVQrCFwdjSWtG13wXAKMFD998OAbaPKo4VrT7Sr/HDblFEBckbiBaMLvr56/5KKKAQ6tbXIMPEB+TH9B/ePqxzuiT+h1D6Kd7tRzH3mNvdOZYRV+QVYB8IgXNhX5tRo9GRd3AcC1B7oPc6+FMp/nmwrxokBpmTB30z0hbQ1NHyb+4UPQITgZpyWl+QbbiHla4IoW/RoDuy8PZRR6Pjn8P1cdtKKT6AcbY9EPEC6KAse6XTuWUUeXU4D4ucB4RASvbx3wo3EFyWOfHQg5GH91z+R55sz+2D2N5Rxb3VuNR5ZGvLYHhFPL/pRsZlRQkSZtLgjGfIXPF0OxHRI2d02jgo9mCnQEC5z3S41u38EEsH5T7NU9j6IWq/9tjZHAPoseYB421FYwQTdDu8sd0ru5yoSrIavRtVd0x+Jp/cPszBASaXI80BTM2GfO/+FxwfPqhaQTTcrz+Vuff0RmjH8YvUrZuGntIAIB/D/UmqsZEescfxgUYkwpGvhf9zioESoc+h/IRqEQMAxTy/x06BSYE7I0e6H8Oj0e3QC381oPawowBL4g1BjD0Qw0dAFugcQxE4Ye7KCQDEGOo4ifCdeSUD2XGbvZdQWf0RZGN8fCdB94fwmAciwhc7zPToFQHRg/E8gadABOpe3j2U893X0FlszHq75N+7+53W5Hvi9DfxmyDOn6jetiAj/X7O3AgRVdZfWcdWFmTGuZzBt4DCEbCvVS/PKrto5x/6vL6hxb+x3+vy7/XT/P3nntFoqYp69fJ5FHjPkrcC8yCCYyRuAT1vdx9eeTbl49E+/KZaL+T+gDpFfn3NPudiPeQfkXwF+wFGx/JsQfGmH3/QCDEL1P7CzU+/Zpr4JuH38NgZDHIrG7/WUw+hsCKElYgHAc/iks91qQbLIN3TrsXh88oeM8RSJl5OFbCuvgud0ebRp8+XPbJvfBRPrK6P/ZuIRg3Nemofg2eXvM2TZ+fcicD/+NmZiRXGKXjBdwAwYyBjVATg/vVZ1M0Xvx+33bPJUgCfvE6phQsZLCBfUY+e9Fn5GN3cN9t5S3cHv089sHjknAo/PM59nNT6IInuBlr+nJU+7HlGduv97b4j0qMmQQ19sBYqovP1BxX/IMQ+CUMQfVHIbv7Fyd954e6ccbyB6vue1bXUE8ftkrPCHQczDaYQJAXWzjhj8vAdSpwaWHB9Udzv+H3zaziYctvdxiax77x16cPnhi/P6r/I2jghH+xPxsB/airb6NYZ5x876Lu+N67zjdoWzzWz+8ehWMz8PaIwKdXSDHg+WlEsYphKz3cd8hPD12gEd/6VSgBksWXeuwHJjCBoCRYpcvRgAQS3XcLjLdj/z5+/PL6p03uX2f9K0tzgKOA5xOB71EYzZOAZ3gvgN8xnycAxhDwF8EAzHF8ODTwaYLhAUdjDMVwPIAqjD7MnHcVJviIPlT+E+J/s+1+esyGBYKgGTgdMITjeg7jYyxPMS6FUThJ+CxPeoHLY6wT0FCngMUdPAh8isIAztMO6dAYCxw3YJxR3nvr91Dp7aPN/vDHI/XfHg0DXJFwHI/zWJzyedZhPEBiLukBnMB9lgQjQgHHAQrO/5z67pPRZQ+rx1iF/Qjsua7jOr+++3iMP4aCI5dUvRIeH3HCHxyGYF0tctGKAfbpyK/c2Low1tE9+I68Kxhj5otJeMJb0w3FXa8tsUY1I9RSTVeXQoOe5+x0XzfoSSR4PZd1uXM2U4trvcxQ8qE1WbJLLuJK1mwmMfjDxTQUf5GYqeZcnWLIWHveZ326xN1Svums7AdBdshPaTgM2co50nlHFOxQLjSnnmjqIU70g+M4lXnBT0aXb+PJJc4O+gHfEQlvSSU4oIfGpjdY1VlF4cfcYZPaq9Sp2sPBCJ3cwHmQ5x2/Gw6dpRAckA90AGOItSLKvenAO1BHCzc3Ts3f+tJyHS0TdZ6SZwoTVdzF2FDy8WSJLgZO53kD2GjixHp7Eg1uMUcvySVptbpuB73fgb675St3qYYDUa3ksD6rC8miWTl1hLO3cs/OJe3TS55ML3WFW92ywNn9zPegI+rCPqEeTaW3tFgoWCQBnJxnc9bWVwVOe+HOX4lz3K/5g1zCvsnHpXV5BUALk5Rs9cERhWo/rVJOSeTO2KUM2gyn6zop++nE3zLhiXJN+6IGbhAt7D2ueD24aKRyC5ZLLZq5YhMSS8OScK0B1hw3gaWYFKFNGsdcMYvY1xpb7Or9gIvl1Eq2nsbObphKWwO+77r80mMeR0+xsrWPVZVWNEuqWUdUhXxqvL2G2eQ1tisJ5XPJnkSEYsfVVE4P5S6qTR8t+FRybUtekBHALTO2Z0epqoelVs4XOzzILjt/Q3oGdcaIdjqXqY3rqPUa1XbrTpzFfDqTdyYaqv0VJVmnnhOHw7Hojj3IVtba6ryYbMFKXCSrvRNwWZNvs2tmZmezxLXDhXWV8Iqh1ypUj9fwSqz2N2oyDc9Hrpmby5gJhpmIgkHj2f1+O4uZxQYP4O4zlY7DnjqThq5nsl5P+HQVX3HmYGOosWrnYNlptHaWJFFUIhTfnwFtbnoqSB1GzDwsSbVdyNBYXmyWNT0cDEkp3EHEL9m8nZmcJMwULV0mybDbEGLGLv15JJR4PV8cp2FopjJ1OZkW2M1vvrGj2aHyZgUqXqv0lJIxuVicFpgGDv78rF8lt0qGVZJT0XYockJZJMGCp7fWZMbbhEOZ+GW9ZwNsEVRUrWxx+czfLOeIT7rGcy/MsOyvhSvz9MKyTHwpYZPTbkPhxcKtxJ1oUjOPv3F+Y/q51oV7rLwR4mWx1m5BgKk7xyTjzcENZf5qutwOLMtl7Rxjm0In4Joneixzvlym0gy1ygO7Sw+54eyHYTBzZVVfpLWcJfP8spxPuGghc8dtozPzc1Kh6a3nTl2kihyt5p7mobOqP2f0eXncVtJ6LsflkhWPhpGsCBttD/Fslwj7w3kiQEaa13p2PlbEflepvLKN53guC81JXJCgshp3trV2XJf1qz3Mzw09bIZtu7ZX69U0teriwFxwZUEoyUaaGB13EhIOpyaXS925qu9hjHYxDqZMHaVoonC7sBNp7rxt666gzoRNHMiE1fZltWCN9tpO+d1Z99EJFcQRf1iGy3VHY952ve3DiGxcS9b425nqtdnq2u6BuFiE9sHtLfy875rVxrNVYGWm24arVbvn8hnJ5NncSDhrrScEt19OiM1Z3fYLPzKZNN/UE0LEVAdM5VC1d0a6aJOO5bUp2Z0UYk2djtsgYuDeaWkwnAI/FnVpduYxj0UhnumxuC7MUCy17sSszjOTrhlB2OhHUUm4oTCVjXfkrVZiPc/HHLWt7HZ+mzW+vWt2br4/BTsKGxbeUFWTXZPTnXetYhpiGutYtM5haesuun6mMt6sKns5L5j5YoozbAuWeyIVcJxc1kc8LIQzTV23V6yeGAY74dhtOwkCN8R6FPVXy3gRmsqwvkCQCmNeCymxnuswqzjqlFjTFd83p/U6V5fWovDtLJdMEwI8d2F9mfph0Z1PeGTSii4rXU/poV+tdlg2SE3sC8dTPpVrC7vloMA3pV6g5VIJ6xw/XGCVQNltD7erc2p6ZDehM1XSGt8kh9wk60gcKD6h/BWVMKucK4QJG+5n7RrXWLU1ZInsHGNDUoolRdfqchVqcTWfzfR9KZ2ixKdJx7uJ/GU3uGlY4FGsxB7XrpXVeV0J0kRk+LpTOuOYTZXsnAp7M9LdPlVT83pAY55XCHu+6gh9O1/ruY+ltlq7NnrmOr+gMHJBV1v2mly4y5JRgdQX++qwEfYWSdQ6k1D6tKBW22h3cZpT2MR9vh9yq9RYoVBLe3s81lUkXW5HR+O6ueNKt4OKTXa3zcaQ4028KpKNL0T6jhd0YTXMVu4qr6QtTma9F6xUQr0sylI4XXbK4eD4eu3muZwrRKpO2/CSV/Wh27dKW5xlN+znfk2J+klM6G3TYprNzasbd6Mua6VrzvXAa7GUcQTnmJFX54u0qaQjZbr7tQmdQ1XTSUG0h+QQy0dwxtRIXBBOsz7q1uEI7Olp76qleQCYvh/a81oXRSwuCl7j0aN41CWj00OOWdWYYdu6b2usvV6EQ1ta8rxIWoEzDUNbpdep6pw97AZbDP5C8ys0i2bq7Lpu0KVKEcJy4vjF7pyoBNDDRU3tN0SiDVjEO4lctXXEsizNJxXO3VxqftZu872X6KzVHOvVOaWOOxTDLtc50FmUMUGKwv22K2Mnq+TlE38RjROIkrmuhId44lQlp1Hz1UKctrB3tjs8WduSZwfywlynl6UUOfuCaY+LnWvWNs6IZZ7cuAgjaKeM3M4+yrRo1XM7Fc+X1hBMzyX4ebLY+IxgkSXv+BWmSdXxkJocaQ66H4qDYN/yYHbEakHiiDnWLY2NDv1GzbCLJlF1utXodRxcjAIXaqYw+lg9L41JeNRWZZAkZCzkrkUbKkYxItsKEzmLeSmwtpLNXNzzuUm9qeMxRYPfDJ6J6+IY7tY1DZkvVHRJjvVIXqzDdqof5tG8y/HwqFJ1U5xiD1OGQFQ2ld3LKn8dwvOs4qRbSRp2Zkjprveqxfy8yGt2d9h0C9QvV1i+8Tmuc6JZwOjxld2X2JoJr5F06/olqw/U9jp01dJMy8zqjhpauzM8XPucQ7TLqt0F2kLWOHVwrDbFKFQ7d7shMZKjcT0vmxU38TR1IrRMv4qVdNVtbDPEd1IQ9dPwpneg8M1dKhjnkxQTU2M7jxSldQWiXvlCcmAwvLK8E4vZijTD4sW6SZ3M32nzE3FhJtEOVEOS13wRGZrmqafdwd/ozWbe6p0jrFHxrO23iUBl4ryZ9sp0EjaHbNldenG3ic1bUWOxfOrzw1U5AnkpWE4qp9ZUh+XzNhHXuKe40mwRoq6kl16m1lnmbafmsGoNes1YRDA/cwMYJpliCwZscAn3ODuSS6XLSo/XF3h3A72pqaXqHbZ0vEl0Znr2z9sdKZHrSbg9MZqB48xedRTBxoMl0HEDdRak1WzgpCzaeuR+04h+dmzN8rKorsxaIaJEcTcbWboZ+4TYl4XOzraDmcH9xHSBY9ZlHaLpjEnoIdJtXdmfS/q4Kdzk2KrbkJ0JLjazsTkYElGPvMW1uMmLmZJQ5iR1MCLZcxR58JYHSUCFhbO4LBzscPOvRnVVLa9KRGEpS6Xg5+BWNHIjRE1ch95K6zOiCfuCj4XzkZfWfnUwh+kM0JMzS/btXiS8Rj5aC18IRfm2svhdbhhHbDH4DT9gRbyRaN4onep8TdtD63SToFAihq8ObMBfLvR1mFb0nGVv1E6uUCYll4eJN0s9wr0SUjzUZ4E8Sqebqc8Nv2VPRXeB/eWVCLYXSikLb6AkI4GMd4W55t6mrEtf8lN27lpqamjJplhoADUv4gQluRkFW05VweYVl1csSsyCA8nLs/AWNhNIpVuGp8FUNdM6msUGj9lld9rs2NVwInzCKVvNr+RZh52yID1qrao4p71Rr0GsXG3mFlS9F3a8z6MT1ZwUC/qkHkHE19ykM7m8OJHHZYCihCPJWEnO12nJCnQ3KwZ1TS4GbGtLNLMx97AG9Dk/1dZbSajZSWaZRChsfKXaCyrWeyow5XZmb4xk352MOc30qLGp0pvXwq7ZogG91DBleXVUJ1YosQgcb8iVHVecYLu4YIWwrG8Veg7XnEOee14V4b4KoFvsPJmrA3lUD2hiwm5dw0Sy71mmrxI2qcApS7apJZYlevbOeB642TTShUDu/Kmn7EgsnZkobDY9Vp8M1rW7Tqzdfh5sRPkCE1fo5olBbnn5Gp6kkN2x/Hldb9prA3bSqrFDWTr03iDhHCv32O5M5DmYmiy4LLfejlUmy+oK+8QwKwRh0jD18XZa892GPgrWjtytF928wjtf3FgF69UBmrC6EFLbOlglpBe1vZnRwNhcgIIlArNV+i6mEnnKLTpBIq/qzpju7JQGltlyrBEvb8ssseFuJOVUSJdnY4le9vsJC/cowpZVwUVg59hUDtzl6drfVqvzLVenfBhv+MaeizePkVcgsq/GdV3qVzfZElR7CqaEtyZNwm5QiWgASbFl0RAWGbPrDjPrYTdbu7KbCgSLz3fZHD2t5IHZbzc8mYYgatvCpfcuWZVdyoYqlXRg1jsUShLbXO23ytEI0W7n3rz1wVMY1DF8UrKvko0SvHBS5WldZ66/9+TdGcOOxAHmJebDSrfpCptpulAyYoYND8yWDJNhhgnTU4DRqsJM+B5I04UAaR4tJRV1bN3LVwOA+5llmZeS3HNezNosKa7AZGP1PLqf1leKRTFrqPatzig0PqngHo/Tl8GRofxNRKsSHw7r+ujxMLnxjdweQBTlB7khJ1ljX3iKLAurbFGS2k+4tj5QhxlQSNG1zCYoLYHTGkorY8HhFlqJ+Yze6ry1XBEXldMKZn3h6fgaolTFO1boiKK9uDitvCRpypzOtDLI3XO2PeZWcDq3KL6laoJ1d/RiY2RD0aidPt8zy2nR3wLVlnVzBfn2fI6GCFPcbQs3+zo4XhuaqGlA7CZwIyDepGhrDm3E9ynjW7YAlgbFbByiEltU9U83RpgettFygRdiPXSDHV+umwBEjbpltp2WWUZoE0c3m+hFKYM+vSh5awfnaiUvWQPPxcng9xgq9JM1EIOTaxR1pDQpttS5vW3R9PVmKZMV05ArYz2fDkNGD7BpTW3/0m6utBoe9pM4MweXJovutu7a3VHwijXmyYuGVe1MK+e1CjsTBg0nnGYDE2gqXdLp1cSGtqUxWjxivUK3HlGpjBRgy3owMn8QSkEQ/v70/HR/Rfv0imM0RT0/jef976f2//qxbzjE5du7HJIliOen/72Tyccp4ce7vPsRPnD81/vqr/+qiv94fqq8GKrzOCau0zZ8P4r8b+euX/75SfA4t3+8Wx5fN3bNx4uOxgnvx9Rx7rd1U/VvdZG290NqCHBbj/+vpH57f1HwdDcoK5v7s08Dvp2UNsVb6Yy4xvn4Bg348ePxeBm+H+c/P/k99FPs1W8kQ7+BqhyNfH+fNJ7Pji+Unn77f6vljeonJwAA -->
