
## Rename every file in a folder in an ascending order
useful for when you rip dvd's and need to rename the episodes

```bash
ls | awk '{start=0;system("mv ./" $1 " \"./Simpsons-S01E0"start+NR ".mkv\"")}'
```

## Sed rename files in a directory
```bash
rename 's/find01/replace02/' filestart*
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
## ffmpeg cut a video (no encoding)
```bash
## ss = start t = end
ffmpeg -i input.mp4 -acodec copy -vcodec copy -ss 02:16:30 -t 01:03:10 output.mp4
```
## Find and list files of a specific extension, format them, and write their full path to a text file
```bash
#Useful to make an ffmpeg list of files for concatenation
find /full/path/to/dir -maxdepth 2 -type f -name *.flac -printf "file '%p'\n" >> ~/Downloads/music.txt
```
## Randomize lines in a file
```bash
sort --sort=random input.txt >> output.txt
```
## ffmpeg encode audio
```bash
# -vn is no video
ffmpeg -i input.wav -vn -c:a aac -b:a 128k output.m4a
```
## Encode an mkv keeping all the audio/subtitle streams
`-map 0` maps all streams. `-c copy` sets default to copy.
```bash
ffmpeg -i innie.mkv -map 0 -c copy -c:v libx265 -c:a aac -b:a 128k outie.mkv
```
