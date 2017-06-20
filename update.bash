#!/bin/bash
# Pull in any new feed items into a CSV
# Pass in arguments if you want to scp the channel CSV to prod, like so:
# ./update.bash --feed http://url.com/feed/
while [ "$1" != "" ]; do
    case $1 in
        -f | --feed ) shift
            FEED=$1
            SLUG=$2
            ;;
    esac
    shift
done

if [ -e .source.bash ]; then
    source .source.bash
fi

NEW_CSV="new-$SLUG.csv"
CSV="$SLUG.csv"
head -n 1 $CSV > $NEW_CSV
python recentfeed.py $FEED --output csv --days 1 >> $NEW_CSV
COUNT=`cat $NEW_CSV | wc -l`
if [ $COUNT -gt 1 ]; then
    echo $COUNT
    python addtocsv.py $NEW_CSV $CSV
fi
