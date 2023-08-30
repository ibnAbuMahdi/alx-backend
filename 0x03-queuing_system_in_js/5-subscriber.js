import redis from 'redis';
import util from "util";
const client = redis.createClient();
client.get = util.promisify(client.get);
client.on('error', err => {console.log(`Redis client not connected to the server: ${err}`)});

client.on('connect', () => {console.log("Redis client connected to the server")});

const subscriber = client;

//  subscriber.connect();

  subscriber.on('message', (channel, message) => {
	  console.log(message); // 'message'
   	if (message === "KILL_SERVER") {
          subscriber.unsubscribe();
	  subscriber.quit();
	}
  });

subscriber.subscribe('holberton school channel');
