import test from "node:test";
import assert from "node:assert/strict";
import path from "node:path";
import { buildListSkillsResult } from "../src/skills/list-skills.js";

const skillsRoot = path.resolve(process.cwd(), "skills");

test("buildListSkillsResult returns sorted skills with count", async () => {
  const result = await buildListSkillsResult(skillsRoot);

  assert.equal(result.count, result.skills.length);
  assert.ok(result.skills.length >= 2);
  assert.equal(result.warnings.length, 0);

  const ids = result.skills.map((item) => item.id);
  const sorted = [...ids].sort((a, b) => a.localeCompare(b));
  assert.deepEqual(ids, sorted);
  assert.ok(ids.includes("document-qa"));
  assert.ok(ids.includes("document-summary"));
});
