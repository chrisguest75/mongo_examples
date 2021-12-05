
const fs = require('fs');
const path = require('path');
import { FileInfoResult } from "prettier";
import { logger } from "./logger";

export default class Find {
    constructor() {}

    findSync(folder: string, pattern: string, recurse: boolean, callback: (file: string) => void) {
        try {
            let files = fs.readdirSync(folder)

            for (let i = 0; i < files.length; i++) {
                let file = files[i]                
                let relative = path.join(folder, file)
                let fullpath = path.resolve(relative)
                let stat = fs.statSync(fullpath);
                let directory = stat.isDirectory()
                if (directory) {
                    if (recurse) {
                        this.findSync(relative, pattern, recurse, callback)
                    } else {
                        logger.child({"directory":directory}).info(fullpath)
                    }
                } else {
                    if (path.basename(fullpath).match(pattern)) {
                        logger.child({"size":stat.size, "directory":directory}).info(fullpath)
                        callback(fullpath)                
                        logger.debug(`Processed ${folder}`)
                    }
                }
            }
        }
        catch (error) {
            logger.error("Failed to list directory", error)        
            throw error
        }
    }
}