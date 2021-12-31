#!/usr/bin/env bash

# export all 
#mongosh "mongodb://ffprobe:ffprobepassword@0.0.0.0:27017/ffprobe" ./scripts/export-all-queries.js

# export one
mongosh "mongodb://ffprobe:ffprobepassword@0.0.0.0:27017/ffprobe" ./scripts/export-one-query.js
