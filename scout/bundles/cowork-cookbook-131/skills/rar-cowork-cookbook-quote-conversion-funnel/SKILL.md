---
name: "rar-cowork-cookbook-quote-conversion-funnel"
description: "Analyzes won/lost/expired sales quotes by salesperson, product family, and reason; produces a funnel chart HTML and a workbook."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/quote_conversion_funnel", "rar_sha256": "57055993cc580afb91039f007a2de7d3f6f5c191f4567bea3a7dc83603c1d2aa", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/quote_conversion_funnel`. The original RAPP
agent is preserved byte-for-byte in `quote_conversion_funnel_agent.py` and in the RCI capsule.

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

Quote Conversion Funnel Analysis (HTML) — Analyzes won/lost/expired sales quotes by salesperson, product family, and reason; produces a funnel chart HTML and a workbook.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/quote-conversion-funnel
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `quote_conversion_funnel_agent.py` and embedded as the fenced Python below (sha256 57055993cc580afb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `quote_conversion_funnel_agent.py` first:

```bash
python3 quote_conversion_funnel_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 quote_conversion_funnel_agent.py   # or on stdin
python3 quote_conversion_funnel_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Quote Conversion Funnel Analysis (HTML) — Analyzes won/lost/expired sales quotes by salesperson, product family, and reason; produces a funnel chart HTML and a workbook.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/quote-conversion-funnel
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/quote_conversion_funnel',
    "version": '2.0.1',
    "display_name": 'Quote Conversion Funnel Analysis (HTML)',
    "description": 'Analyzes won/lost/expired sales quotes by salesperson, product family, and reason; produces a funnel chart HTML and a workbook.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'quote-conversion-funnel',
        "upstream_url": 'https://coworkcookbook.com/recipes/quote-conversion-funnel',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c914c9e9393487ff',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/analyze-sales'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/quote-conversion-funnel', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class QuoteConversionFunnel(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'QuoteConversionFunnel'
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
    print(QuoteConversionFunnel().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6ebPaSJbvV9Hc+cOukX3RgjZ3dMSTQAiQEAIJBJQrbO37vqteffeXAu511VRX93TERDx5ASkzz35+52SKX1+Mpvaz8uXLi+oYKSQYcRz4TgkZqQ0tsi4rI/CRRSb4B1lZWpeB2dRZWb18erGdyiqDvA6yFCxnUyMeRqeCuiydxVlVz5w+D0rHhiojBo+LJqvBhzk87nOnrLL0E5SXmd1YNeQaSRAPn+58S8cAY397joFFBuQ2aerEkOUbZQ2ttZ10n2hAk4CTbK9AHqc3khyQfvny8y+fXgLw/eXLry9WbFTg0cth4r/I0hYwBhKv7gTBqthIPTCcD8AMKbgHgrlZmYBHtuNCz7uPlRO7n6D/+q+oM0qv+unL1xR6Xl9fpj/HJoVq34HqzKhqoLNl5IYZxEE9vEJs3BlDBbSqmzKdlKmAFVPv9bHyB6Ush/4+jX18MHn1nPrj15cMiGBMNv768hOUlYBf2UzfXycq+cefXuOsc8qPP/2gUzVm6ACTAmJA6tdvz/snWTDxx9TAvXP9O6D68KbpfH35nXLT9ZB70hOsfHkNsyD9+CAM/NM6qZFazsef/oqs5TtWFAdV/T+i+/ODsO8YNtDpKfhPn+5G/gWCnwq90/xrtjlw67+jCZj+xu4T9DTUX9G+2/+/kY6DFMTpm8X/Ibl/tAD+O/TzX+r2zxZ8gtyvL0snDkA4G2bsfIF+/aYq/OLnD/aPhx9++Q2Q/pdk1KwprTuFb4mRBq5T1d++/fyhuj/+8MvPH5ocxJpjJN+aMv5HNP+RXe98/mDB56yPf1wL+J/SKM26FHqPdOjXLP+P8rdX6GzEgf3jefUF+n2+TBcMTUq8MX2Y4Hc5UwFZf2fHn15+A8CQAm0A5EzDIMv/8z+hXWCVWZW5NaRaWVNDwMF1kDiT8JofVBD4O+V26dyxAxj2OQ/E/+ThSeLMhb7/H+uOl5+tJ17O7pD3zXrHnG8PFPv+CmmAXFYGXgBAEzqyivI1NTwnrSdWeelUTtkCEDGH2vkM4Ofz9AUKUuj7X1D8dl/8mg/f77AYPLDouNhMOFQ1sfM66aL7TvqU3AJQ7/SO1QC6cWYBIdwAIOcnoGOVxS3AsUnvKgriGLIBiFsA8ocHNjfpl4nY9+/fTaPyv6YP4MShRy2oZmDCuzjQ589AGzcOPL/+mjqWn0Effv3tA/R/oX+26k584qEA5H5aHki4VfcyBDKpScA04BTgRgATd8v/+tvTpuVkjhIC1gncwHksBpEYOfabgdU1+xkjSMh0gGGBUZM8K2uAxlBQv0IbF3qXFzCdhia89kE1g2wnd1LbSa0BUDWAOu+WTLMa1LQ6qFxQv5rKuXP9bpbGXcQEpLRRf4d2CwVUhywG/01i3ieBxVkaAPO/u//xHBApP1QQ90biFZKn2INyozRyvzSePFzj4RdQFd6WA+IGlDrd13Sqf85kqnsiPMwDJgHLWE+Xfp58Dop6ArLert543+cYUw3T7rWs/JpWzyA3yskVFgB9wNRrAnuC/r89Q6rysya27/YDkk6Unl6wn165x+C9CkM/yjD0qMPQvXuoQMx9nIr7T9DXBkPQOfT/uamYJGYF4cgLrMYvIV7WjteHJadWaLL4o3sCZR4C4fTImh+l/w043vDzaxoHICzK4W+PmXf7P+c8MKmZVDuyxzt94HxgyYnuPTanWCvLKaqNr+kbUAPdoDdTgkQGgT7F1xvDafRNUh9k63T/o2jffVnak9Ig/qC8MWMQG67j2KZhRUCqcsqvpydAoDpTrnV+YPl/0AoC1EE8APoQECIAGQPA/G46OQNqgtRyyyz5MT2YWqGnF2wI9JrOK6SDFJnCBLjSAf3MNAdY4cOdFJQ4wMZAxHcLV76RP4SZ2tOngMbkiywBkft7DzwHfwT1XZZJfEDVsI0a2LKbsNV2+odn3+V8+goIm0xpeF/0R3c/dYV+X1H+9jW9y/gO5yC746kY/844EMiqpLoH2wROFQCYxHkGEIiEe919fZTOR21+l+XLn3ryj/9e234vhqc/eu4L5Nd1Xn2ZzR4F7K1+vQJomIEYCXKnetSyzz8qz+dH8vyB3MM6X6B/T6Q/kHhS/wKhr8grMg1JgeVMwfq8gAUWn7nr5/k0+jU9Oj9c+/T/hKfxcMeEZ3F5mwIqjFc63jT5UWyqqUZ1oCze0RUY/2v67v5ncgBwSL2pMlbZ75L2XmWBMx++ei8CYCitAW976sA8Z9qUxJP4lfPyJW3i+NNLaiTOP9mMTAAPAhM8nbYuIEkAotWBc797b2qmmz/uve7pA/Lezr5MWQQAEDSgn6D3XvIT9Nbd3/dJaQO2Nz9PfezEEkwFH+9z3zd2pvMCtlH1kE8CP7YsU/v0bGv/LMSUPEBiAK3VJMtbNk4c/0QEfPE8p/wzkf39ixE/IaGqjakEB/VbIldAThs0NJ8g4DKQYCBnABQ2YMGf2QA+pVM0U7mY1P1hvx9qZQ9dfruboX7s+359eYOGpw+ePR6YDnLwczVVuxkIT8AQ3D8CCYz9T7u/5zKAYaANAesICiEIhsEti6ARwzUZFMEZF0EoA7MdysZd0iUslEHdOUFSpmPgBmVbNE4iuIXamGEAeo8o/DZV8mASxUFcB2dQzLJxEiOIOYNSmMHYxpwyDBuhaQqhXBvA/I+lEQDAp34PfSbjvTeikx2eav76YpJzMHM9rzbs41rMmLNBzimz9y9wSTrXKoSRBAlOEpIaw1o/jpeyFjaebcMItlheF/vhuEaSQ76skJtTINWq8pcEm45bBd9f+EBEClJb8adjR7HxmEcjgZPwDj2cjoY8k3fZxi5K0SYl/ZRfKuO817OETbcqjOlJjjGybq5Q2q1QBobriIHRVWYXF1E3BCS5pnhs9KsxPLS04tW0valws2xXWlBYlVjozVm+1YFqYmqfapxDFJ2+FhplxmWYZd4QDrPLi18LPpovwkopBlTNB9xD9mmKUcpYYVZiVoNbUXvdpGEmYJJrrYs3cYOUS0dQ9CK/JQNhFLfkKs812aHPB51hR3e5CUzVr6zWj867AiXaCx4tts7Ab3ie4xb4xsT3Gj2vnYGQTmeQB5VWNYd12OTXiEnCpUpFJyxi21XSX4t9pzZztAhJ5bzZOwY5nhkfptrjLpW0HWslRj6e0oAnENQYNl3tW76Wxuhimy435cEWz4ciiZu+kEwFDcP5Lt1XNa1fDweupG30srgt6DOzqC/mKim1k7XT9NY3b/BYG/5qlAgQmUqRZ4fl0RCagDWLcEDC2hc6UyOKpdFe2rWodstal3kKO/fN3tjnt/R809nKXNJMtz2cxeXagom5sSt1Cd/1lzYdzleY6rtNc13n6bnGcKdCe4FKpdy3lT6/YW4glsLAXPoD7es7KhjZkMwwLDpfNnQsjrWdbdbDrGuFstB2XBFKGLZGa46IvGMBZ/kmF4LoiDGrso9GfMH7ClL1A7/dm4MuWr1KYko32ztNCd8q8zTEBCXfbqGduDFsFRay41W+zHQLy8nbLSEYLR5ujFnNO2tmmtw+H2lpTKk1QUsUuY4NJt4GXjM7Mpk7lgxdtvkW9az02u4zm4qjYGDqa+Ki5mZw/NuGLwkD1berfpOiwZwsJWtzGcbgFC6JInVIjWV178JGjKfZZHNKi4iF7QBeGlWsCoY6nLnITfmm160VxifhTYzyxVm1Nk4FV0fxuM7NDdoFzbUq0visGch8h3mWZvfkoFmLAt616bJJuuNszyFp6tEacd2POGw4CHNYV/ZI0yOpN4uSkNmacXW9NClrc0MoBVZ6191sT5LsS1k9P5uYMJuriYL3Rz/H6WWPIWqZBXzc9ztM8xtZLWqUrXkvEW8pLAX5co2LJ83Xeqe1lLmhJqdkpxZjw6wWeizTQUyNVBttLKc1iVVJHpLT3HHbW75p8qJVOPVmcG5xySWnvWD1SpyZWnCu6OPmetHXHHxWg3CoUHhbs+gsO261VpXqFUnLYiYNZ+GSrZQrDGfywszPozTuz0uCT2fjikQplUtmM4PZVFF8qta0MALwEYNSqKSaCQVXvjKVFqyWirSTnYWwstPcxNVTo+X+PjpQt+3ZH3UtcAx1L6WbPF426I6SFGHrD7yNppFXcLIR9rPTaAdIgRBwpKlIGhxUR2aanLU8xiMOcnrijmvnpClUMt8yfIwgIpPj6sAzzd5dHnHMU7hZhBWVVlcUFhyyopHz2ybXDBautwupZxrYzgoQOAA9rYKvxQXF0jUjYiyr9ta6FNt22M+PC7PZpqJ5VWlHmSd17qXMCjcT0ikk6Tb2nHGITuKBnV9OAqwtQ9JjsptAWcnKaqKqUDZmsDuoltnWLUbs7MwLDqy8CG+XU1zZG/ZKxoXKLFfYrSD2HtvIBxEdV+vwWpV5tqhpuaEIkz0lmp4z+VnIziWxH08E7i5jaUFc9qrs3lCaUUaUhJVgr3v8TVThgJxdUCu4uj6F6rmcVtayOqiihkiMwiviDg8TgghtpOFGo1QoHFZddQ67s5DokBkM526MeI6I9yoa25fGFZhKFVm1u5KnKl8mgAGSrcE2Hmlu8vVyCxuX6k3FI7e0P+e2m+MBb/BMUfLWglONmKucavY5N/KM6PXUbTFEsbT2ymbFnnHVu1xW+rygTkkdy6vQ8HQ/5mE5KXO1bcLjybLm2tIMy8Dem5YzJuhQbUXB0fuUvFj7NsHQmCeVUtIx/VwP1cyWvHpVj2uzQkuRbW9n4VDIbrhkiUNCrWtO6HbH877s7JQaZWHmtNKJPHqVfeEZwjf5fRbJGrrsLeqggTDeB5cGv+p0QrFzPaqOlI4Pm77bWq4wk0xW3sncaEU8YQ9UtV1eq8O+W+zZS+mQvLIM9gJ74zmaEpOqvsXJYuGtW5vGsppQV7fAizNVjzXjWrDLQa1yRHKMxnHW7eqsrw9tKPj0NRTNklNXNOfwR0y4BAcFoJhJ5xXlRn7KXUhVPUns7nLJqyS+lnv2pJuVfb0aPILT4v68bskGFTNtfRxD1qJEOUm5Uu6KxPPbhaYm7U4zDnMK38t8HkUrRvGwZHMxTQw3ge/pMysN6rEozr7F82XR74/VLpWN5WGBUKltDE3cMyzD7tZRHm9Y8zxTs14md/5mU9FFt0I43LdYFl6p/iWnzvL1yg90RGR11ZnzWpbya6Xqh5y9DUq9CHSLYw1GPNRjZdmSi/hR7mWeJOXtDF/VRTajMgNGLG8VokK2W3OEPND7PuLSU42ezqf1UgYbEIxk9ngb3PCjsVmvdyTGIddzi558eHkVzte0vUQIrkvlirAKHCHbW21IwW2fM6VpC6h342KTX7DL04CR8xt6jDcH8bo0bsV+xhSbY6eQHawX3WgichicXIlE7Shfqn548fayb2QnLonFc9eqFwWhDl25EKLbKRepHXccWykkD6cSz8xTbqB4ly/ywgtPFYoNg8sGEntlQ1e+0KlnNBs+Itba3tpt5koM9OZzVV5Fmz184tFGuHUeN17PUb5OVuRxKTVISh9Ba3wRTSIhVd30ZGJHx/kFvh43gXWUxgBLtpfrfr/YVtGZPVDhcneW5gKeCAhXicNpExPiYeJAbxIyHvyMDJR4ELK0lwzQsIq7XAvEjtUGee9tOpJm84UTUbJqIE27Fb1TdD1YUwzUZOroEXEtmW2wTefGopWlvo3qRGyb80LY8c1hpjZuKQ2M0XNWn3D9jiJJHaZdwTDRzkVOOMni2aHQnbJ05P0Kqfxj028vQRXA9HUfSmPHjEmGUyef2Z8C/mqrS35+zROaX/oSPxxRbYZwYw1w8FRXODk3DNGfU8LoxchmTGeGIBKL09jU5xGWLwiw8o6/6qLkKxs/dlB5e1gMK+notzu+1rLyJLIckwRU53kbjkzFW9RIHMMXN/5GHJANM5JJL5k25jHOTLsel7tjHo71XApXIhpdeWJ5tW+20FbSja+u9nybXIlUN+V8kW1Ipukus9WmE5sMFux6V68tHd+frYHn3X26KKKDd1ikaHEOElSwEdYMhauV4O2hZa8j7YdKmjisiLCJOsOr0IjIerBlg9e5pbJIsdpJtgFTt1ZAnUwXt46UJu6M/Wmn201iEZ21xOtZttLzFYqpCzOobL5cLrdrJL516mkuiJLMM6WtpuJpI1YdyXmWwBbDbreyRLhD7UQ8LFdLOSBOjS1G1GWOVQejkRKPuxxhLZ8tNe6irREJG1njFp05W9VhQSrVylEyRNU4MqD3XJPwfsjhqKoj5WKHlWwZt8ZAtA1V3Wz82KOKfcD7AMReYl6Kwa5jXGESMheE7Xwdgq7URq01hi9ayr2ZVBt4571yNI/43Cmsmd81bdzIkY3Hncvos7PUXi/nbmfDhHU5IBhTGwKMjTGPeHB7UVxEJDSP1Kg9drGFE46JDnclNrceHfDL5RA5TZ9kyq2gTbaKNgF3sebldXFd3WZypRNeJN3sSCiCwBx1uiREwW3wW6ti/QVRXL4xFZbClcJo507OzEy2m1v2WmH7lhxEyrroBbbyaaqizDFnyw0H26u+5RRLam+YNzvPCWmNS+Ns5ks0e+outqEUrTsPZu1Zwy6ts4HbjWgR6ybXDhx6ak9y1sFHQkh7XV0cTHIA+6+IC1JqocmLlYce4GXtyKvDfi4dwn7sBPi4AjsLmcpgb75NGf1IWxQGayp1G9vmGKxqI5bqMTMUechPestZY3ginVNMdXFKDsiWiG+bRLgg8qiBPXZNS52xci68Vq0pmMFAAoYbMcGG86XuPHqPYQlFsLOqDOWoDouD2bibgZhtlyh+EJrlPs52R9gIaM9RMKMOZ9f6CLtS5a9n+oyey/rWQRx84MEu6pwcFBWfa+sDUxOwT90KyaidBmVpIxgTpr5p+5ExLzidSG6xmTfNbjkKs8vJuqkUXPqaUl17/nCZF3bFhL1ZXXGjD7mA8iNTB01RgUjyNRSo2ywod77Add7OHKLR6pvBRAgFdL2W3c83c8Mk1svoQK8CDD1idciklXToJYK2cmOu3XCmSxPvqmLheX5oFLFd46OLUyE653dODyMcA/YJOqqY6cWuHH2tsoKNXnl1oGRrHXiHQboa/hV2q+3KLE1+Y8/hrM22omJybWVgHVYqNmNXrE6N5WBXKCnurTyrHG99c6vFjZ2NKJcujN5ew4qlBjO0Wzu4QYCtJE55ykUMg7WEmPzaq3zzEnqmICzbEe0Eo7OOiW0Xsw3l4HyrnK92v2PnhsTVhdwshTnOLMzwcuMpBFdxW6r1WtAze7DjgVmvtGKBB527AFsR0Bv2sHxatuHYyPxBOIUzXlHz21q6KeGc4dd8cnHPu1m+vmrrESZ5gz4sD2VNeQdtxVBm3SaDWzMtKeFpg3O2U1Ay50phCqPNOopcZFPp8EFaXc4U2FaWPL7V1MhsPHik5rZl2noId/MKbnFSmtGX04EmFEvGBRNHEtoTePhoo0eNZ9F5UWoZVeK0NGz2x/oM93roJ2UzL2CO6mbzbscibDSXTgytK0qdl8E2VDoPX2dGK0WwKJrUCQ+oa1hReJJRfFOtlmfFo7KrHqy5kfPsLetJ9eF8da6On948sdVMdkEsWxhNpR7H97s+LI4eG2fLrA0YJg0LodVy2t1yNtbv4H5Pd1bE3SoOX3RzHeuOHRyKS7EkNNPLMy5dppuo6+lCQNZRT0X2oi72Riitj34qaHhuBiTV1fBsjI69bo9bUHFpQyMrTSVAILfMrnTm2FzUXZrR04bLdG6UBkIs1L7pqVV+dsmMKxRqtSBifJyd6dNaISmLC73NfK6nGub5bKjalnuWw5wY2241RPkwaL1W7mbe6JHuQh7XGwsx62hmezGqKJlCZ83hoLAZy7J/f/n0Mh0uP4+I/9Wr3unw7n/tDPFx3Pf2Yuh+OOwY9pc7ry//UpJfPr2UVgDkeJyKVnHjPQ8T/9uZ6Oe/eIswLRoe70qnt1V9/XZcXhve9HOelyC1m6ouh29VFjf3w9hPL2ZTTb8xqL49D51f7iok+f0E2wDZnBml/XhY5Y5Vf6uzb3f+L9NvAKZXMI4dGO+33vNwGCwegAsCq/qGk8Q3p8wn/Z7yArWwV+QVffnt/wFzYzSeOSUAAA== -->
