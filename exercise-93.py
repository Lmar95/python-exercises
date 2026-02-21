# Exercise 93 — Program to test internet speed
# Requires: speedtest-cli (pip install speedtest-cli)
# ─────────────────────────────────────────────────────────────────────────────

def test_speed():
    try:
        import speedtest
        st = speedtest.Speedtest()
        print("Testing download speed...")
        download = st.download() / 1_000_000   # convert to Mbps
        print("Testing upload speed...")
        upload   = st.upload()   / 1_000_000
        ping     = st.results.ping
        print(f"\nDownload : {download:.2f} Mbps")
        print(f"Upload   : {upload:.2f} Mbps")
        print(f"Ping     : {ping:.2f} ms")
    except ImportError:
        print("speedtest-cli not installed. Run: pip install speedtest-cli")

def main():
    test_speed()

if __name__ == "__main__":
    main()
