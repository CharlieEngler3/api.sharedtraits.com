const db = require('../models');
const Question = db.question;
const Answer = db.answer;

exports.getQuestions = async (req, res) => {
    // TODO: Implement me

    const tags = req.body.tags;

    let questions = [];

    for(let i = 0; i < tags.length; i++){
        const question = await Question.find({ $expr: { $in: [tags[i], "$tags"] } });

        questions.push(question);
    }

    res.send(questions);
};

exports.addQuestion = async (req, res) => {
    const question = req.body.question;
    const answerSorting = req.body.answerSorting;
    const questionType = req.body.questionType;
    const questionTags = req.body.questionTags;

    const answers = req.body.answers;
    const answerTags = req.body.answerTags;

    const answerIDs = [];

    for(let i = 0; i < answers.length; i++){
        const newAnswer = new Answer({
            answer: answers[i],
            tags: answerTags[i]
        });

        const newAnswerData = await newAnswer.save();
        answerIDs.push(newAnswerData._id.toString());
    }

    const newQuestion = new Question({
        question: question,
        answerIDs: answerIDs,
        tags: questionTags,
        answerSorting: answerSorting,
        type: questionType
    });

    newQuestion.save().then(() => {
        res.status(201).send("Added Question and Answers");
    }).catch(error => {
        res.status(400).send(error);
    });
};