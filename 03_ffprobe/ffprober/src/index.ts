import path = require("path");
import fs = require("fs");
import { logger } from "./logger";
import Probe from "./probe";
import Find from "./find";
import { findSourceMap } from "module";

async function analyse(fullPath: string): Promise<string>  {
    return new Promise((resolve, reject) => {
        logger.info(`Analyse ${fullPath}`)
        const outPath = "./out"
        let probe = new Probe(fullPath);

        let output = probe.analyze().then((output) => {
            let outFile = `${probe.md5}.json`
            let fullOutPath = path.join(outPath, outFile)
            
            // write to outpath
            if (!fs.existsSync(outPath)) {
                fs.mkdirSync(outPath);
            }
    
            fs.writeFileSync(fullOutPath, output)
            logger.info(`Created ${fullOutPath}`);    
            
        })
    });
}

async function main() {
    const basePath = "/Volumes/videoshare/bigbuckbunny-hls"
    let find = new Find();
    logger.info(`Find files in ${basePath}`)
    find.findSync(basePath, ".*", true, analyse)
}

main()
