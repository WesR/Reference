
# Rename every file in a folder in an ascending order
useful for when you rip dvd's and need to rename the episodes

```bash
ls | awk '{start=0;system("mv ./" $1 " \"./Simpsons-S01E0"start+NR ".mkv\"")}'
```

# Encode a folder with ffmpeg and output into a folder called encodes
useful for when you take ripped dvd output and need to encode it
```bash
mkdir encodes; for i in *.mkv; do ffmpeg -i "$i" "./encodes/${i%.*}.mkv"; echo done
```
