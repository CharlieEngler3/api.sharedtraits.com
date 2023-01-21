const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const userRouter = require('./routers/users.router.js');
const questionRouter = require('./routers/questions.router.js');
const answerRouter = require('./routers/answers.router.js');
const questionTagSuggestions = require('./routers/questionTagSuggestions.router.js');

const app = express();

const corsOptions = {
    origin: "http://localhost:3000"
};

app.use(cors(corsOptions));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.use('/users', userRouter);
app.use('/questions', questionRouter);
app.use('/answers', answerRouter);
app.use('/question-tag-suggestions', questionTagSuggestions);

const PORT = process.env.PORT || 8000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}.`);
});

const db = require("./models");
const { PromiseProvider } = require('mongoose');
db.mongoose.connect(db.url, {
    useNewUrlParser: true,
    useUnifiedTopology: true
}).then(() => {
    console.log("Connected to database.");
}).catch(error => {
    console.log("Cannot connect to the database!", err);
    process.exit();
});