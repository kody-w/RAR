---
name: "rar-cowork-cookbook-adaptive-card-develop-product-roadmap"
description: "Produces a reusable Adaptive Card JSON snapshot of develop product roadmap status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_product_roadmap", "rar_sha256": "019abdecc652cd999c806d5b9ea8107e4c5ae4d1d4cf2bf51ae2081e803503d5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_develop_product_roadmap`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_develop_product_roadmap_agent.py` and in the RCI capsule.

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

Develop product roadmap Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop product roadmap status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-product-roadmap
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_product_roadmap_agent.py` and embedded as the fenced Python below (sha256 019abdecc652cd99…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_product_roadmap_agent.py` first:

```bash
python3 adaptive_card_develop_product_roadmap_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_product_roadmap_agent.py   # or on stdin
python3 adaptive_card_develop_product_roadmap_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop product roadmap Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop product roadmap status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-product-roadmap
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_product_roadmap',
    "version": '2.0.1',
    "display_name": 'Develop product roadmap Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of develop product roadmap status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-develop-product-roadmap',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-product-roadmap',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8ef07f7a09dac069',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/develop-product-roadmap'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/adaptive-card-develop-product-roadmap', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardDevelopProductRoadmap(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopProductRoadmap'
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
    print(AdaptiveCardDevelopProductRoadmap().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZPiyLLlX2HyfajqR1WiFYm6ds0GoQUhQKAFCXW1VWvfF7RLPf3fJwRkVtfr229uj43ZUEsiKcLD/bj7cY9Q/vZiNnWQly9fXmTXzGacmSRh4JYzM3Nmm7zLyxj8yGML/JvZeVaXodXUeVm9fHpx3Mouw6IO8wxMP5W509huNTNnpdtUppW4s7VjgsetO9uYpTPbyeJxVmVmUQV5Pcu9meO2bpIXs+I+tZ6VuemkZjGrarNuqpmXlzM3tVzHCTN/FmYzx6wCKweiqk/ggRkm4CcYo7hmWr0ChdzeTIvErV6+/PzLp5cQfH/58tuLnZgVuPXypsykC/1Y+aFzLT3WBRISM/PB0GIAmGTgunBLoEUKbjmuN3tefazcxPs0+8//jDuz9KufvnzNZs/P15fpj9RkszpwZ3VuVrXrzGyzMK0wCevhdbZOOnOoAER1U2YTWBWANPNfHzO/SwKw/HN69vGxyKvv1h+/vuRABXMC/OvLT5PpX1/KZvr+OkkpPv70muSdW3786bucqrEiF2ALhAGtX789r59iwcDvQ0Pvvuo/gdSHay3368sfjJs+D70nO8HMl9coD7OPD8HAia2bmZntfvzpr8TagWvHSVjV/5bcnx+CA9d0gE1PxX/6dAf5l9n8adC7zL9etgBu/TuWgOFvy32aPYH6K9l3/P+L6CTMQB68If4vxf2rCfN/zn7+S9v+uwmfZt7XF9pNQHCXU959mf32TT4xm58/ON9vfvjldyD6/yhGzpvSvkv4lppZ6LlV/e3bzx+q++0Pv/z8oSlArIGM+9aUyb+S+a9wva/zA4LPUR9/nAvWV7M4y7ts9h7ps9/y4n+Uv7/OLmYSOt/vV19mf8yX6TOfTUa8LfqA4A85UwFd/4DjTy+/A5LIgDWAAqbHIMv/4z9mh9Au8yr36pls5w0gpSarw9SdlFeCsJqBv1Nul4BByiqcWO4xDsT/5OFJY0Btv/5P+06en+0neS7MJ/18swH/fHtS37cn9X17Ut+vrzMFCM/L0A8zM5lJ69Ppa2b6blZPCxelW7llCyjFGmr3MyCjz9OXiRt//bfkf7uLei2GX+8EHz54StrwE0dVTeK+TnZqgZs9rbJBTXB7127AKkluA5W8EDDsJ2B/lSeA2esJkyoOk2TmhCUAIC+Hu2yA25dJ2K+//moB3v6aPUgVnT2KRrUAA97VmX3+DGzzktAP6q+Zawf57MNvv3+Y/a/ZfzfrLnxa4wQY/ukVoOG9zoAsa1IwDDgMuBhQyN0rv/3+RBiIyUCVAz4MvdB9TAZRGrvOG9zydv0ZwZczywUwA4jTIi/reyGqX2e8N3vXFyw6PZq4PMirGlS1ws0cN7MHINUE5rwjmYGyV4FQrLzh06yp3Puqv1qleVcxBelu1r/ODpsTqBx5Av6b1LwPApPzLATwvwfD4z4QUn6oZtSbiNfZcYrLWWGWZhGU5nMNz3z4BVSMt+lAuDnL3O5rNtVJd4LqniQPeMAggIz9dOnnyeeg+qeAEZzqbe37GHOqb8q9zpVfs+qZAGY5ucIGBQEs6jehM5WFfzxDClT/JnHu+AFNJ0lPLzhPr9xjkP6L3kB+9AY/dhZfGwSCsdn/7xZk0nvNcRLDrRWGnjFHRbo+8Jw6pwn3R7MFGoG75HvufG8O3qjljWG/ZkkIgqMc/vEYeffCc8yDtZoSgCatpbt8EAIAz0nuPUKniCvLKbbNr9kblX8C0Nx5CzgJpDMI9ynK3hacnr5pGgBDp+vvZf3uUYAhiAEQhbOisRIQIZ7rOpZpx0CrcsqypytAuLoTvl0Q2sEPVs2AdBAVQP4MKBGCvAF0f4fumAMzAcxemaffh4dTs/RwD9AWtKbu60wDiTIFSwWyE3Q80xiAwoe7qFnqAoyBiu8IV4FZPJSZutmngubkizwF8ftHDzwffg/tuy6T+kAqYNgaYNlNfOu4/cOz73o+fQWUTadkvE/60d1PW2d/rDn/+JrddXyneJDjyT1wv4MzA7mVVndSnSiqAjSTus8AApFwr8yvj+L6qN7vunz5Uwv/8e91+fdyqf7ouS+zoK6L6sti8ShxbxXuFRDEAsRIWLjVe7X7PFWjz88s+/zMss/PLPtB+AOrL7O/p+APIp6R/WUGv0Kv0PRoH9ruFLrPD8Bj85m6fsamp18zyf3u6Gc0TBybDKC8vhectyGg6vil60+DHwWomupWB0rlnXGBK75m78HwTBVA6Jk/Vcsq/0MK3ysvcO3Dc++FATzKarC2M3VsvjttaJJJ/cp9+ZI1SfLpJTNT99/cyEwFAIQsAGTaAgHcQRNUh+796r0hmi5+3MTdEwswgpN/mfLr02xqXj/N3vvQT7O3ncF9v5U1YGv089QDT0uCoeDH+9j3HaLlvoDtWD0Uk/KP7c7Uej1b4j8rMaUV0BgQeTXp8pan04p/EgK++L5b/lmIeP9iJk+yAHw+leiwfkvxCujpgIYH0Hg7pR7IJkCSDZjw52XAOqV7a0AtdCZzv+P33az8Ycvvdxjqx57xt5c30nj64NkfguEgOz9XUzVcgFAFC4LrR1CBZ/93neNTCOA60LQAKRC8Mi3Hte0ljtjOarWySWjp4NbKNUkYIlzMxk0Xc2AHsz3E8nDYdBGIhF0SQnEIdXAg7xGf36a6H06KuZDnoisYiEOXCI5jK5hAzJVjYoRpOhBJEhDhOaAcfJ8aA6J8WvuwboLyvYmdUHka/duLtcTAyC1W8evHZ7NYXUxC562611fj0lkfxxW/cxVZdpo4N2uRZRMEvcZOND8jMcxg3Lxr5M3O3NfXfclJWo7HpLTDOmW1G9dulwlOIhYrcSdhaU7pVG8rC/EkeXt+HXAKKcMDq1BhIiQXbXe96eESP2vE4diraYHELU0PWkkp+s2qYHy1uJqLShIYw1hq+ZEnx4MRwRFWt/ooOCS0axOOvfXOjljVVBPh6i11Io6P4aRNr4MxZHoKB1Syw0P/UB3acQtKLmVtrzi3I+duZpArEU1Wq1x2Wr1fLTKU11OSkWGpkTjsWpI9lzj7qmSHMTZAEy5u+lH0jUUkXHVKNxNqjQ6pZJPZHkUY2JalEdjHMEv2duFTPdvNHe20c3FBgK+mukdQhuo0NR96LdrbRCwjcR8kaS2Zt2RIblm8uTVHwCYRdClP9BnfeeQhh4d95so7f4QUyov6k4QGbm8kB4S58UfR2rG6vKFEd6OL2obY3sbYTlOnx7jB1USDPuT8Gp6j7rlD1IYlSQ67wbsaIWPMlFNbXdKZVJxD47iqRapXcaNkyWN8HO1t38PXM9KV12MAwUGtWnoUHC/bJLm4x9gj9ETK5FoJj+XaPQWue1N5AQqim2eTR+ZY7pYZdkNHQxA9p1uqEkXHYwivVotcuZaXkSWHZovNKyvrj5fScseRtwoTZlNqm1wKMahUZ144CWddtRML7L1oanildW7fjFupYFgR1pGb4Ai6rWMRBDXUYWEckC64KmRpKyG7ZQmB467FSmLjRXlqb51ucewp7/XBRXhtp/d2akb1VjoEGwABulEMuhfUMYPI57+Vg9j4YbMwgmWmJvNN4FbMgpbmTBRtu4iBWGnZLij25o4lMfcW55TO0ZPU1PbW38gEAYfkdcwLQ9tC7Q6TSU9bslxjbtm4XVr0lTf8PmLQHWUegMm9sKMat+wu/lmoAZnu+kE4iSDAoMw/dkfeGPwlrHBCb3c4Q9kcpkq6JkoBQxilHYmx7McdshHgsMtFiT1Yp9u43YZXseRsArtwFLzAjW68Eajibs5hBCkuj29RWTyvDq0htxt4B3Fuh988mISVG9+IxO1IJGdyg8UyZ3sWSi5Gm4SRG77eyMdT2DHLhcaV40XTMYyiKW1zlZwiuVygoeXUyD0Ka6yBd/kpqnY3F3NF5HCSC7yvl2uq3TkSZrCGvhnY/fmAx8qGD1TeJ8p2ZfMKsaKb/KgYghCdUGKOQ6Ha61HBqlXnLVFhKyF1tTSkBYOyG+8Q8pi6OtU7TJtfMDUm896oBLEJePzoQF2qRwPDr6nTgWGvmkvBK0k+4FGZ6iEZKp06zkO+GfZSFcxXlJrI4UXuTwOPMpsmYdQd4YFATT3lioNOjOpaa10bNse168Koz6m4Rc59ESc9ddxm1pB3ZWqqzE2Li8tgQYh2Vhj7RhBbgYI2ZyIryUYY2bpfjaQsWKK6hw7cfHG6rY4xQ5NbIzESKTh456PV5HU+j+3l7WjCxJ7wV4K4dTiUPBcUaAKxQ8oWDRGP/AYUkepyOI2+zsn8xRtiZiWznIqlRoeVqU1fKvXKV/Oa8BH2bAx2Vgpti3jXfmMgecJbJ3nuth1Wm0uwo16izQG/ZE2nh3QVhvGa9g+uqg3ermV5xNwkfo/SPtZtmGJPcaWj0Lci59GLA/dxUaj+voPyFIul8NYdWb3a7G82bmT0RkXO7MXBUz/e7B3TZiXMdsYBC4r1rS4IZb0X4J7Y4qY9H8kxUEhjFMV2kU7MPGDVyPjJUFgKo+nuQpHL3eE01EN9QRRSoAZhR4/zFsdU0jxvLd3WOm8XBptFuNMiAr96NuN5RjbgwEH6oliT12ZDZVk9lB4X+NJ5k5mxw18RBU1T6solugDHaqquG1udV+nVPlq22KwDc+8E+wMbHqxNTSs5zJPYElunoCxebnQXiT7J92dEZMizgt9KerdUNvqm89rDbZduV8gl4wJN9olT2uEjrZ0zy1mciDhjC08tKPZ4uVzpnglRhujnnZCOl/qqFXIjUumVJFFYjFfqmQuP4pCWiKxBbtL0XWIXlhFp0OLKCeaOMFmiuJBEt1K01uocG2qMUja681URYpOvuEuzkE8NAIFBjfOcjwXFT+e9cyjM8yGzpNgJBC7KXJAiusfpN/5E8Eff8+XOPBhCdVopCOfP55RSCmAzJaVJSA/bQ71QsWSQ0HVPuZHqyPMG2g9JD5DVB0gr/X2IY4a/o8S5e9stZTWnN0cevdIbanu2DOOwMvpbRSJ6gIfbhs0Thaf3461L5OLC9W6MQ3gD+Wup2qoOgswHYjRu/IBgh0CzxHWCaMWp2Ee1mJ4o2uCW6c7L1UPULqqeGft9XiIubKqBXbVM0licvrsc2h0DXwTy6C8gQy8Gvs/2rWSu5WBDtNr5lmdLCtJAV4OowiXQVyKg53xgUlJRpQhZJ5y58WRT6bX1yuwq6MpeZRuTiOuO9aFboe2ZPG6oraooEp+01NmMBqiz2Gh1w1f8PA3oM83u8DlxJhFyu7BXhRvF58rNO4q1AX+kPrZUUkfWpQsrgeLjuiHR4nNyVds0m+zlW3A+O8t1u/Kh2L+ddBYiiVKbk91KaMtEXqYr9FBKdlTAp8KyWp0bT1Cf+1K13+iEAm34MeQ2wRoxRaq+LRHWpoFj4fDGhD1NnfstZGtlBZ9uXmWSlKCVjFk2iJzoe+c4htuUq/kzHG2ivKH5i70fiCvECo4pgN4nsUlc529sjO7rS3XRIWHvczSvd+iCvW2yI3sQKajPLH5jq6hcwJY/xDAbc8d5cSvVTRRQdNrtd5uTc9usHTWNF6Hl8bLhWbAoKGPF1/x23ggntPRyM42xHNXZakPzgqMazXKXGmEmsBhdW6J3iPm92odYnMtb2d77mmccQyFKCl6U4CvBWxy+k1l4xJo63Kq+Mq/GrqXK6sQUW91IFTc7DeecHUouqsbDBbQjrgYlKo1G6f7AW56pKQuDFoPTjb3tKskO5pA9p/ckafacPabisIMii2kTq2eWiLUPBSLMIClcbn3NMmCoqcTblVQanFmxELGES9k7LY6q1O0rSDoe7R23U8KYgcLaVkXGPxeoA5hFZKEgL8IUcvbKVnKyvUg12Fk4zvdWWnPzgjdQ18cXXL50ozIImR177C9xh9cyF+eUISR5l8VCySyHITKhmuor6hjXF44bC5kTBUodcqsLCmOZXY4XTSTadUasdgFz6LlSULwN2dn1haGKfGVxRlHtGV2NhK1rOrFYYDFsWUJItUZ7WXQCyfDwFhqORZLvIRkbiHhJoWjeCQnox9f5Skiu/UVKnfXF7VNaiCw477QDyWMLHN/GG9znhXZV7pGouLDIshUMze9Ka8XhSyNm0auMO2lurhoshE0tRqF1byBLY0ip7uTqPZ6aMYTaOd9ITVtSeGacyNg4qpeuUtUsgmp45/Gmfxtp+0CbvsX4NGL7w0EIK1ijrrlRZUJClm4KzVcZI5T+Mu9Y1bPktitt0NcqMAg7Ndqug9oPPULqsTktC5Ag8OP2tL7KwnHrznd7Q1HHpb9ukMI4jHZotbg7HNE63Z6269CpT96FPfjhRis2JbISU6xMTMUPZGcu0nngmTIh0DsrUfyyTZxFL9K2G82HcrSA3TDhVJEnFR4adIpjrgarrehhuRXQRr9iIptZ20DMG34dp4WL28ao+BelzKHL0Tp2urSggkHM6G2zb1wkcM3eXApmaWcEG/kSZyamupFOoauEiw72FTg+wqO5li54fepGfzmWrclvQCtu5auVhDOnCN1ZGnxlFrK1hI7UaC5FhIo8XNSQuhn6akcbqKGhpUpp2naJb6KKsm77Vl922xwid4sFnOCLfo0Ll6upI94Ca7yoKAgLbVLPutBenqBq0vIlpXf0AEm703qE9C1ThWQlwHuMyqt5l67OPX9ATjE8DrcNFQU1BlI/pZfUsDkOVr+2A1c5XbM9aGQM3Wou4Uiqa1QoD6gb5OR+s730LaWOkZrZdYkmWxGL1gUeG3x60btLr0Qa2fD7zl231lC6GA1ZJNuh8OW8J/Z5a/U0dqwTB0bYxQ7deYbFqet47uY9AngCRs9XMcjkTl+PR8kRxQjOohxF95CHDSWpLOBo0XAbpl2KxXJd1Wv2mNFKSe6j3ETsxYEwwn21zNra33M8cwksxO4rT0RW7bFDb0WtNyS951BNxBALGedHZH5WLIpS/AIhYD4JB2UVJUJKV2zogI70xEsqwdiZciKBxmXnU9TcuLoe3xh7j7mVvS16OknXAkUahqRsu1w7YHuTA/s3f3mIVz6qV5i86uFsO/onVugvJF9cg96BF8wJXh7ZLMMuwZLGz9trmOys1jnVoUb1V5sRrvsDk51rvVL21JhX1MCFtbZIYQp2pHpgosXiEAW7JWVt2jhBFW3cOrhTDRqmWHM3jpEdaGgo28nFwbVAbKELgRK3F7zfzgvbGU5wv/WM1l7V5rEhZZbhwD0j8olF3DvRuYPrDUVAq4rya73TMiKpCVcLOzMiVJRi18AHg1WLcF8taeXgORcrRhW0JuBSC4Lb9qgb7javAi8f3Q11EEB5pMMMlMCzPG+RnvfXQ+V1u0EfZfkUL7kIimIFbKcvo5tnQWMpFiZZvX+kGhQiAmzb7ufNgmBJZCCiJqJW3oVY7A2eJmxygYA9F0S7wTFCSfoqLNE5i+wr+pzDJdwscUJsL6u+htOThbfKatsOuk5CfLAQ5oHTVlqbm1Rz6Mkc6yiHWxfQbb+KiIM3ZNGVVWoeAkG5Gljd33rcwiRyLfZTSo7bEAc7EdY9q3J7qVfkdl/Kp0PSzBmcqJDIkuu2PCFlbwbcDRFt0L8R9Xy9NqPdVQ526ZK3CRtzNqJy1OE6NHXHQmsjXNUOPKJXgrkyO9OEPOQ8H3t4HVWYt5XOOntQ0FBvD9vDen/0BcxNwFZhLVqQoeIKCtc3KT1ztjiEZ3o7lFatxie5vOm11JFDd7CNHjT9Gglpc7rVs8NG311PckZ7MZsfKjtNlmiI0+hpHwxwjutOhcvOIWg2V32uMfsYZaqkviwEhsm9XB8RxTzV7n7tGtCAbbO1iMbXY2ZuoNthxyIss6cVB7N80J7Go3DiRRKe9wiIgKIxc4ISl5pZXnHHlpanxXontJAks8J5vX759DIdQT8Pkv/eK+PpWO//2eni4yDw7dXS/RAZ1O8v97W+/E29fvn0Utoh0Opxlloljf88dPwvJ6mf/623EpOI4fE+dnoX1tdvx++16U+/WvQSZk5Tgf33typPmvuB7qcXq6mm33Govj0Prl/u5qXFdAr+gzmPU/HQz77V+bfSrcPSfZl+DWF6x+M6oVm/XfrPM2YwfgD+Cu3qG7rEv7llMRn8fNUB7EReoVf45ff/DSstqrbJJQAA -->
