const SlackBot = require('slackbots');
const axios = require('axios');

const bot = new SlackBot({
    token: 'xoxb-573614227475-574805061319-I0lOdj9ehaf2ZhtPlADQzFrM',
    name: 'jokebot'
});

// Start Handler
bot.on('start', () => {
    const params = {
        icon_emoji: ':smiley:'
    };

    bot.postMessageToChannel(
        'general',
        'Get Ready To Laugh With @Jokebot!',
        params
    );
});

// Error Handler
bot.on('error', err => console.log(err));

// Message Handler
bot.on('message', data => {
    if (data.type !== 'message') {
        return;
    }
    handleMessage(data.text);
});

// Response to data
function handleMessage(message) {
    // If message contains 'chucknorris'.
    if (message.includes(' chucknorris')) {
        chuckJoke();
    } else if (message.includes(' yomama')) {
        yoMamaJoke();
    }
}

// Tell a Chuck Norris Joke
function chuckJoke() {
    axios.get('http://api.icndb.com/jokes/random/').then(res => {
        const joke = res.data.value.joke;
        const params = {
            icon_emoji: ':laughing:'
        };

        bot.postMessageToChannel('general', `Chuck Norris: ${joke}`, params);
    });
}

// Tell a yo mama Joke
function yoMamaJoke() {
    axios.get('http://api.yomomma.info/').then(res => {
        const joke = res.data.joke;
        const params = {
            icon_emoji: ':laughing:'
        };

        bot.postMessageToChannel('general', `Yo Mama: ${joke}`, params);
    });
}
