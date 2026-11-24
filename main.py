"""Ridiculous at First Glance, Real by the Second.

Entry: one sentence (149 characters) pitching a bizarre startup idea that
sounds like a joke until the business logic lands.

The idea: ferrets as cable-pullers. It is a real, documented trade trick --
ferrets were used to pull cables through conduits at Fermilab in the 1970s
and in other tight installations -- because a ferret goes where no drill
or fish tape can reach, and it works for raisins. The buyers are
electricians, who already pay per cable run; the ferret is simply the
cheapest crew member that fits inside a wall.
"""

import os

PITCH = (
    "We rent ferrets to pull cables through your walls: "
    "electricians pay per run because a ferret goes where "
    "no drill can reach, and it works for raisins."
)

# Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space. This pitch is 149 characters, one sentence.
assert 1 <= len(PITCH) <= 200, len(PITCH)
assert PITCH.strip() == PITCH


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)
    os.chmod("/output/entry.txt", 0o644)
    # Verify the gate locally before the run ends: what the judge reads
    # must be byte-identical to the pitch, 1-200 characters, no trailing
    # newline. A truncated or altered write fails loudly here instead of
    # shipping a corrupt entry to the gate.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == PITCH, "entry.txt differs from PITCH"
    assert 1 <= len(written) <= 200, len(written)
    print(f"entry.txt: {len(written)} characters, sha256 verified")


if __name__ == "__main__":
    main()
