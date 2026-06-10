from __future__ import annotations

from pypresence import Presence
import time

CLIENT_ID = "1243023497962328115"

def main() -> None:
    rpc = Presence(CLIENT_ID)
    rpc.connect()
    try:
        rpc.update(state="TEST RP", details="Testing Rich Presence")
        print("Rich Presence set to: TEST RP")
        time.sleep(8)
    finally:
        try:
            rpc.clear()
            rpc.close()
        except Exception:
            pass

if __name__ == "__main__":
    main()
