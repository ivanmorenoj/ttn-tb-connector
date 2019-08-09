#!/bin/sh

while true; do
curl -v -X POST -d \
    "{\"temperature\": $((RANDOM%60)),\"humidity\": $((RANDOM%100)),\"pressure\": $((RANDOM%100000)),\"co\": $((RANDOM%10)),\"o3\": $((RANDOM%5)),\"so2\": $((RANDOM%5)),\"no2\": $((RANDOM%5)),\"pm1\": $((RANDOM%10)),\"pm10\": $((RANDOM%10)),\"pm25\": $((RANDOM%10))}" \
    ivan28823.sytes.net/api/v1/Evz8jfpa63K7pDOmkvOB/telemetry --header "Content-Type:application/json" > /dev/null 2>&1
    sleep 10;
done