# gitdown
Parse git logs and output them to a markdown file


## To Use
1. Clone the project
```bash
git clone https://github.com/austinmccalley/gitdown.git
```

2. Change directory to your project
```bash
cd ~/code/myawesomeproejct/
```

3. Run ``src/main.py`` with the optional filename
```bash
python3 ~/code/gitdown/src/main.py changelog.md
```

## Example Output


[1e4191](https://github.com/austinmccalley/gitdown/commit/1e4191964a5605848abc93f165183f043952297e) - Initial commit

[03eb63](https://github.com/austinmccalley/gitdown/commit/03eb63edd5e712f757932c2e4bc211298d0fbacb (origin/master, origin/HEAD, master)) - Not using Node.js

[dc1699](https://github.com/austinmccalley/gitdown/commit/dc1699cfbe59541e304e45ada435aac78913d777) - Get hash and message of commits

[93b701](https://github.com/austinmccalley/gitdown/commit/93b701bb854854dc2f454067d3424247a0fc507e) - Output markdown file based off of commit message and specify output file

*Powered by [gitdown](https://github.com/austinmccalley/gitdown)*