from __future__ import annotations

import csv
import importlib
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifest.tsv"


class CatalogTest(unittest.TestCase):
    @staticmethod
    def manifest_rows() -> list[dict[str, str]]:
        with MANIFEST.open(encoding="utf-8", newline="") as stream:
            return list(csv.DictReader(stream, delimiter="\t"))

    def test_manifest_has_204_unique_solutions(self) -> None:
        rows = self.manifest_rows()
        self.assertEqual(204, len(rows))
        self.assertEqual(
            ["problem_number", "relative_path", "title"],
            list(rows[0]),
        )
        self.assertEqual(204, len({row["problem_number"] for row in rows}))
        self.assertEqual(204, len({row["relative_path"] for row in rows}))

    def test_every_manifest_module_exists_and_imports(self) -> None:
        for row in self.manifest_rows():
            relative_path = Path(row["relative_path"])
            self.assertTrue((ROOT / relative_path).is_file(), relative_path)
            module_name = ".".join(relative_path.with_suffix("").parts)
            with self.subTest(problem=row["problem_number"], module=module_name):
                importlib.import_module(module_name)


if __name__ == "__main__":
    unittest.main()
