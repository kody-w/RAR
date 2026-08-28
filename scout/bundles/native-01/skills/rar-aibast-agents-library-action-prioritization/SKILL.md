---
name: "rar-aibast-agents-library-action-prioritization"
description: "Prioritizes sales actions and builds daily plans, weekly reviews, and resource allocations from built-in demo deal data."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/action_prioritization", "rar_sha256": "ebd28d87a1c31ff50a12afcab1aa8cfc0d2ae2d7f52bbe2e412d882b605b6d0e", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "AIBAST", "tags": ["b2b", "sales", "action-prioritization", "planning", "resource-allocation"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/action_prioritization`. The original RAPP
agent is preserved byte-for-byte in `action_prioritization_agent.py` and in the RCI capsule.

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

Action Prioritization Agent

Prioritizes sales actions by effort-impact analysis, generates daily
time-blocked plans, produces weekly reviews, and optimizes resource
allocation across enterprise B2B deals. Helps reps focus on the highest-
value activities.

Where a real deployment would call CRM and calendar APIs, this agent
uses a synthetic data layer so it runs anywhere without credentials.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "The prioritization operation",
      "enum": [
        "prioritize_actions",
        "daily_plan",
        "weekly_review",
        "resource_allocation"
      ],
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `action_prioritization_agent.py` and embedded as the fenced Python below (sha256 ebd28d87a1c31ff5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `action_prioritization_agent.py` first:

```bash
python3 action_prioritization_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 action_prioritization_agent.py   # or on stdin
python3 action_prioritization_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Action Prioritization Agent

Prioritizes sales actions by effort-impact analysis, generates daily
time-blocked plans, produces weekly reviews, and optimizes resource
allocation across enterprise B2B deals. Helps reps focus on the highest-
value activities.

Where a real deployment would call CRM and calendar APIs, this agent
uses a synthetic data layer so it runs anywhere without credentials.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent
import json
from datetime import datetime, timedelta

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/action_prioritization",
    "version": "1.0.1",
    "display_name": "Action Prioritization",
    "description": "Prioritizes sales actions and builds daily plans, weekly reviews, and resource allocations from built-in demo deal data.",
    "author": "AIBAST",
    "tags": ["b2b", "sales", "action-prioritization", "planning", "resource-allocation"],
    "category": "b2b_sales",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ═══════════════════════════════════════════════════════════════
# SYNTHETIC DATA LAYER
# ═══════════════════════════════════════════════════════════════

_REP_PROFILE = {
    "name": "Michael Torres",
    "role": "Enterprise Account Executive",
    "quota": 8_000_000,
    "ytd_closed": 3_200_000,
    "pipeline_value": 7_800_000,
    "active_deals": 6,
    "available_hours_per_day": 8,
    "available_hours_per_week": 40,
}

_ACTION_ITEMS = [
    {
        "id": "act-001", "account": "Acme Corporation", "action": "Get champion intro to CTO Sarah Chen",
        "category": "Stakeholder", "impact_score": 95, "effort_hours": 1.0,
        "deadline": "2025-03-15", "deal_value": 2_400_000, "stage": "Proposal",
        "dependencies": ["Champion James Miller available"], "status": "pending",
    },
    {
        "id": "act-002", "account": "Acme Corporation", "action": "Send customized ROI calculator to CFO",
        "category": "Value Prop", "impact_score": 88, "effort_hours": 2.5,
        "deadline": "2025-03-15", "deal_value": 2_400_000, "stage": "Proposal",
        "dependencies": ["Finance team input on TCO model"], "status": "pending",
    },
    {
        "id": "act-003", "account": "Acme Corporation", "action": "Prepare competitor counter-strategy",
        "category": "Competitive", "impact_score": 82, "effort_hours": 1.5,
        "deadline": "2025-03-15", "deal_value": 2_400_000, "stage": "Proposal",
        "dependencies": [], "status": "pending",
    },
    {
        "id": "act-004", "account": "Contoso Ltd", "action": "Schedule renewal discussion with CTO",
        "category": "Retention", "impact_score": 90, "effort_hours": 0.5,
        "deadline": "2025-03-17", "deal_value": 1_100_000, "stage": "Negotiation",
        "dependencies": [], "status": "pending",
    },
    {
        "id": "act-005", "account": "Contoso Ltd", "action": "Deliver expansion proposal",
        "category": "Value Prop", "impact_score": 78, "effort_hours": 3.0,
        "deadline": "2025-03-20", "deal_value": 1_100_000, "stage": "Negotiation",
        "dependencies": ["Product team review"], "status": "in_progress",
    },
    {
        "id": "act-006", "account": "Fabrikam Industries", "action": "Conduct discovery workshop with VP IT",
        "category": "Discovery", "impact_score": 72, "effort_hours": 2.0,
        "deadline": "2025-03-21", "deal_value": 890_000, "stage": "Discovery",
        "dependencies": ["VP IT calendar confirmation"], "status": "pending",
    },
    {
        "id": "act-007", "account": "Fabrikam Industries", "action": "Share production downtime case study",
        "category": "Content", "impact_score": 55, "effort_hours": 0.5,
        "deadline": "2025-03-18", "deal_value": 890_000, "stage": "Discovery",
        "dependencies": [], "status": "pending",
    },
    {
        "id": "act-008", "account": "Northwind Traders", "action": "Initial discovery call with CTO",
        "category": "Discovery", "impact_score": 60, "effort_hours": 1.0,
        "deadline": "2025-03-22", "deal_value": 540_000, "stage": "Qualification",
        "dependencies": [], "status": "pending",
    },
    {
        "id": "act-009", "account": "Acme Corporation", "action": "Update deal forecast in CRM",
        "category": "Admin", "impact_score": 30, "effort_hours": 0.5,
        "deadline": "2025-03-16", "deal_value": 2_400_000, "stage": "Proposal",
        "dependencies": [], "status": "pending",
    },
    {
        "id": "act-010", "account": "General", "action": "Attend weekly pipeline review meeting",
        "category": "Admin", "impact_score": 40, "effort_hours": 1.0,
        "deadline": "2025-03-17", "deal_value": 0, "stage": "N/A",
        "dependencies": [], "status": "pending",
    },
]

_WEEKLY_METRICS = {
    "week_of": "2025-03-10",
    "actions_completed": 12, "actions_total": 18,
    "completion_rate": 0.67,
    "hours_selling": 22, "hours_admin": 8, "hours_meetings": 10,
    "deals_advanced": 3, "deals_stalled": 1,
    "emails_sent": 28, "meetings_held": 8, "calls_made": 15,
    "pipeline_movement": 450_000,
}


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def _priority_score(action):
    """Compute priority from impact, deal value, and deadline proximity."""
    impact = action["impact_score"]
    value_weight = min(30, action["deal_value"] / 100_000)
    # deadline proximity bonus
    deadline_bonus = 0
    if action["deadline"]:
        days_left = 3  # synthetic approximation for urgency
        deadline_bonus = max(0, 20 - days_left * 3)
    return min(100, int(impact * 0.5 + value_weight + deadline_bonus))


def _effort_impact_quadrant(action):
    """Classify into effort-impact quadrant."""
    impact = action["impact_score"]
    effort = action["effort_hours"]
    if impact >= 70 and effort <= 1.5:
        return "Quick Wins"
    if impact >= 70:
        return "Major Projects"
    if effort <= 1.5:
        return "Fill-Ins"
    return "Reconsider"


def _sort_by_priority(actions):
    """Sort actions by computed priority score descending."""
    return sorted(actions, key=lambda a: _priority_score(a), reverse=True)


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class ActionPrioritizationAgent(BasicAgent):
    """
    Prioritizes and schedules sales actions for maximum impact.

    Operations:
        prioritize_actions  - ranked list of all actions by priority
        daily_plan          - time-blocked daily schedule
        weekly_review       - weekly performance review
        resource_allocation - resource utilization analysis
    """

    def __init__(self):
        self.name = "ActionPrioritizationAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "prioritize_actions", "daily_plan",
                            "weekly_review", "resource_allocation",
                        ],
                        "description": "The prioritization operation",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "prioritize_actions")
        dispatch = {
            "prioritize_actions": self._prioritize_actions,
            "daily_plan": self._daily_plan,
            "weekly_review": self._weekly_review,
            "resource_allocation": self._resource_allocation,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"**Error:** Unknown operation `{op}`."
        return handler()

    # ── prioritize_actions ────────────────────────────────────
    def _prioritize_actions(self):
        sorted_actions = _sort_by_priority(_ACTION_ITEMS)

        rows = ""
        for rank, a in enumerate(sorted_actions, 1):
            score = _priority_score(a)
            quadrant = _effort_impact_quadrant(a)
            rows += (
                f"| {rank} | {a['action'][:45]} | {a['account']} | "
                f"{score}/100 | {a['effort_hours']}h | {quadrant} | {a['deadline']} |\n"
            )

        quick_wins = [a for a in sorted_actions if _effort_impact_quadrant(a) == "Quick Wins"]
        total_effort = sum(a["effort_hours"] for a in sorted_actions if a["status"] == "pending")

        return (
            f"**Action Priority List: {_REP_PROFILE['name']}**\n\n"
            f"Total pending actions: {sum(1 for a in _ACTION_ITEMS if a['status'] == 'pending')}\n"
            f"Total effort required: {total_effort:.1f} hours\n"
            f"Quick wins available: {len(quick_wins)}\n\n"
            f"| Rank | Action | Account | Priority | Effort | Quadrant | Deadline |\n|---|---|---|---|---|---|---|\n"
            f"{rows}\n"
            f"**Quick Wins (do first):**\n"
            + "".join(f"- {a['action']} ({a['account']}, {a['effort_hours']}h)\n" for a in quick_wins)
            + f"\nSource: [CRM Actions + Deal Intelligence + Calendar]\n"
            f"Agents: ActionPrioritizationAgent"
        )

    # ── daily_plan ────────────────────────────────────────────
    def _daily_plan(self):
        sorted_actions = _sort_by_priority(_ACTION_ITEMS)
        pending = [a for a in sorted_actions if a["status"] == "pending"]

        schedule = [
            {"time": "8:00 AM", "duration": "30 min", "action": "Review pipeline and prioritize", "type": "Planning"},
            {"time": "8:30 AM", "duration": "60 min", "action": pending[0]["action"] if len(pending) > 0 else "Open block", "type": pending[0]["category"] if len(pending) > 0 else "Free"},
            {"time": "9:30 AM", "duration": "30 min", "action": pending[1]["action"] if len(pending) > 1 else "Open block", "type": pending[1]["category"] if len(pending) > 1 else "Free"},
            {"time": "10:00 AM", "duration": "60 min", "action": pending[2]["action"] if len(pending) > 2 else "Open block", "type": pending[2]["category"] if len(pending) > 2 else "Free"},
            {"time": "11:00 AM", "duration": "30 min", "action": "Email follow-ups and LinkedIn engagement", "type": "Outreach"},
            {"time": "11:30 AM", "duration": "60 min", "action": pending[3]["action"] if len(pending) > 3 else "Open block", "type": pending[3]["category"] if len(pending) > 3 else "Free"},
            {"time": "12:30 PM", "duration": "60 min", "action": "Lunch break", "type": "Break"},
            {"time": "1:30 PM", "duration": "90 min", "action": pending[4]["action"] if len(pending) > 4 else "Open block", "type": pending[4]["category"] if len(pending) > 4 else "Free"},
            {"time": "3:00 PM", "duration": "60 min", "action": pending[5]["action"] if len(pending) > 5 else "Open block", "type": pending[5]["category"] if len(pending) > 5 else "Free"},
            {"time": "4:00 PM", "duration": "60 min", "action": "CRM updates and end-of-day review", "type": "Admin"},
        ]

        sched_rows = ""
        for s in schedule:
            sched_rows += f"| {s['time']} | {s['duration']} | {s['action'][:50]} | {s['type']} |\n"

        selling_hours = sum(1 for s in schedule if s["type"] not in ("Planning", "Admin", "Break", "Free")) * 0.75
        admin_hours = sum(1 for s in schedule if s["type"] in ("Planning", "Admin")) * 0.5

        return (
            f"**Daily Plan: {_REP_PROFILE['name']}**\n\n"
            f"| Time | Duration | Activity | Type |\n|---|---|---|---|\n"
            f"{sched_rows}\n"
            f"**Day Summary:**\n"
            f"- Selling activities: ~{selling_hours:.1f} hours\n"
            f"- Admin/planning: ~{admin_hours:.1f} hours\n"
            f"- Top priority: {pending[0]['action'] if pending else 'N/A'}\n"
            f"- Deals touched: {len(set(a['account'] for a in pending[:6]))}\n\n"
            f"Source: [CRM + Calendar + Action Engine]\n"
            f"Agents: ActionPrioritizationAgent"
        )

    # ── weekly_review ─────────────────────────────────────────
    def _weekly_review(self):
        m = _WEEKLY_METRICS
        quota_pct = _REP_PROFILE["ytd_closed"] / _REP_PROFILE["quota"] * 100
        pipeline_coverage = _REP_PROFILE["pipeline_value"] / (_REP_PROFILE["quota"] - _REP_PROFILE["ytd_closed"])

        selling_pct = m["hours_selling"] / (m["hours_selling"] + m["hours_admin"] + m["hours_meetings"]) * 100

        # Account-level summary
        acct_actions = {}
        for a in _ACTION_ITEMS:
            acct = a["account"]
            if acct not in acct_actions:
                acct_actions[acct] = {"total": 0, "pending": 0, "deal_value": a["deal_value"]}
            acct_actions[acct]["total"] += 1
            if a["status"] == "pending":
                acct_actions[acct]["pending"] += 1

        acct_rows = ""
        for acct, data in sorted(acct_actions.items(), key=lambda x: x[1]["deal_value"], reverse=True):
            acct_rows += f"| {acct} | ${data['deal_value']:,} | {data['total']} | {data['pending']} |\n"

        return (
            f"**Weekly Review: {_REP_PROFILE['name']}**\n"
            f"Week of {m['week_of']}\n\n"
            f"**Performance Summary:**\n\n"
            f"| Metric | Value | Target |\n|---|---|---|\n"
            f"| Actions Completed | {m['actions_completed']}/{m['actions_total']} | 90%+ |\n"
            f"| Completion Rate | {m['completion_rate']:.0%} | 85%+ |\n"
            f"| Selling Hours | {m['hours_selling']}h ({selling_pct:.0f}%) | 60%+ |\n"
            f"| Emails Sent | {m['emails_sent']} | 30+ |\n"
            f"| Meetings Held | {m['meetings_held']} | 10+ |\n"
            f"| Calls Made | {m['calls_made']} | 20+ |\n"
            f"| Deals Advanced | {m['deals_advanced']} | 3+ |\n"
            f"| Deals Stalled | {m['deals_stalled']} | 0 |\n"
            f"| Pipeline Movement | ${m['pipeline_movement']:,} | $500K+ |\n\n"
            f"**Quota Progress:**\n"
            f"- YTD Closed: ${_REP_PROFILE['ytd_closed']:,} ({quota_pct:.0f}% of ${_REP_PROFILE['quota']:,})\n"
            f"- Pipeline: ${_REP_PROFILE['pipeline_value']:,} ({pipeline_coverage:.1f}x coverage)\n\n"
            f"**Account Activity:**\n\n"
            f"| Account | Deal Value | Total Actions | Pending |\n|---|---|---|---|\n"
            f"{acct_rows}\n"
            f"**Recommendations:**\n"
            f"- Increase selling time ratio (currently {selling_pct:.0f}%, target 60%+)\n"
            f"- Address stalled deal: schedule re-engagement within 48 hours\n"
            f"- Prioritize Acme Corporation actions (highest deal value)\n\n"
            f"Source: [CRM Activity + Calendar + Pipeline Analytics]\n"
            f"Agents: ActionPrioritizationAgent"
        )

    # ── resource_allocation ───────────────────────────────────
    def _resource_allocation(self):
        # Time allocation by account (based on deal value weighting)
        accounts_data = {}
        for a in _ACTION_ITEMS:
            acct = a["account"]
            if acct not in accounts_data:
                accounts_data[acct] = {"effort": 0, "deal_value": a["deal_value"], "actions": 0}
            if a["status"] == "pending":
                accounts_data[acct]["effort"] += a["effort_hours"]
                accounts_data[acct]["actions"] += 1

        total_effort = sum(d["effort"] for d in accounts_data.values())
        total_value = sum(d["deal_value"] for d in accounts_data.values() if d["deal_value"] > 0)

        alloc_rows = ""
        for acct, data in sorted(accounts_data.items(), key=lambda x: x[1]["deal_value"], reverse=True):
            effort_pct = data["effort"] / max(total_effort, 1) * 100
            value_pct = data["deal_value"] / max(total_value, 1) * 100 if data["deal_value"] > 0 else 0
            alignment = "Aligned" if abs(effort_pct - value_pct) < 15 else "Under-invested" if effort_pct < value_pct else "Over-invested"
            alloc_rows += (
                f"| {acct} | ${data['deal_value']:,} | {value_pct:.0f}% | "
                f"{data['effort']:.1f}h | {effort_pct:.0f}% | {data['actions']} | {alignment} |\n"
            )

        # Category breakdown
        category_hours = {}
        for a in _ACTION_ITEMS:
            cat = a["category"]
            if cat not in category_hours:
                category_hours[cat] = 0
            if a["status"] == "pending":
                category_hours[cat] += a["effort_hours"]

        cat_rows = ""
        for cat, hours in sorted(category_hours.items(), key=lambda x: x[1], reverse=True):
            pct = hours / max(total_effort, 1) * 100
            cat_rows += f"| {cat} | {hours:.1f}h | {pct:.0f}% |\n"

        weekly_capacity = _REP_PROFILE["available_hours_per_week"]
        utilization = total_effort / weekly_capacity * 100

        return (
            f"**Resource Allocation: {_REP_PROFILE['name']}**\n\n"
            f"**Capacity Overview:**\n"
            f"- Weekly capacity: {weekly_capacity}h\n"
            f"- Pending effort: {total_effort:.1f}h\n"
            f"- Utilization: {utilization:.0f}%\n"
            f"- Status: {'Over-committed' if utilization > 100 else 'Available capacity' if utilization < 80 else 'Well-utilized'}\n\n"
            f"**Allocation by Account:**\n\n"
            f"| Account | Deal Value | Value % | Effort | Effort % | Actions | Alignment |\n|---|---|---|---|---|---|---|\n"
            f"{alloc_rows}\n"
            f"**Allocation by Category:**\n\n"
            f"| Category | Hours | % of Total |\n|---|---|---|\n"
            f"{cat_rows}\n"
            f"**Optimization Recommendations:**\n"
            f"- Allocate effort proportional to deal value\n"
            f"- Automate admin tasks to increase selling time\n"
            f"- Delegate low-impact activities where possible\n\n"
            f"Source: [CRM + Calendar + Capacity Planning]\n"
            f"Agents: ActionPrioritizationAgent"
        )


if __name__ == "__main__":
    agent = ActionPrioritizationAgent()
    for op in ["prioritize_actions", "daily_plan", "weekly_review", "resource_allocation"]:
        print("=" * 60)
        print(agent.perform(operation=op))
        print()
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
