
## Rename every file in a folder in an ascending order
useful for when you rip dvd's and need to rename the episodes

```bash
ls | awk '{start=0;system("mv ./" $1 " \"./Simpsons-S01E0"start+NR ".mkv\"")}'
```

## Encode a folder with ffmpeg and output into a folder called encodes
useful for when you take ripped dvd output and need to encode it
```bash
mkdir encodes; for i in *.mkv; do ffmpeg -i "$i" "./encodes/${i%.*}.mkv"; done

# for interlaced video with h265 and audio passthrough
mkdir encodes; for i in *.mkv; do ffmpeg -i "$i" -vf yadif -c:v libx265 -preset slow -c:a copy "./encodes/${i%.*}.mkv"; done
```

## Remove the encoded title in a mkv
useful for removing the title from a ripped dvd
```bash
for i in *.mkv ; do mkvpropedit "$i" --edit info --set "title="; done
```
## Imagemagick convert tiff to jpg
```bash
mkdir compress; for i in *.tif; do convert "$i" "./compress/${i%.tif}.jpg"; done
```
