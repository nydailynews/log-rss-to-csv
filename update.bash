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

DATE=`date +'%Y-%m-%d'`
NEW_CSV="archive/new-$SLUG.csv"
CSV="archive/$SLUG-$DATE.csv"

cat header > $NEW_CSV
python recentfeed.py $FEED --output csv --days 1 >> $NEW_CSV
COUNT=`cat $NEW_CSV | wc -l`
if [ $COUNT -gt 1 ]; then
    echo $COUNT
    python addtocsv.py $NEW_CSV $CSV
fi
