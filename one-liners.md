
# Rename every file in a folder in an ascending order
useful for when you rip dvd's and need to rename the episodes

```bash
ls | awk '{start=0;system("mv ./" $1 " \"./Simpsons-S01E0"start+NR ".mkv\"")}'
```
