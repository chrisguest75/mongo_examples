import { logger } from './logger.js'
import * as dotenv from 'dotenv'
import minimist from 'minimist'
import { MongoClient } from "mongodb";

/*
Entrypoint
*/
export async function main(args: minimist.ParsedArgs) {
  logger.trace('TRACE - level message')
  logger.debug('DEBUG - level message')
  logger.info('INFO - level message')
  logger.warn('WARN - level message')
  logger.error('ERROR - level message')
  logger.fatal('FATAL - level message')
  logger.info({ node_env: process.env.NODE_ENV })
  logger.info({ 'node.version': process.version })
  const uri = process.env.MONGODB_URI || '';
  const client = new MongoClient(uri);

  try {
    // connect to your Atlas deployment
    const database = client.db("sample_mflix");
    const collection = database.collection("embedded_movies");

    // define your Atlas Vector Search index
    /*const index = {
      name: "vector_index",
      type: "vectorSearch",
      definition: {
        "fields": [
          {
            "type": "vector",
            "numDimensions": 1536,
            "path": "plot_embedding",
            "similarity": "dotProduct",
            "quantization": "scalar"
          }
        ]
      }
    }

    // run the helper method
    const result = await collection.createSearchIndex(index);
    logger.info(`New search index named ${result} is building.`);
    */
    // wait for the index to be ready to query
    logger.info("Polling to check if the index is ready. This may take up to a minute.")
    let isQueryable = false;
    const cursor = collection.listSearchIndexes();
    for await (const index of cursor) {
      logger.info(`Index name: ${index.name}`);

    }
  } finally {
    await client.close();
  }
}

process.on('exit', async () => {
  logger.warn('exit signal received')
  //process.exit(1)
})

process.on('uncaughtException', async (error: Error) => {
  logger.error(error)
  // for nice printing
  console.log(error)
  process.exit(1)
})

process.on('unhandledRejection', async (reason, promise) => {
  logger.error({
    promise: promise,
    reason: reason,
    msg: 'Unhandled Rejection',
  })
  console.log(reason)
  process.exit(1)
})

// load config
dotenv.config()
logger.info(`Pino:${logger.version}`)
const args: minimist.ParsedArgs = minimist(process.argv.slice(2), {
  string: ['ssmName'],
  boolean: ['verbose', 'ssmRead', 'ssmWrite', 'throwError'],
  default: { verbose: true, throwError: false, ssmRead: false, ssmWrite: false, ssmName: 'testssmdocument' },
})

try {
  await main(args)
  process.exit(0)
} catch (error) {
  logger.error(error)
  process.exit(1)
}



