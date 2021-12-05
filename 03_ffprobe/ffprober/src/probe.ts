import { spawnSync } from "child_process";
import { logger } from "./logger";

//ffprobe -v quiet -print_format json=compact=1 -show_streams /Volumes/videoshare/sintel/sintel-x264-5.1.mp4 
//ffprobe -v quiet -select_streams v -show_frames -of csv -show_entries frame=key_frame,pict_type,best_effort_timestamp_time -i /Volumes/videoshare/sintel/sintel-x264-5.1.mp4

export default class Probe {
    constructor() {}

    async probeStreams(file: string) {
        let options = ["-v", "quiet", "-print_format", "json=compact=1", "-show_streams", file];
        logger.info({ options: "jp2a " + options.join(" ") });
        const spawnResult = spawnSync("ffprobe", options, {
          cwd: process.cwd(),
          env: process.env,
          stdio: "pipe",
          encoding: "utf-8",
        });
        //logger.info({"stdout":spawnResult.output});
        if (spawnResult.status !== 0) {
          throw new Error(`ffprobe exited with ${spawnResult.status}`);
        } else {
          return spawnResult.output;
        }
    }

    async analyze(inFile: string): Promise<string> {
        let out = await this.probeStreams(inFile);
    
        let realOut = "Error";
        if (out != null) {
           realOut = out[1] || ""
        }
    
        return new Promise((resolve, reject) => {
          resolve(realOut);
        });
      }    
}