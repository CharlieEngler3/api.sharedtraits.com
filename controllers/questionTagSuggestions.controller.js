const db = require('../models');
const QuestionTagSuggestions = db.questionTagSuggestions;

exports.addTagSuggestions = (req, res) => {
    const questionID = req.body.questionID;
    const question = req.body.question;
    const tags = req.body.tags;

    const newSuggestion = new QuestionTagSuggestions({
        questionID: questionID,
        question: question,
        tags: tags,
        addressed: false
    });

    newSuggestion.save().then(() => {
        res.status(201).send("Successfully added tag suggestions");
    }).catch(error => {
        res.status(400).send(error);
    });
};