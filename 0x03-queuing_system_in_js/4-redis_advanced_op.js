import redis from 'redis';
import util from "util";
const client = redis.createClient();
client.get = util.promisify(client.get);
client.on('error', err => {console.log(`Redis client not connected to the server: ${err}`)});

client.on('connect', () => {console.log("Redis client connected to the server")});

const val = {Portland: 50, Seattle:80, "New York": 20, Bogota:20, Cali:40, Paris:2};
for (const key of Object.keys(val)){
  client.hset("HolbertonSchools", key, val[key], redis.print/*(err, resp, redis.print)=>{
    if (err) throw err;
  }*/);
}
client.hgetall("HolbertonSchools", (err, res)=>{
  if (!err && res){console.log(res)}
});
