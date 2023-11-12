const fs = require('fs');
const Papa = require('papaparse');
const { AxieGene } = require("agp-npm/dist/axie-gene");
const { Transform } = require('stream');

// Function to decode hex genes using AxieGene
const decodeAxieGenes = (hexGene) => {
  try {
    if (typeof hexGene === 'undefined' || hexGene === null) {
      console.error('Hex gene is undefined or null.');
      return {}; // Return an empty object or a default value indicating an error
    }
    const axieGene = new AxieGene(hexGene);

    return {
      mouth: {
        d: axieGene.mouth.d.name,
        r1: axieGene.mouth.r1.name,
        r2: axieGene.mouth.r2.name
      },
      eyes: {
        d: axieGene.eyes.d.name,
        r1: axieGene.eyes.r1.name,
        r2: axieGene.eyes.r2.name
      },
      ears: {
        d: axieGene.ears.d.name,
        r1: axieGene.ears.r1.name,
        r2: axieGene.ears.r2.name
      },
      horn: {
        d: axieGene.horn.d.name,
        r1: axieGene.horn.r1.name,
        r2: axieGene.horn.r2.name
      },
      back: {
        d: axieGene.back.d.name,
        r1: axieGene.back.r1.name,
        r2: axieGene.back.r2.name
      },
      tail: {
        d: axieGene.tail.d.name,
        r1: axieGene.tail.r1.name,
        r2: axieGene.tail.r2.name
      }
    };
  } catch (error) {
    console.error('An error occurred while decoding genes:', error);
    return {}; // Return an empty object or a default value indicating an error
  }
};

// Function to convert gene objects to a string format for CSV
const geneObjectToString = (geneObject) => {
  return Object.entries(geneObject).map(([part, genes]) => {
    return `${part}_d: ${genes.d}, ${part}_r1: ${genes.r1}, ${part}_r2: ${genes.r2}`;
  }).join(', ');
};

// Function to read the CSV, decode the genes, and write back to a new CSV
const convertGenesInCsv = (inputFilePath, outputFilePath) => {
    const readStream = fs.createReadStream(inputFilePath, 'utf8');
    const writeStream = fs.createWriteStream(outputFilePath, 'utf8');
    let lineCounter = 0;
  
    const transformStream = new Transform({
      writableObjectMode: true,
      transform(row, encoding, callback) {
        if (lineCounter === 0) {
          // Write headers
          this.push(Papa.unparse([row], {header: true}) + '\r\n');
        } else {
          row.childGenes = geneObjectToString(decodeAxieGenes(row.childGenes));
          row.matronGenes = geneObjectToString(decodeAxieGenes(row.matronGenes));
          row.sireGenes = geneObjectToString(decodeAxieGenes(row.sireGenes));
          this.push(Papa.unparse([row], {header: false}) + '\r\n');
        }
  
        lineCounter++;
        if (lineCounter % 50000 === 0) {
          console.log(`Processed ${lineCounter} lines.`);
        }
        callback();
      }
    });
  
    readStream
      .pipe(Papa.parse(Papa.NODE_STREAM_INPUT, {header: true}))
      .pipe(transformStream)
      .pipe(writeStream)
      .on('finish', () => {
        console.log(`Updated CSV saved to ${outputFilePath}`);
      })
      .on('error', (error) => {
        console.error('An error occurred:', error);
      });
  };
  
  // Usage
  convertGenesInCsv('goodcpgenes.csv', 'updated_goodcpgenes.csv');