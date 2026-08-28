---
name: "rar-cowork-cookbook-configure-develop-asset-policies"
description: "Applies a bulk configuration change to develop asset policies from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_asset_policies", "rar_sha256": "32eb4ee5f83d1bd040295cd9f3b925843779a994d5cf15fbaaeca432787f5cdd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_develop_asset_policies`. The original RAPP
agent is preserved byte-for-byte in `configure_develop_asset_policies_agent.py` and in the RCI capsule.

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

Develop asset policies Configuration Bulk Setup — Applies a bulk configuration change to develop asset policies from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-asset-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_asset_policies_agent.py` and embedded as the fenced Python below (sha256 32eb4ee5f83d1bd0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_asset_policies_agent.py` first:

```bash
python3 configure_develop_asset_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_develop_asset_policies_agent.py   # or on stdin
python3 configure_develop_asset_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop asset policies Configuration Bulk Setup — Applies a bulk configuration change to develop asset policies from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-asset-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_develop_asset_policies',
    "version": '2.0.0',
    "display_name": 'Develop asset policies Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to develop asset policies from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-develop-asset-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-develop-asset-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '68621f893f2abfd6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-asset-policies'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/configure-develop-asset-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureDevelopAssetPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDevelopAssetPolicies'
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
    print(ConfigureDevelopAssetPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZPiSJLvV2Fz/+jupap0oqPGxuwJECAQkkBCCHWNVesI3fct+vV3fyEgq7q3Z3ZmzNbskZmWCHn47T/3CPHrm9U2QV69fX5TgZXNtlaShAGoZlbmzlZ5n1cx/JfHNvybOXnWVKHdNnlVv314c0HtVGHRhHkGl3NFkYSgnlkzu00etF7ot5U13Z45gZX5YNbkMxd0IMmLmVXXoJkVeRI60yqvylMocxZmRdvM+MEBycwLE/Bh1odNMOusJHSfrCbFqjxJbMuJZ3VbFHnVfILagMFKiwTUb59//tuHtxC+f/v865uTQEFQu9VLHbB+yucm8cpLOlydQP0gWTFCZ2TwugCVl1cp/MgF3ux19WMNEu/D7L/+K+6tyq9/+vwlm71eX96mn3ObzZpgstOqG+DOHKuw7DAJm/HTjEt6a6xnFWjaKpvcVENfZv6n58rvnKBv/jrd+/Ep5JMPmh+/vOVQhYf9X95+muUVlFe10/tPE5fix58+JXkPqh9/+s6nbu0IOM3EDGr96evr+sUWEn4nDb2H1L9Crs+Y2uDL2++Mm15PvSc74cq3T1EeZj8+GRdV3oHMyhzw40//iK0TACdOwrr5l/j+/GQcAMuFNr0U/+nDw8l/m81fBn3j+Y/FFjCs/44lkPxd3IfZy1H/iPfD//+NdRJmMJffPf532f29BfO/zn7+h7b9Tws+zLwvb2uQhB3MDjsBn2e/flUVfvXzD+73D3/422+Q9T9lo+Zt5Tw4fE2tLPRA3Xz9+vMP9ePjH/728w9tAXMNWOnXtkr+Hs+/59eHnD948EX14x/XQvmXLM7yPpt9y/TZr3nxH9Vvn2b6VPzfP68/z35fL9NrPpuMeBf6dMHvaqaGuv7Ojz+9/QYBIoPWtM7jNqzy//zP2TF0qrzOvWamOjkEIRjgJkzBpLwWhPUM/k61XUEAqeoQOvZFB/N/ivCkce7Nfvk/zgM1Pzov1ETekRB8fWHf1wf2fX3Hvl8+zTTIN69CP8ysZHbmFOVLZvkgayaZRQVqUHUQTeyxAR8hDn2c3kCknP3yz1h/fXD5VIy/PGAzfKLTeSVMyFS3Cfg0WXcNQPayxYEQDAbgtFBAkjvWE4TrD9DqOk86iGyTJ+o4TJKZG1bQ7Lwan5DcZp8nZr/88ott1cGX7AmlxOzZI2oEEnxTZ/bxIzTLS0I/aL5kwAny2Q+//vbD7P/O/qdVD+aTDAVa+YoF1HCvytIM1labQjIYJhhYCByPWPz628u5kE0GmxqMXOhN7WZaDHMzBu67p9Ud9xFfUDMbQA9D76ZTX4H4PAubTzPBm33TFwqdbk0IHuR1AxtaATIXZM4IuVrQnG+ezPJmVsMErL3xw6ytwUPqL3ZlPVRMYZFbzS+z40qB/SJPpuZYvfoHXJxnIXT/tzx4fg6ZVD/Us+U7i08zacrGWWFVVhFU1kuGZz3jAvvE+3LI3JploP+STZ0RTK56lMbTPZAIesZ5hfTjFHPYwFOIA279LvtBY01dTXt0t+pLVr/S3qqmUDiwDUChfgs7NWwGf3mlVB3kbeI+/Ac1nTi9ouC+ovLIwfXfHwtWf5giltNgoUIAKWZfWhzFyNn/16Fj0pvbbs/8ltP49YyXtPPt6c9pUJr8/pytYPufwaR61s73keAdUN5x9UuWhDA5qvEvT8pHFF40T6yChe5CeDg/+MMUgP6c+D4ydMq4qnr44kv2DuAfoGMeaAVNgOUM033yxrvA6e67pgGs2en6ezN/RLRyJ9NhFs6K1oZem3kAuA8nNEE1VdkrDjBdwVRxfRA6wR+smkHuMCsg/xlUIoR1A0H+4Toph2bCAntE4Rt5OI1IUAu3daC2cBIFn2ZXWChTstSwOuGcM9FAL/zwYDVLAfQxVPGbh+vAKp7KTMPrS0FrikWewvz9fQReN7+n9kOXSX3I1YKxh77sJ6h1wfCM7Dc9X7GCyqZTMT4W/THcL1tnv+80f/mSPXT8hu6wxpOpSf/OOTNYW2n9SLkJomoIMyl4JRDMhEc//vRsqc+e/U2Xz3+a2H/894b6R5O8/DFyn2dB0xT1ZwR5Nrb3vvYJAgQCcyQsQP29x318ldrHR6l9fC+1P/B9uunz7N/T7Q8sXkn9eYZ9Qj+h0y0xdMCUta8XdMXq4/L2kZzufsnO4HuMX4kwwWsywqb6rde8k8CG41fAn4ifvaeeWlYPu+QDbGEUvmTf8uBVJU+sgY2yzn9XvY+mC6P6DNq3ngBvZQ2U7U4jmg+m3UsyqV+Dt89ZmyQf3jIrBf/CrmXCfZip0BnTXgdWDZx4mukWvPo2/UwXf9yqPeppgsX881RWH2bTpPph9m3o/DB73wY8NlZZC/dBP08D7yQSksJ/32i/7QNt8Ab3Xc1YTIo/9zbTnPWaf/+sxFRNUGMHTL08/1aek8Q/MYFvfB9Uf2YiP95YyQsj6saaOnPYvFd2DfV02wnRoQNhxcEigtjYwgV/FgPlVKBsYQt0J3O/+++7WfnTlt8ebmieG8Rf396x4hWD1zAIyWFRfqynJojANIUC4fUzoeC9f3tMfK2H6AbHFMiAwIFNArDwGMLFbBclUZxdOC7rETaLLxiSoGnWYlnSXTgetvBsywKORRI4zdAepHMhv2dafp06fTjphFuWwzg0RrosbVEOIFCbcACGYy5NAHTBEh7DABL8bmkMofFl6NOwyYvfJtbJIS97f32zKRJS7sha4J6vFcLqln1FoiHYzatkPpgaLdidqhpS7etGsdkd3f0aD9uAbiqf4c7p6rqIIyttuYGwTLbcyqFCrZCjOI/vNV1fziBh1FsZjsft3gR0Tcsjo0TSJQ7V6M5em0OMNoVoHEK3vMiNdwjjRqs8lbItTSuCg9eAqwQOunMlaw9B9M7Rd8b+vNnH7mblxSvbxlVMrwXzYg5pd62Oeh0cqEPRZnZAxVSjVju12Ld7uSVxMrEurbJqzI0lDKaZ7RHevjXlQiJxK0Kdq2HQFDPvxJB1jYxsqwW18Lz7UasiVSiyQ+nEB8JOeYvO9NA8V6HUhAejcQZUdZA+6aXhinXGQYzdRCsqU1ToYSmr2z3PL7dEi8c3nWyNjYrfOte6WGbZudp6uN+kHq2E6KwnJlVYo31apURZ8bGXZuN2Pm6h7kOzrBKCD+ncRqqhGUs1sRZ8Thw0XTk1F5ckUvOUbvxC99Yscbo50ETEVPPkzleObahz2Q4VTnbTM91vlhInd3OyLOVx0Xt42bgueyZHW/KrbIOjsqyB8qIpA3u5Uait6ptzenRRB20V6ra9pY2fUuLFcm/tYoslzAmVxtHaK7hdGWpZEbp1Vet8zTCi2J/3a+OmFoUVyXjIHpqTbTOJ3KWcsxLTDVVh5rpGbTuPXCIZTi2CxYMo7qVralb6/HrMpYAd8rMW6faILHSqrbZhTphly3W1OBQpNiwt9MCQ+dwVuI5f6giGFqG9Vub7GnMOVdcnUbM+7YijExfr5XaBLcUbyi6ZObJji1LQbBkzbkM2B8zxhNBmlZn3lj+3iYnvYumoXaSTpqV5EW3zeTqyQWCHCzS7LgbOASt+nu3Qft5zlcdeF4LvSAi12o7zJCPQAYkY46zSV8IWV+y+MLqzeNOklEVp0DNxeR67K31J80CTipWLaR15NM3hsE0QbBMjZ0FR9sRtVSPqKjks1kOn4n6OV2MUBLV+Wuw2WF5vunXgJyqxCqQbEaal4Zd07KKho6VbJIAlsNwLONwbHlWTZOz9cGANp2x7uaMvOH6x1vaROAflMbaFAU3Do3PlThjvM1nBhSQirXC6vLT3E2DWkuYc3S0A+FZAqE7VssNihyuDkiyIwCNkOsXxHcqeoyInT4DG9uVYGMqOv+/ka14f7S1+yPZGJN2J9YATDbWRsk1XrWUUKTUhPy77rEgtMqc314A06IGmdYNXMJPecqfM7VB3QFhB1yVFJ7e5IZ4qFL/neIex2Rni1PIwZocCJcsuqtduE1zBWdhvEXddnpvkokP0bXE96/U8oHU95owSeHwJ5OM8xuxYiUb11IUucLd6uK9IUVJPjbQS197JFXu7kIjLiuqR/Oq3vraOeF7brvClyvIYv5MsxByipZxe0PPO85XrpQDAZO2yLrn4Gp2pQKtqn4yiNSPSubKX0eOFzCq2vUaGWREZpS9dcDmBpaRRaTjyI7NHtWSLaXzLR62tIgcAR6zrlWZLgcnSpWJnNJFqDOYt2Jhgam+H2ONykPVkv20wlDgOqncNby6gdPl62CyZm56PhBaoAgnKox7OTZGnS07sWrG/wASNHC7cOSl5YIu0yyocHLXysDHLai6dL4srubR7eXvMljS519NwWC/2Y8GLSnY8R6XH7ZZ7JzZJa3de4phRVllB08vdkkOXh4HMx4TfXccYZ4XFOkrUBWP6K2NZLuyNdR2PfXUHG+dms/2dCIojno+SWWwpLNzc7ypsC+tKUQtFoiz63t0puttVc6rOs5QtbpHdtV6QGGS7i7eYbNLn7Y5HF5tksdjNm4zYtFmVX71bPz9zu048DwPDzo01xpxZpCHysMaM4WKsLvUqK5yQ6DxZue3NlZ3zzuEWR/dAHZs8UAt9bN1m1FV8LpDZ4qYutRtlcGWxaYVFvCquTYlGOXWL51pAColA3GJG002XKtCQvaAlq1QbLYoZ+7bo3QtK9O31Xt7XWsxur0q0gt3IKha5yQFM19L2GlfL3ivylJ4n6dKZ+8JqjxYRHTBd5NfHym7c+3l7F1HJnUu2al+jQj0siX0v9bW+Mjp3k6g2oHZz0MdSKrdGKBx1VWWu18VlV7PnrQ4Ikkk4fHMVlyogu3yj5ki0jY1RKWk6IGPy1uyuS4snzECIETl2/ENLlJdtodKgtBKlwZSbcVyt+MFcL5NV5qtKKxbietRLA6V0jE5Yn2UrynFoXRH1kWwud3fcX0XBc0Az3jmHpG94orjpXubyeEWRfude157Eq2DOImGgO7gcNzV/0MTrohw2KuykV4xf1XgVlPfznA6jIlGLC9icb9qFF8/dTV6tusAES5+5jJe6JEYNrHaH9SXPxEvLmUuvte3Tue4j2DxFnfQPCTqsxCGhCLqVDiAWrHPWLy/UUeXCjia6QOOzXbw54tS+EwxHdkvTOwj23D03l1NL9NqNlzOxN2kDj0NJrbNcYWU9ZMLcXu3Qq88XfgeoxbakB4xS+SwXT1djLvTAcFdafNn3GL9gAo/CdTnkOnTNbDBX8ueWIBvJml47dRuMh2S1U3VOWRcgNXVwOSx9QU2NE7YgBkVF5oLJ3y7Uis4xZBPq1AhoOMuhjk9Hd0nI1utFl/KAPW5AcVOxLdhqgU3PR8aojqLmrze+n93Wbngl2UbU+yiXWs/dV6N4dJtsQd3IymW3tKzHI6vxxInWdzuxWQ09CrjNHumKoV2FvstzorK8CvyO29yKO6k0wqnUbrBBMdfx0mXF4F5SCdd93N+jQ8GYey6X6FN5nPc6E4gHXirwkqpC8rKWmUzpwyLrAL6xMLvVhSQ6r5z13dhyG4abX5aBI82lTrpwMa8VFHoKrM7HHJPp+8UlC0x53UXnpj/1Lc8p9rbeCXfzWsCk8bBlxxcC22yj8XQ/Fp2wa9uDMm70ftRiMoDotxfOg3S6+IDdB/ekO+zjwFmsAi4nyLumNDfJWkLLLiteN3VdbdDWECjM5aX2IOhSPRD8xSW2YzseLx1q746HnaglqU6a1Fxg72fiZuyrbdGmpqJTaHk1QnmMMbCLOjgrW8kNU3Nc24wezuSZgSVYEOKBlNLL9mBIyYHN62JjGwhWpwTeObFnkPi9avUjvSVwXutLQqgOiKMz9Xhfn07dvt0JmwMN6zjZDb2QLBFS8wV+hRCRkG9X0a06ODhJRY6/2IiRC7iOs9VhK6oKK/grC7ta8sLyMLksDEaUqxAQSj8A6xrmp6hkLYzT+fNBuDbXBdurC3mcn2thU1ha228Oezc1y6ggZfawxLn1zY/idm+eNJ1qwFE6nVn3tr+PuJmSpUA6hXZwC2q5HK78kQxw5W6cNu6FFZLL8kLDMXzlZgOuI/vteMnHm+fTq4Nm3j11wFfHESwPR1HUnKV/WKoF2JoXF+/3+qoM8P5+DJTj7V6nnFDU82XnrrhKoEJZsNu+YLDcFHjJOcy3WEqlRrRhqE17owKc8vE+vFyO8c1kwdLbjCdOEBharbZJW24DhsI3y3SvC1Js8WuJNijZNG/44rLRj+q2742Is4+bTUouxcHIDpi5VAQTzTZFWV0TfFjskpEjr6ywunBLyw6u1kEaXIl0YL8plkAVo2iDtN5a2N/Ma9jr++Qk7tb9sqB3+/Ng5ZlSrtY0FaQ7fZUfa5UURpsUTopZG1iz7i+jul+Lg2TcVd1mSN8tlHV/2zhH697tlaTVgTyndBI5BCjJ7uxDp7EnD5d9ZiUz83MPtLVM9Yxd9YyRMLILZwmmd2yAZ5xnotbmJp52/sJts1Oe3+EgnN6BudsoHCr4+mLuyixSXxTPagzCQa8mqh14VL7fBAbwe3+DIB3fufwgalLkt0KHYItQo69w9N3JnNHxCHWWBebqbyV5vij6QU4NLPe15R130N32Ng8uDA5qVFmfU3vurYlwY8f7uXvvKYdQOpDbMoh6AUeQnYcwgtJvrH2m2czc6kjqpqP1ruCItUtQ+6YW6dN+lEgfo3hMjuuVqJVGsPWu7JEnrl2/Vy4qWG84yiVRwR6i5r6WPd/rj+IR2Xd8MiqhRGOply3ZDh1b1tnt41tom82hYqht1DPj5mLvT/UNk5hKlUgt6o7dCpiGug90JnQupNFshwaszyLGhCLGMcCNgUyWoVmT1sh4pBIytMV3l32EdjyhXbclpy7mB2p+KWivXnvLchwNYdCX4KwYaCkHtWuRtIxh1wqpIIS44Daa1Zbeeqf1JjwrRcQIWuxRNa2x7JlvQXeyQnA5X0LOda5n3I2p6y5ZVJuzskHR01zAKAzZXgLEGwp6VG7DfmT4FgELvh68LgTFRXBujF2bu9y4Fn59HlnTa0V8La/6U2wtSscz2wNAN5pfjs4SI3naifootBV/lQ9Y7FZ8QKMi3F4yl3pRkSlhyBfK2ffV9ZAlS2sl96ArmjnD77QFfTQjBfFBwRVBFrNdE4g+E8rO7ojFq5O/Tbq1vTZPgp2gG/2GZAtuADk+rOQlEpWLcRtbPUAWnqbYNYtjV6GiFdlf0OT1VqDjdaQXmpvOV1G1VGJGZtfZhgf89q7sbAOmvEz7CB55HRdooowDnBPE0e2lanHaJGsOWaC3tXJr+bxlWSYg5WyTV8rNSwSONMVlU0lsyg4NtTPkYBQ73ZY9MsDK2JVONm5vKBBRvbSlh7PU7gLpxBSHuR7vOsxziMB3T8qRmkt0TlGL0MlIBPBqtCuzYlth5CrqbhlxPHqkVNESnpJzaYv3OBOJYtEgputEc0o07s6JQ5D+Ts6JdagrlIKeu7sXoq4dYIROxvFeohZ26nmDOvJzTGl3+KJZt6OBLAZzZ8YS4t3WNlAxRuW1/ZrYbGRf8/zS3pTK4IjGEC8o3dhtLXltERRs5wqudUN5W+bcPkrgZrpFEICdTxfV24QOKFDL3syvLiGl/qauG0lglqWNiyI/sBEnUVupijjtdAOo3x8Y1L2BGwg60z80tr1aLaIOYDtxIAhJMaP0nHNJHuVdia2yXbnttIHxir2rDwoYAIM68dIiufxM8nvjxpPeOVkne6aS8u2NM1F63HNX79A050J1Ft35imXiXRSGIEuMcZ7hcMdPsAghZHGdjRcfQeZYerilxEhGhbezrvSi5SzTQ1nDB8s6XY4V7GajOgcD2dCXDo+5UlksDUozFRqIJ4cuElLmOM/mR+PQib0/oNFpmztn2cDbVQdCtY0r7bbW5kodmeQgWwwWHxdzCg5UVH+PPYRzS2Pv197B57i3D2/TifXr3Plffq48nQT+rx1IPs8O358/PY6cgeV+fsj6/K+r9LcPb5UTQoWeh6510vqvI8r/duT68Z89tZhWj89HtdNjsqF5P55vLH/6ntFbmLlt3VTj1zpP2seh74c3u62nLz3UX1+H228Po9JiOin/JnA6zH08OPja5F+fD5Tfpu8kTI9+gBtaDXhd+q8z6A9v7giDEzr1V4JafAVVMdn5egwyHd1Oz0Hefvt/XFxBec8lAAA= -->
