// RAPP workflows - a GitHub Copilot CLI extension that registers every workflow saved by the RAPP
// DynamicWorkflow agent (~/.rapp/workflows/library/*.json) as a native Copilot Dynamic Workflow in every new
// Copilot session, so a workflow is never lost with the session that authored it.
// Written by dynamic_workflow_agent.py (action install_copilot). Safe to delete; the library stays.
import { defineWorkflow, joinSession } from "@github/copilot-sdk/extension";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";

const home = process.env.RAPP_WORKFLOWS_HOME || path.join(os.homedir(), ".rapp", "workflows");
const library = path.join(home, "library");
const workflows = [];
let files = [];
try {
  files = fs.readdirSync(library).filter((f) => f.endsWith(".json")).sort();
} catch {
  files = [];
}
for (const f of files) {
  try {
    const w = JSON.parse(fs.readFileSync(path.join(library, f), "utf8"));
    const run = (0, eval)("(" + w.run + "\n)");
    if (typeof run !== "function") throw new TypeError("its run source is not a function expression");
    workflows.push(defineWorkflow({ meta: w.meta, run }));
  } catch (e) {
    process.stderr.write("rapp-workflows: skipped " + f + ": " + ((e && e.message) || e) + "\n");
  }
}
await joinSession({ workflows });
