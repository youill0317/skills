import test from "node:test";
import assert from "node:assert/strict";
import path from "node:path";
import { buildListSkillsResult } from "../src/skills/list-skills.js";

const skillsRoot = path.resolve(process.cwd(), "skills");

test("buildListSkillsResult returns sorted skills with count", async () => {
  const result = await buildListSkillsResult(skillsRoot);

  assert.equal(result.count, result.skills.length);
  assert.ok(result.skills.length >= 5);
  assert.equal(result.warnings.length, 0);

  const ids = result.skills.map((item) => item.id);
  const sorted = [...ids].sort((a, b) => a.localeCompare(b));
  assert.deepEqual(ids, sorted);
  assert.ok(ids.includes("document-qa"));
  assert.ok(ids.includes("document-summary"));
  assert.ok(ids.includes("mcp-search"));
  assert.ok(ids.includes("mcp-obsidian"));
  assert.ok(ids.includes("mcp-skills"));
  assert.ok(ids.includes("mcp-subagent"));
  assert.ok(ids.includes("report-writer"));
  assert.ok(ids.includes("plan-skill"));
  assert.ok(ids.includes("workflow-orchestrator"));

  for (const skill of result.skills) {
    assert.ok(Array.isArray(skill.references));
    for (const referencePath of skill.references) {
      assert.equal(typeof referencePath, "string");
      assert.ok(referencePath.startsWith("references/"));
    }
  }

  const mcpSearch = result.skills.find((item) => item.id === "mcp-search");
  assert.ok(mcpSearch);
  assert.ok((mcpSearch.references ?? []).includes("references/brave.md"));
  assert.ok((mcpSearch.references ?? []).includes("references/scholar.md"));

  const mcpObsidian = result.skills.find((item) => item.id === "mcp-obsidian");
  assert.ok(mcpObsidian);
  assert.ok((mcpObsidian.references ?? []).includes("references/discovery-and-navigation.md"));

  const mcpSkills = result.skills.find((item) => item.id === "mcp-skills");
  assert.ok(mcpSkills);
  assert.ok((mcpSkills.references ?? []).includes("references/run-skill-guide.md"));

  const mcpSubagent = result.skills.find((item) => item.id === "mcp-subagent");
  assert.ok(mcpSubagent);
  assert.ok((mcpSubagent.references ?? []).includes("references/delegate-task.md"));

  const reportWriter = result.skills.find((item) => item.id === "report-writer");
  assert.ok(reportWriter);
  assert.ok((reportWriter.references ?? []).includes("references/research-report.md"));

  const planSkill = result.skills.find((item) => item.id === "plan-skill");
  assert.ok(planSkill);
  assert.ok((planSkill.references ?? []).includes("references/plan-template.md"));
  assert.ok((planSkill.references ?? []).includes("references/decision-rules.md"));

  const workflowOrchestrator = result.skills.find((item) => item.id === "workflow-orchestrator");
  assert.ok(workflowOrchestrator);
  assert.ok((workflowOrchestrator.references ?? []).includes("references/chaining-patterns.md"));
});
