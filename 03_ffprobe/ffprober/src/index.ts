import fs = require("fs");
import md5File from 'md5-file';
import path = require("path");
import { logger } from "./logger";
import Probe from "./probe";

function getFilesizeInBytes(file: string) {
    const stats = fs.statSync(file);
    const fileSizeInBytes = stats.size;
    return fileSizeInBytes;
}

async function main() 
{
    const basePath = "/Volumes/videoshare"
    const file = "elephant-dreams-hls/stream_2/data183.ts"
    const outPath = "./out"

    let fullPath = path.join(basePath, file)

    logger.info(`Analyse ${fullPath}`)

    let probe = new Probe();
    let output = await probe.analyzeStreams(fullPath)
    let probedata = JSON.parse(output);
    let gop = await probe.analyzeGOP(fullPath)

    // merge gop and filename into video stream
    let video = probedata.streams.filter((stream: any) => stream.codec_type == "video")
    video[0]["gop"] = gop

    // merge md5 of the file
    const md5 = md5File.sync(fullPath)
    const size = getFilesizeInBytes(fullPath)

    let final = {
        file: fullPath,
        md5: md5,
        size: size,
        ...probedata
    }

    console.log(final)

    // write to outpath
    if (!fs.existsSync(outPath)) {
        fs.mkdirSync(outPath);
    }

    let fullOutPath = path.join(outPath, "output.json")
    fs.writeFile(fullOutPath, JSON.stringify(final, null, "\t"), function(err) {
        if (err) {
            logger.error(err);
        } 
        logger.info(`Created ${fullOutPath}`);
    });
}

main()
