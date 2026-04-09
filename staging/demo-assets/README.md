# Demo Assets — Agent Conversion Examples

## Pillar 1: n8n → RAPP → Copilot Studio

### Workflow: "Auto Categorise Outlook Emails with AI"
- **Source**: [awesome-n8n-templates](https://github.com/enescingoz/awesome-n8n-templates)
- **File**: `staging/demo-assets/n8n_outlook_email_categorizer.json`
- **Complexity**: 36 nodes, 26 connections
- **What it does**:
  - Monitors Microsoft Outlook inbox
  - Loops through emails in batches
  - Sends each email to an AI Agent (Ollama/LLM) for categorization
  - Routes categorized emails to different Outlook folders (Switch node → 6+ category targets)
  - Handles errors gracefully with catch nodes
  - Parses markdown responses, extracts JSON classifications
- **Why it's perfect for the demo**:
  - Uses **Microsoft Outlook** (not Gmail) — audience will relate
  - Has an **AI Agent node** — shows competitor already uses agent patterns
  - **36 nodes** is visually impressive when you show the n8n canvas
  - The conversion to a single RAPP `perform()` method is a clear win
  - Side-by-side: n8n canvas (complex) vs. one .py file (simple)

### Demo flow:
1. Show the n8n workflow in browser (36 node canvas)
2. Export the JSON
3. Feed into RAPP transpiler → single .py file
4. Feed into Copilot Studio transpiler → MCS skill
5. Side-by-side: same email in, same categorization out

---

## Pillar 1b: OpenClaw → RAPP → Copilot Studio

### Agent: OpenClaw "QuickBooks Bookkeeper"
- **Source**: [openclawmarketplace.ai/agents/quickbooks-bookkeeper](https://openclawmarketplace.ai/agents/quickbooks-bookkeeper)
- **What it does**:
  - Autonomous bookkeeping for QuickBooks Online
  - Auto-categorizes transactions
  - Monthly reconciliation
  - Financial reports, invoice tracking, receipt matching
  - AR/AP alerts, sales tax summaries, 1099 tracking
- **Powered by**: Claude (Anthropic) — `anthropic/claude-opus-4-6`
- **Price**: $79/mo on OpenClaw

### Why it's perfect:
- **Anthropic/Claude-powered** — clearly a competitor platform
- **Finance use case** — enterprise-relevant, not a toy
- **$79/mo subscription** → RAPP agent is free and open-source
- The message: "This costs $79/mo on their platform. On ours, it's a single .py file you own forever."

### Demo flow:
1. Show OpenClaw marketplace in browser → QuickBooks Bookkeeper
2. Show their agent config (YAML/JSON)
3. Feed into RAPP transpiler → single .py file with __manifest__
4. Feed into Copilot Studio transpiler → MCS skill
5. "Same capabilities. Zero subscription. You own the code."

### Alternative: OpenClaw "DevOps Engineer"
- **Source**: [openclawmarketplace.ai/agents/devops-engineer](https://openclawmarketplace.ai/agents/devops-engineer)
- GitHub + Docker + CI/CD monitoring + PR review + vulnerability scanning
- $199/mo — even more dramatic cost comparison
- More technical audience might prefer this one

---

## Prep Notes

### OpenClaw agent config format
OpenClaw agents use `openclaw.json` config:
```json
{
  "agents": {
    "defaults": {
      "model": { "primary": "anthropic/claude-opus-4-6" }
    }
  }
}
```
Skills are defined as YAML/markdown files. For the demo, create a representative config that mirrors the QuickBooks Bookkeeper capabilities.

### n8n export format
The JSON file is already downloaded at `staging/demo-assets/n8n_outlook_email_categorizer.json`. Import into a local n8n instance to show the visual canvas during the demo.
