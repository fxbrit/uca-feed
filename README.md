# uca-feed
Feed that allows you to checker wheter an updated version of official [ungoogled-chromium](https://github.com/Eloston/ungoogled-chromium) binaries for Arch is available.


The module scrapes the [website](https://ungoogled-software.github.io/ungoogled-chromium-binaries/) which contains the latest releases, it checks if new binaries are available since the last time you run the module, and if that's the case it returns a link to the download page.

To run simply type:

    python -m uca-feed

Dependencies:
- `bs4`
- `requests`