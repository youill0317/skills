import test from "node:test";
import assert from "node:assert/strict";
import path from "node:path";
import { listSkillManifests, loadSkill } from "../src/skills/loader.js";

const skillsRoot = path.resolve(process.cwd(), "skills");

test("loadSkill reads frontmatter and body", async () => {
  const skill = await loadSkill(skillsRoot, "document-qa");
  assert.equal(skill.id, "document-qa");
  assert.equal(skill.name, "document-qa");
  assert.ok(skill.description.includes("Answer questions"));
  assert.ok(skill.body.includes("Document QA Workflow"));
});

test("loadSkill reads report-writer metadata and body", async () => {
  const skill = await loadSkill(skillsRoot, "report-writer");
  assert.equal(skill.id, "report-writer");
  assert.equal(skill.name, "report-writer");
  assert.ok(skill.description.includes("structured reports"));
  assert.ok(skill.body.includes("Section Standard"));
});

test("loadSkill reads plan-skill metadata and body", async () => {
  const skill = await loadSkill(skillsRoot, "plan-skill");
  assert.equal(skill.id, "plan-skill");
  assert.equal(skill.name, "plan-skill");
  assert.ok(skill.description.includes("decision-complete execution plans"));
  assert.ok(skill.body.includes("Planning Workflow"));
});

test("loadSkill reads mcp-search metadata and body", async () => {
  const skill = await loadSkill(skillsRoot, "mcp-search");
  assert.equal(skill.id, "mcp-search");
  assert.equal(skill.name, "mcp-search");
  assert.ok(skill.description.includes("mcp_search"));
  assert.ok(skill.body.includes("Tool Families"));
});

test("loadSkill reads workflow-orchestrator metadata and body", async () => {
  const skill = await loadSkill(skillsRoot, "workflow-orchestrator");
  assert.equal(skill.id, "workflow-orchestrator");
  assert.equal(skill.name, "workflow-orchestrator");
  assert.ok(skill.description.includes("multi-skill workflows"));
  assert.ok(skill.body.includes("Common Chains"));
});

test("listSkillManifests returns installed starter skills", async () => {
  const manifests = await listSkillManifests(skillsRoot);
  const ids = manifests.map((item) => item.id);
  assert.ok(ids.includes("document-qa"));
  assert.ok(ids.includes("document-summary"));
  assert.ok(ids.includes("mcp-search"));
  assert.ok(ids.includes("mcp-obsidian"));
  assert.ok(ids.includes("mcp-skills"));
  assert.ok(ids.includes("mcp-subagent"));
  assert.ok(ids.includes("report-writer"));
  assert.ok(ids.includes("plan-skill"));
  assert.ok(ids.includes("workflow-orchestrator"));

  const mcpSearch = manifests.find((item) => item.id === "mcp-search");
  assert.ok(mcpSearch);
  assert.ok(mcpSearch.references.includes("references/brave.md"));
  assert.ok(mcpSearch.references.includes("references/scholar.md"));

  const mcpObsidian = manifests.find((item) => item.id === "mcp-obsidian");
  assert.ok(mcpObsidian);
  assert.ok(mcpObsidian.references.includes("references/read-and-link-tools.md"));

  const mcpSkills = manifests.find((item) => item.id === "mcp-skills");
  assert.ok(mcpSkills);
  assert.ok(mcpSkills.references.includes("references/reference-loading-and-scripts.md"));

  const mcpSubagent = manifests.find((item) => item.id === "mcp-subagent");
  assert.ok(mcpSubagent);
  assert.ok(mcpSubagent.references.includes("references/task-writing-guide.md"));

  const reportWriter = manifests.find((item) => item.id === "report-writer");
  assert.ok(reportWriter);
  assert.ok(reportWriter.references.includes("references/research-report.md"));

  const planSkill = manifests.find((item) => item.id === "plan-skill");
  assert.ok(planSkill);
  assert.ok(planSkill.references.includes("references/plan-template.md"));
  assert.ok(planSkill.references.includes("references/decision-rules.md"));

  const workflowOrchestrator = manifests.find((item) => item.id === "workflow-orchestrator");
  assert.ok(workflowOrchestrator);
  assert.ok(workflowOrchestrator.references.includes("references/chaining-patterns.md"));
});
