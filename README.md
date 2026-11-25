[![make.fun](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![Rank](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/h05meigames2/wifi-story-25nov26/rank.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![Reward](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/h05meigames2/wifi-story-25nov26/reward.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)

# The WiFi Died With Grandma

A Wi-Fi network name that is a joke and a whole story in 26 characters. Grandma was the one person in the house who kept the Wi-Fi alive — she knew the password, she rebooted the router, she called the provider. Now she is gone, the network is named after her, and nobody left in the house knows the password. A stranger scrolling the network list gets the punchline instantly and can fill in the rest: the unplugged router, the family staring at a login screen.

## The program

`main.py` (Python 3, standard library only, no network) holds the name as a single string, validates it (1–32 characters, one line, non-blank), and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

> The WiFi Died With Grandma

## Run locally

```sh
MAKEFUN_OUTPUT_DIR=/tmp/wifi-out python3 main.py
cat /tmp/wifi-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

Built for [make.fun](https://make.fun) — referral: `77v1ce78`
