#!/bin/bash



cat cols-pitch.tsv > pitches.tsv
for current_date in $(./drange 2013-10-01 180)
  do
    echo "Scraping day ${current_date}"
    for i in $(mlb games --date "${current_date}" | cut -f 1)
      do
        echo "    Scraping game #${i}..."
        mlb game --date "$current_date" --pitches "${i}" >> pitches.tsv
        # mlb game --date yesterday --hits "${i}" >> hits.tsv
      done
  done
