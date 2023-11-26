const kafka = require('./client')
const axios = require('axios');
const makeRequest = async () => {
    try {
        const producer = kafka.producer()
        await producer.connect()
        const response = await axios.get('https://api.datos.gob.mx/v1/precio.gasolina.publico');
        console.log(response.data.results);
        const prices = response.data.results.map((price) => ({
            regular: price.regular? price.regular: 0,
            premium: price.premium? price.premium: 0,
            diesel: price.diesel? price.diesel: 0,
            calle: price.calle,
        }));
        await producer.send({
            topic: 'test',
            messages: [
                { value: JSON.stringify(prices) },
            ],
        });
        console.log('info enviada');
        await producer.disconnect()
    } catch (error) {
        console.error(error);
    }
};
let time = 1;
const temporizador = async () => {
    console.log(time);
    if (time >= 15) {
        time = 0;
    }
    time++;
}
console.log('iniciando');
setInterval(makeRequest, 15000);
setInterval(temporizador, 1000);

/*
async function main() {
    const producer = kafka.producer()

    await producer.connect()

    for (let i = 0; i < 10; i++) {
        await producer.send({
            topic: 'gasolina',
            messages: [
                { value: `mensajon ${i}` },
            ],
        })

        console.log(`producing message ${i}`)
    }
    getWeatherData();
    await producer.disconnect()

    console.log('done.')
}*/

/*
async function getWeatherData() {
    try {
        const response = await axios.get('https://api.datos.gob.mx/v1/precio.gasolina.publico');
        console.log(response.data.results);
    } catch (error) {
        console.error(error);
    }
    
}*/


//getWeatherData();
//main()