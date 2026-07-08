import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class StaticRigTests(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        required_paths = [
            "README.md",
            "PROTOCOL.md",
            "rubric/RUBRIC_VERSION.md",
            "fixtures/brake/dev_cases.jsonl",
            "runners/README.md",
            "results/brake/dev/README.md",
            "results/brake/shadow/summary-aggregate.json",
            "verdicts/brake/README.md",
            ".github/workflows/static-validation.yml",
            ".gitignore",
        ]

        for relative_path in required_paths:
            with self.subTest(path=relative_path):
                self.assertTrue((REPO_ROOT / relative_path).is_file())

    def test_readme_contains_leakage_rules(self) -> None:
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")

        for rule in ("R1", "R2", "R3", "R4", "R5"):
            with self.subTest(rule=rule):
                self.assertIn(f"**{rule}**", readme)

        required_terms = [
            "影子集题面",
            "raw-responses.jsonl",
            "summary-aggregate.json",
            "rotating shadow set",
            "build-release-pack.py",
        ]
        for term in required_terms:
            with self.subTest(term=term):
                self.assertIn(term, readme)

    def test_readme_declares_non_certification_boundary(self) -> None:
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn(
            "本仓库一切结果均为诊断/训练性质，不构成 Mindthus 认证",
            readme,
        )

    def test_protocol_preserves_static_delivery_boundary(self) -> None:
        protocol = (REPO_ROOT / "PROTOCOL.md").read_text(encoding="utf-8")

        required_phrases = [
            "逐子进程空 HOME",
            "--fail-on-contamination",
            "generate/judge 分阶段",
            "公开题该病型 n>=3 全绿",
            "影子变体不回退",
            "负例",
            "Patch summary",
            "本次仓库构建不执行 runner",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, protocol)

    def test_dev_cases_jsonl_shape(self) -> None:
        path = REPO_ROOT / "fixtures/brake/dev_cases.jsonl"
        records = [
            json.loads(line)
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]

        self.assertEqual(["EXB-D1", "EXB-D2", "EXB-N1"], [record["id"] for record in records])
        self.assertEqual(3, len(records))

        required_fields = {
            "schema_version",
            "id",
            "pathology",
            "case_type",
            "turns",
            "should_brake",
            "should_trigger",
            "expected_owner",
            "expected_skill",
            "acceptable_skills",
            "scoring",
            "tags",
        }

        for record in records:
            with self.subTest(case=record["id"]):
                self.assertEqual("mindthus-exams-brake-dev-v0.1", record["schema_version"])
                self.assertEqual("brake", record["pathology"])
                self.assertTrue(required_fields.issubset(record.keys()))
                self.assertTrue(record["turns"])
                self.assertTrue(all(turn["role"] == "user" for turn in record["turns"]))
                self.assertEqual({"2", "1", "0"}, set(record["scoring"].keys()))

        positives = [record for record in records if record["case_type"] == "positive"]
        negatives = [record for record in records if record["case_type"] == "near_negative"]
        self.assertEqual(2, len(positives))
        self.assertEqual(1, len(negatives))
        self.assertTrue(all(record["should_brake"] for record in positives))
        self.assertTrue(all(record["should_trigger"] for record in positives))
        self.assertFalse(negatives[0]["should_brake"])
        self.assertFalse(negatives[0]["should_trigger"])
        self.assertEqual(2, len(next(record for record in records if record["id"] == "EXB-D2")["turns"]))

    def test_shadow_results_contain_only_allowed_aggregate_file(self) -> None:
        shadow_dir = REPO_ROOT / "results/brake/shadow"
        files = sorted(path.name for path in shadow_dir.iterdir() if path.is_file())

        self.assertEqual(["summary-aggregate.json"], files)

        aggregate = json.loads((shadow_dir / "summary-aggregate.json").read_text(encoding="utf-8"))
        self.assertEqual("mindthus-exams-shadow-aggregate-v0.1", aggregate["schema_version"])
        self.assertFalse(aggregate["shadow_run_recorded"])
        self.assertEqual([], aggregate["cases"])

    def test_shadow_leakage_guards_are_present(self) -> None:
        gitignore = (REPO_ROOT / ".gitignore").read_text(encoding="utf-8")
        forbidden_patterns = [
            "results/*/shadow/*",
            "!results/*/shadow/summary-aggregate.json",
            "results/*/shadow/prompts/",
            "results/*/shadow/answers/",
            "results/*/shadow/raw-responses.jsonl",
            "results/*/shadow/judge-prompts/",
        ]

        for pattern in forbidden_patterns:
            with self.subTest(pattern=pattern):
                self.assertIn(pattern, gitignore)

    def test_ci_runs_static_validation(self) -> None:
        workflow = (REPO_ROOT / ".github/workflows/static-validation.yml").read_text(
            encoding="utf-8"
        )

        required_terms = [
            "pull_request",
            "push",
            "python3 -m unittest discover -s tests",
        ]
        for term in required_terms:
            with self.subTest(term=term):
                self.assertIn(term, workflow)


if __name__ == "__main__":
    unittest.main()
