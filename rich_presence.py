"""Simple Discord Rich Presence script using pypresence.

Usage examples:
  # using CLI args
  python rich_presence.py --client-id YOUR_CLIENT_ID --lyrics "Line 1|Line 2|Line 3"

  # or use .env with DISCORD_CLIENT_ID=... and run
  python rich_presence.py --lyrics "Line 1|Line 2"

Notes:
  - Requires Discord Desktop app running on the same machine.
  - Client ID is the Application ID from Developer Portal (no user token).
"""

from __future__ import annotations

import argparse
import time
from typing import Iterable

from dotenv import load_dotenv
import os

try:
    from pypresence import Presence
except Exception as e:
    raise SystemExit("Missing dependency pypresence. Install from requirements.txt")


def split_lyrics(text: str) -> list[str]:
    parts = [part.strip() for part in text.replace("|", "\n").splitlines()]
    return [p for p in parts if p]


def rotate(iterable: Iterable[str]) -> Iterable[str]:
    while True:
        for x in iterable:
            yield x


def main() -> None:
    load_dotenv()

    parser = argparse.ArgumentParser()
    parser.add_argument("--client-id", help="Discord Application (Client) ID", default=os.getenv("DISCORD_CLIENT_ID"))
    parser.add_argument("--lyrics-file", default="lyrics.txt", help="Path to lyrics file")
    parser.add_argument("--delay", type=float, default=15.0, help="Seconds between updates")
    parser.add_argument("--details", default="Dating", help="Details field in presence")
    args = parser.parse_args()

    if not args.client_id:
        raise SystemExit("Missing client id. Provide --client-id or set DISCORD_CLIENT_ID in .env")

    try:
        with open(args.lyrics_file, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        raise SystemExit(f"Lyrics file not found: {args.lyrics_file}")

    if not lines:
        raise SystemExit("No lyrics found in file")

    rpc = Presence(args.client_id)
    rpc.connect()

    try:
        for line in rotate(lines):
            rpc.update(state=line, details=args.details)
            time.sleep(args.delay)
    except KeyboardInterrupt:
        pass
    finally:
        try:
            rpc.clear()
            rpc.close()
        except Exception:
            pass


if __name__ == "__main__":
    main()
