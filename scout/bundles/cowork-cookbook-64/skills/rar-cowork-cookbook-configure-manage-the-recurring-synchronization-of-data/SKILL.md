---
name: "rar-cowork-cookbook-configure-manage-the-recurring-synchronization-of-data"
description: "Applies a bulk configuration change to manage the recurring synchronization of data from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_the_recurring_synchronization_of_data", "rar_sha256": "84faffbd9118032bf33f49b0dd2e6f919b736d1869012cc4beac4734870db4f7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_manage_the_recurring_synchronization_of_data`. The original RAPP
agent is preserved byte-for-byte in `configure_manage_the_recurring_synchronization_of_data_agent.py` and in the RCI capsule.

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

Manage the recurring synchronization of data Configuration Bulk Setup — Applies a bulk configuration change to manage the recurring synchronization of data from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-the-recurring-synchronization-of-data
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_the_recurring_synchronization_of_data_agent.py` and embedded as the fenced Python below (sha256 84faffbd9118032b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_the_recurring_synchronization_of_data_agent.py` first:

```bash
python3 configure_manage_the_recurring_synchronization_of_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_the_recurring_synchronization_of_data_agent.py   # or on stdin
python3 configure_manage_the_recurring_synchronization_of_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage the recurring synchronization of data Configuration Bulk Setup — Applies a bulk configuration change to manage the recurring synchronization of data from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-the-recurring-synchronization-of-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_the_recurring_synchronization_of_data',
    "version": '2.0.0',
    "display_name": 'Manage the recurring synchronization of data Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to manage the recurring synchronization of data from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-manage-the-recurring-synchronization-of-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-the-recurring-synchronization-of-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '33c8fceeffa06e25',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-data/manage-the-recurring-synchronization-of-data'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-manage-the-recurring-synchronization-of-data', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureManageTheRecurringSynchronizationOfData(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageTheRecurringSynchronizationOfData'
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
    print(ConfigureManageTheRecurringSynchronizationOfData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZOjSJbtX9HEfMiqITPYkZRtbfYACUkggcQmRGVZFPu+gwDV1H8fR1JEVnV1z3vdMx+eMsNCgPv1u55z3YlfX6yuDYv65euL4ln5bGOlaRR69czK3Rlb9EWdgF9FYoOfmVPkbR3ZXVvUzcvnF9drnDoq26jIwXS6LNPIa2bWzO7S+1g/Crramh7PnNDKA2/WFrPMyq3pW+jNas/p6jrKg1kz5k5YF3l0ewwv/JlrtdbMr4sMaDKL8rJrZ+vB8dKZH6Xe51kfteHsaqWR+5gxqVsXaWpbTjJrurIs6vYV6OgNVlamXvPy9aefP79E4PvL119fnNRqwK0X9qmkd7hrpYae/K6T8keVJH8FFAICU2AImFmOwGs5uC692i/qDNxyPX/2vPqh8VL/8+w//iPprTpofvz6LZ89P99epn9yl99d0BZW03ruzLFKy47SqB1fZ3TaW2MDvNN2dT75s2knhV4fM79LKsrZX6dnPzwWeQ289odvLwVQ4a7xt5cfZ0UN1qu76fvrJKX84cfXtOi9+ocfv8tpOjv2nHYSBrR+fXteP8WCgd+HRv591b8CqY/g2963l98ZN30eek92gpkvr3ER5T88BJd1cfVyK3e8H378R2Kd0HOSNGra/ye5Pz0Eh57lApueiv/4+e7kn2fQ06APmf942RKE9Z+xBAx/X+7z7OmofyT77v+/EZ1GOSiVd4//XXF/bwL019lP/9C2/27C55n/7WXlpdEVZIedel9nv74pxzX70yf3+81PP/8GRP9fxShFVzt3CW+gmCPfa9q3t58+Nffbn37+6VNXglzzrOytq9O/J/Pv+fW+zh88+Bz1wx/ngvW1PMmLHoDEe6bPfi3Kf6t/e53pEx58v998nf2+XqYPNJuMeF/04YLf1UwDdP2dH398+Q1gRg6s6Zz7Y1Dl//7vs0Pk1EVT+O1McQqASyDAbZR5k/JqGDUz8P8Bb8CvTQQc+xwH8n+K8BPgfvk/zh1evzhPeIXfIdN7e4DkG5Dy9gGSb38Dkm+F/zaB5C+vM4BboNSjIMqtdCbTx+O3aXreTpqUtdd49RVgjD223heATl+mLwBSZ7/8awu+3WW/luMvd9SNHkgms7sJxZou9V4nT5xDL3/a7QAE9wYgFiybFo71wPDmM/BQU6TXiQyAok0SpenMjcD6gF/GB6J3+ddJ2C+//GJbTfgtf8AuPnsQTwODAR/qzL58Acb6aRSE7bfcc8Ji9unX3z7N/nP23826C5/WOAJKeMYNaMgrkjgDddhlYBgIKUgCADL3uP3629PlQEwOmBJEOfIn5psmgzxOPPfd/8qW/oKR1Mz2gN+Bz7OJlibCi9rX2c6ffegLFp0eTWgfFk07c73Sy10vd0Yg1QLmfHgyL9pZA+LR+OPnWdc8mPQXu7buKmYAEKz2l9mBPQJuKdKJcesn14DJIJbA/R/Z8bgPhNSfmhnzLuJ1Jk6ZOyut2irD2nqu4VuPuABOeZ8OhFuz3Ou/5ROxepOr7pnycA8YBDzjPEP6ZYo56AoykGpu8772fYw1MaB6Z8L6W948S8Sq7x0CoAywaNABogfE8ZdnSjVh0aXu3X9A00nSMwruMyr3HDz8M70G+4eGhZl6GAVAUDn71mEISsz+P+xvJhvpzUZeb2h1vZqtRVW+PHw/dWpTjB7NHWgrZiABH3X2vdV4B6p3vP6WpxFIpHr8y2PkPWLPMQ8MBFDhAoCR7/JBugDfT3Lv2TxlJ7B28tC3/J0YPgN33VEQmABKH5TG5KP3Baen75qGoL6n6+9Nwj36tTuZDjJ2VnZ2CrLJ9zz37oQ2rKeKfEYHpLY3ubUPIyf8g1UzIB1kEJA/A0pEoMYAedxdJxbATBCdexQ+hkdT6wW0cDsHaAtaYe91dgZFNSVWAyoZ9E/TGOCFT3dRs8wDPgYqfni4Ca3yoczUPT8VtKZYFBnI9d9H4PnwexncdZnUB1KtKUe+5f0E1q43PCL7oeczVkDZbCrc+6Q/hvtp6+z3DPaXb/ldxw9+AHiQTuT/O+fMQB1mzT3lJjhrACRl3jOBQCbcef71QdWPXuBDl69/2jL88M/tKu7kq/0xcl9nYduWzVcYfhDmO1++AjCBQY5Epdd8584vjwL8AlT98lGAX/6mAL8U/peHc3+32sN5X2f/nMZ/EPFM9a8z9BV5RaZH+8jxplx+foCD2C/M5QsxPf2Wy973yD/TYwLodARk/cFW70MAZQW1F0yDH+zVTKTXA569wzUw+Fv+kR3P2nngEqDapvhdTd9pG8T6EcoPVgGP8has7U4NYeBN26d0Ur/xXr7mXZp+fsmtzPvXtk0TmYCUBv6Z9l+gvEDL1Ube/eqj/Zou/ripvBceQAy3+DrV3+fZ1Cp/nn10vZ9n7/uQ+2Yv78BG7Kep456WBEPBr4+xHztW23sBe8F2LCdbHpurqdF7NuB/VmIqO6Cx400NQvFRx9OKfxICvgSBV/9ZiHT/YqVPMGlaa6L7qH2HgAbo6XYT9INogtIE1QYyuQMT/rwMWKf2qg7wqjuZ+91/380qHrb8dndD+9ih/vryDirPGDy7UTAcVO+XZmJWGGQuWBBcP3IMPPtf6lOfUgE4go4IiF0QvuX7trtE0QWCY7aP4z6xtBHXxTzKX6JLe45TLrqglgiKOQ5he5ZDzHFiMUdcm/DnQN4jf9+mpiKaNMUsy1k4c5Rwl3OLcjwcsXHHQzHUneMeQi5xf7HwCOC0j6kJQNan+Q9zJ99+tMyTm55e+PXFpggwcks0O/rxYeGlbtln2JbDPVSn0DDg1An3ilS1YO6kJj4Vl9I+YVUmt7uo2ekYcybTvZV17Gi0ws5irkUMBde5AlEm5p33wuFcIrdrsKkj9MZjbm7iholcDkG26rXMHCtNIbWKP2m6pklpI3QLLNLP6xG2D03rZGtFOzWg/iSVtwtTPxMlutQp+0zom7MeLZcQpJ8dMs+qVNaV/SYIsWoj6rEQX4jhcoRUulwx9U6VwmbeV4Of24qgRYiVWNEF6XSI35RxiUnY6RwthITS+A264M/emRKceHfJVyTs51sIPqoipIsD3NXiYDjq4nTZnuamYlrnk24nY6hQ+C5ec7LIn+WVYLAkrhzggdNSi9yfmhQlRG3fl6bNL4hTKMR8wDGcqevFmR8co2bmgiHpB65x1UTeI0U/pDp/PInFifWFNJIKKrnoaSMfVUMRcZc5+vLYornQlRwu43ga2ukpa4gQNYnqUsc4vcAqmUqCRGn0BYzvuFXM2bwqmbtc7/S4tObusA220sC7BEt3gXK9XUz9aAvElupZr4N2jimyhHEjxorN2VavdjnhRvpe0xWTO3V6FuAycSxXZqSe2boSGQKN5lqdqSGvGnuxSK7yFa15zbBwdUx5xjMCTxq5nVWzKskIq5WtgK1T1TbYKc5vjhRyw2rpEE0H2ai4kDtzpApcJcxmM/TKJjJrE8qcYLsCVCaXSn1Or0iNuhnKKd1Nb0n/sk1VztywaKEQ5A4SdytxzaIwyLe4ZnxClUlHqK+9I2NxEd9yTHHiINRJen/RlkyzhOduWfGpmWbu1XSZehia+Johcna86FuKu5mWjBJWN7D2qScHBCtiowvF2Oazo2FJzq20lYvHZ5AR4H6d+SGyyOKRZVufQiIZg0tYO8xNSLhehxzmiI4BT2xsW235NdcNGF3YnFpc5/YpYz19PFtBur64jRhf+RZmur0knpomCxanxN+NcxxjNgf0lLpdAOqLS05psxi1vtqX1m2N2OtNN2rNZmT4VSP0q7boOdaP3IQ12M2IBLXDHYa1dmjg7f5AaGJPbuwYUy3C0AnTl87d0TIEjD9lXrTeCNv4krN5kbIJISdFxeUUqe9zBlK97po3tkkKtRv63gDztobf+PMtXMEEfFuZKLmj5qMWbiELXvqkso9QzOgx2YxKAokthK/wApe43YrxdPls4WJy6uIja+fdNpYiuNQw8QIlx41FomUE93IKilXym+veiw5OUQmu519L9+DCcnq9aGsX89nb/kYcdXN9JFFqZI/yXsNAXEpkGXsnWDd5xeJCUP/uVk9DY2PONWZnUJUrcE21FQCSCYuFRXQaL90U4ZLyxNYg+ZU6+ArVhNzZY/jjIFyzoUDWKkzQQMQm4M5wwNx6nwH1JRndwlAHaKfGqbrOzx7GRIs1mZDM3i2RgDluLr1sujR+1ipPIqm9Ymm9KUUkEkT766XcrjYHYY5tFQ8RTsJxu1T1Ta3VcU5pB1fS1OsguWNeYVJFIvRWEJqId/j5OtdxjcJ8RLB1pMjHnZvPd4crrsD7rdLYzOl25SlXlJxMiNJdRbtG1SAwxLieEK5xfGfF3IkWR/q2GpvK3GCoTDd7OBhXZ4vlScyNLAha36L15bYYD/7VGAf3ygc31api2tnwTZOf5gHmsDcmW7M7Rm20CwFfxkjfHI5mJO7TG9crBu9422Nb1xazorGDw7KFHHO00iO1kiUbSyFGyLSUIpY4R0jWBl0RnmzlY0IUvCvjoZZtt+ah6y3ZatikdVpcKed1iV2osiSu2l4wERTKjf1iLhko5q2RLpDOB3Re10vg0nVBylf1bJ+9oZc6pnS9tFZVnEKUrY5vnWPHh/sxOSygCKbO8rpII+OGhEa96AxHu45pkcTHq891owKy6nRZaAt+lWXa2Ba5UiWIvNUvBSKJ1yPY1q5Va+HuC1k7wGshYZKaooqkmNcKdUPkTiaHqsgqxRUBgyZDeU4N1gqKcKcNpYwq63O27/cBQsyL3W3VIfoG9lS1RtdOTnkog9zafEdyemio0aZBKX7RXVOxc05W0JrrBUTuOQ9xuYhYIYgjHSaMMa1yTF04v1x6s8yOnhLxO/OEEzzaRzFdWe0ZFo1WW/GUOUq0cYmqNSUlqX6bU2yNY1Da8UcTIGB6IHjBLOgAimnJClRDX46DU1G94Fr5ebtY0VUpuBuHzhjRKo9JIAjYUlN42GtxT8K1Y74kuVUm252RZtk+kxW025Jr3zVp/pI29nl7bkKFjpJVtGvzrl6l0po/dBe7LJFCPyPVekepatddrsJVZXqRMHm1q81qThGYu2JVXt/GWeBkjeCs2HGzYPGAdxhkoe3BrkqIO4PcWTuRBXypQSt8nAtCK2/VTZeKw/m8Fpnu4NPHZgPb4ljJSLhXDnyM5HJca2p9EuH1nk/STbcXV01iXykJPaw2aw6SABieoDFKL04c28RFseeavKkULVnBsTVI8prHXeLI0Oshv4o+cxF9y2XYC7Lp2M7b1V4uC2p/EXpzYxDR2VqkSmgby0xb7aWoF5YbXBxDQLQ3vlxsqHYdsmt2c8UPia6XdHBgiMtoQbnqIO0O3pXJiTELH6rPMMYoWDI39W0/OgvytFHkS2bPrwvjeuz0dUnnZSM0LYvDt2FJjE6bs2HMM1kv3QBi7REi34j5sFpVKrM+n7HbctHWawzmsjG9HHJt5FAI97I113BMveToGNHVTlnrcrGjhcvyfAmP+3M/5hplza1ttMbWthatEoQjIL9exMd6Uyg9bUItciYWcLc9BKl0rfpVzq7botC1uYHaG5ZwMYKNtvrCJaoC1+o1aSi4ICKFYxKEnJ7W4WmzRHF+06OBUp56Ke8prond2xZfrxhxy0bO1j9XVcZkzi6wz9JFkKFbpg5mAVe2t1Nk3xZZJMxMwz4dzYNwHDmtH9WECGxLzhfFHKClw/nr7lLlFp+EBclB6x1BqOqRu+jW2t2d1uxJd3hdOSCUsaMwd912B0LXlnuHkXF2L5AFeYIZwR13QSdhpg7lnYDTzMEG+7k+Ghshoy7J0tirgint5oKswy22GCiz0sPh4Mmb+NBvKf02pnoaY4xcEUtL6qCIY3p2TDatAZ9HFOI4jtexY0PhsRqiyFwRF0m90BMDX9V2eIDlkzTaTcFeaEpdKCG5O8TFeb5zZDpQO4LnTqjm66bSbRha27EnhcDVwG7Wp0PWoKSt7Pqq4VeanYIWhqqC60Xyxt3cma84srQkcyW1iFbtih2rKa3VDvNQ7N1Siy/9HkK2drBHLPJwa7cqyEJtFaIy6Hi0PSZUiJOdRTxcijtuGDdOTsSq7ZDqQeQpdgi97cGjwUbFyg9UOJeFSgN9Z1uR8mnHw0stJeqTlnsM5qggolYSERuKjJE6OMXpUEgniqOHc8uYjns+CTRbpfgw0tVxcekbancshTNtZqWe7Im6RniMbBBTSypmg22dFMF30T5PF+j5hqAatWRUa4hYQKX09SqtiAu9JbqMLNKV2ug3s3f3Rxbwdr6p2M1qcTtTkLXr0bGqtWFng96mWdnhyZTWWn1ZRfYBiZIDBJSU1L2Cu24MUTKtq+X8RHM75mxcsw2L+8bgEZuK4095GvZDAuH7MicaupZjIdfo5QBdaMRdpWVvVZmvaRyG2pIXjQmuaiJitGq/zHcGblDqcW2E0qbe1xYUnuSV5nOoub1pXGOSRHuRBCPBnMVRHS4Ho9OlsHNlAtKlVUhwKApvAf+2vnqTrB7xyNGG60tuht5cmUvQrcXlolvGJobC8RyUXhFauL85NgiV6ol1C0ssyFhE7Tn8tFZ0uytRbLTH4txkGXXkxVss9tkyOowHeDusk+EK2csVobgGny+RS9xsyYtkhXJwOoi5ENtNTee3Gk0v5VI9g95d2qIFr6Y9IiLM1u/My2K4DZq98s8i5rYUukozBpZCsJk44reri+W+ThDMdmHPYSgIl3QTnua1D99UeKtGBn91L/C+vk1nCX2OBXlnRKBGijXFxn0LlR09QDbS23oM05krhyrSrG54GoTXjYTvDiZEw3TQxItscTLoxQ4EUQZ7dQxXI7eZY+puQAzmbJ4HHNl2VFKTZ+VwulXzTkvnfbw9m8XaGZtEZfaLrWVQ6XV70xXIvUFwFUdbSF7SsNjnlWrebBJ3e18kMXQwdjdi7pXnpOE09spDfOUn8XwesEaY9X0OG6CnPuU8JQyIPc+o7ejqXglbwxIH/fzBckKYOWA052Wr0YNYYj7vtlt0q5rK3K1Q7MQBdEdDY8tnYm1jOgm3gmsoKKuO8MlzqDjf48eO0lScOZxoEiJz+xjUOSFzfRrILN4xazuyCRDhG2Avt/FRFAch6YOdTVJ2x3escSD9vEo0FyZ2hHPD43jcN+wOExLxypXkQiBYA7pRoPuuu2sDtswrRml4IzxkC8Cr12rhHUF/5q0Es6OXGjNYVmGwuAXZ4263W902gA7opF8uCDqD5SQ7um7oGVcmlV3cL06DC8jYcuSbciO4k20scrNxRyMjYnv0CoLaeZcigLMFRariEmXmjhDtCI6aSwcePqqq7y59pk7IzoUvYrdguUMzl9ULTPtLiGk9yWuuxQY+4nRZOwPrzC10FIkh5uq9aEvrkXEQscXQla2CLbfkz5HaqTrLbS28QnTpROI8V3lxNaBbe7gcu23mBrvd3suktRGQhd33x2IbOfAmRNwW8J5KeFfWPS1TAw3q+WHhrqzcoPc+wdTtEo4Jjwe5aPotH6DYvPTLFpvXOJmfruqiv+E+vqyMo8Bcy2NkCwxFz22KH46Hs5XhhsgYIF9zZy41vIhs5m4AQ8SqGZIbBdsYjeHJ9XrtI/IkDrJarHFCyIaqxDzIdsNVXut+YxYEX9gwdO59JYfEFS3SvOSgos/FN9gTiLDAvYochTVDbTIq0a81ehZIxDPDnaEvxFOnziGJXhUm5tG0KAcNz1e5ud7Y3WUTbMuupM7Ecd+1JFaQniRR+by5GBVtXizEwHwIEOJq1ZLQMQg66pJdd7B/8RS6PdB630hc2dDOsRiDsYO0DOHE1YJwyHUiHFMFs0jNI4+yhG5BS351g5yVCawhYGyh+ttLEXXO7Up6jKeaV9QhD3tAxIvjAhfnSydYQHAxhgdnaYqxW6KymyULvR0tmF1wtHiGKR3zlnXmLg1eaoeBWIm0wsDi2RiYqNgk46nIXLzB2KsXKVLQruybDG0go+gNySGQxCUcnOfH+TkOfJg+GfbFXpNCT9Mvn1+mY/DnYfb/8CX4dJb4v3ak+Th9fH8Bdj/K9iz3632tr/9TRX/+/FI7EVDzccTbpF3wPPr8mwPeL//ay5RJ5vh4Bz290xva97cGrRVMf3/1EuVu17T1+NYUaXc/eP78YnfN9JcfzdvzgP3l7oCsnE7rP9QA3y03i/JoekP81hZvjxPv6X6UTy+rPLD//rgMnofhn1/cEcQ4cpo3nCLfvLqcXPB8RTOdFk/vaF5++y9v8w1/AicAAA== -->
