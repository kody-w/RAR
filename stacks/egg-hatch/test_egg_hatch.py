"""The app's egg check: a wake egg passes; a changed egg or one with no Brainstem inside is refused."""
import io, unittest, zipfile
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hatch_app as app, rapp1  # noqa: E402

RID = rapp1.mint_rappid("someone", "my-desk")


def egg(extra=None):
    files = {"rappid.json": rapp1.canonical({"schema": "rapp/1", "rappid": RID}).encode(), "soul.md": b"soul\n"}
    files.update(extra or {})
    return rapp1.pack_egg("organism", RID, "2026-11-26T00:00:00.000Z", files=files, payload={})


class EggCheck(unittest.TestCase):
    def test_wake_egg_passes(self):
        self.assertEqual(app.check_egg(egg({"brainstem.py": b"print(1)\n", "skill.md": b"# wake\n"})), (True, "checked"))

    def test_egg_without_a_brainstem_is_refused(self):
        ok, why = app.check_egg(egg())
        self.assertFalse(ok)
        self.assertIn("no Brainstem inside", why)

    def test_changed_egg_is_refused(self):
        blob = egg({"brainstem.py": b"print(1)\n", "skill.md": b"# wake\n"})
        z = zipfile.ZipFile(io.BytesIO(blob))
        out = io.BytesIO()
        with zipfile.ZipFile(out, "w", zipfile.ZIP_STORED) as w:
            for n in z.namelist():
                w.writestr(n, b"print(2)\n" if n == "brainstem.py" else z.read(n))
        self.assertFalse(app.check_egg(out.getvalue())[0])


if __name__ == "__main__":
    unittest.main()
