#!/usr/bin/env bash

mongosh "mongodb://ffprobe:ffprobepassword@0.0.0.0:27017/ffprobe" ./scripts/export-all-queries.js

