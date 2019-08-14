#!/bin/sh

set -e

HOST=(34.68.27.71)
TOKEN=(yJVlvPwQAXbBPUEIKR71)
SLEEP_TIME=10

send=0

while true; do
    curl -v -X POST -d \
        "{\"Temperature\": $((RANDOM%60)),\"Humidity\": $((RANDOM%100)),\"Pressure\": $((RANDOM%100000)),\"CO\": $((RANDOM%10)),\"O3\": $((RANDOM%5)),\"SO2\": $((RANDOM%5)),\"NO2\": $((RANDOM%5)),\"PM1\": $((RANDOM%10)),\"PM10\": $((RANDOM%10)),\"PM25\": $((RANDOM%10))}" \
        $HOST/api/v1/$TOKEN/telemetry --header "Content-Type:application/json" > /dev/null 2>&1
    echo "Send $((send = send + 1)) times"
    sleep $SLEEP_TIME
done