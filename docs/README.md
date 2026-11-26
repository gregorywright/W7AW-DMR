# docs/

Reference material used for fact-checking. Baofeng's manual is **not committed** because it is Baofeng's copyrighted document.
To download it and make the text copy that the agent notes refer to, run:

```sh
curl -L -o docs/Baofeng_DM-32UV_User_Manual_20250210.pdf \
  https://baofeng.s3.amazonaws.com/Baofeng_DM-32UV_User_Manual_20250210.pdf
pdftotext -layout docs/Baofeng_DM-32UV_User_Manual_20250210.pdf docs/manual.txt
```

The screen-icon table is on PDF pages 12–13 (manual §4.3). The icons are images, so render those pages
with `pdftoppm -r 300 -png -f 13 -l 14 docs/Baofeng_DM-32UV_User_Manual_20250210.pdf build/manual/p`.
