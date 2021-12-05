import { logger } from "./logger";
import Probe from "./probe";

async function main() 
{
    logger.info('Hello world!!!!')
    let probe = new Probe();
    const file = "/Volumes/videoshare//elephant-dreams-hls/stream_2/data183.ts"
    let output = await probe.analyze(file)
    console.log(output)
}

main()
