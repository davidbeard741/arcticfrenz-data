import { readJSON, writeJSON } from 'https://deno.land/x/flat/mod.ts';

const filename = Deno.args[0];
const json = await readJSON(filename);

const timeSeries = json["Time Series (Daily)"];
const data = Object.entries(timeSeries).map(([date, entry]) => ({
  time: date,
  open: parseFloat(entry["1. open"]),
  high: parseFloat(entry["2. high"]),
  low: parseFloat(entry["3. low"]),
  close: parseFloat(entry["4. close"])
}));

data.sort((a, b) => new Date(a.time) - new Date(b.time));

const newFile = 'sentries-postprocessed.json';
await writeJSON(newFile, data);
console.log('Wrote post-processed file: ' + newFile);
