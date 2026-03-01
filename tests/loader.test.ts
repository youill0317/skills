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

test("listSkillManifests returns installed starter skills", async () => {
  const manifests = await listSkillManifests(skillsRoot);
  const ids = manifests.map((item) => item.id);
  assert.ok(ids.includes("document-qa"));
  assert.ok(ids.includes("document-summary"));
  assert.ok(ids.includes("research-mode"));
  assert.ok(ids.includes("report-writer"));
  assert.ok(ids.includes("plan-skill"));

  const researchMode = manifests.find((item) => item.id === "research-mode");
  assert.ok(researchMode);
  assert.ok(researchMode.references.includes("references/search-playbook.md"));

  const reportWriter = manifests.find((item) => item.id === "report-writer");
  assert.ok(reportWriter);
  assert.ok(reportWriter.references.includes("references/research-report.md"));

  const planSkill = manifests.find((item) => item.id === "plan-skill");
  assert.ok(planSkill);
  assert.ok(planSkill.references.includes("references/plan-template.md"));
  assert.ok(planSkill.references.includes("references/decision-rules.md"));
});
