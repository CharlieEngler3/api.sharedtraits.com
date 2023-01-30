const db = require('../models');
const Question = db.question;
const Answer = db.answer;

exports.getQuestionsByTag = async (req, res) => {
    const tags = req.body.tags;

    let questionList = [];

    for(let i = 0; i < tags.length; i++){
        const questions = await Question.find({ $expr: { $in: [tags[i], "$tags"] } });

        for(let j = 0; j < questions.length; j++){
            questionList.push(questions[j]);
        }
    }

    res.send(questionList);
};

exports.getQuestionByQuestion = (req, res) => {
    const question = req.params.question;

    Question.findOne({ question: { $regex: question, $options: "i" } }).then(fetchedQuestion => {
        res.send(fetchedQuestion);
    });
};

exports.addQuestion = async (req, res) => {
    const question = req.body.question;
    const answerSorting = req.body.answerSorting;
    const questionType = req.body.questionType;
    const questionTags = req.body.questionTags;

    const answers = req.body.answers;
    const answerTags = req.body.answerTags;

    const answerIDs = questionType == "Text Input" ? "placeholder" : [];

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

exports.updateQuestion = async (req, res) => {
    const questionID = req.body.questionID;
    const question = req.body.question;
    const questionTags = req.body.questionTags;
    const answerSorting = req.body.answerSorting;
    const questionType = req.body.questionType;

    // TODO: Check which answers were added by cross referencing the given answerIDs
    // TODO: Check for changes in the answer tags
    const answerIDs = req.body.answerIDs;
    const existingAnswers = [];
    const answers = req.body.answers;
    const answerTags = req.body.answerTags;

    for(let i = 0; i < answerIDs.length; i++){
        const existingAnswer = await Answer.findOne({ _id: answerIDs[i] });
    
        existingAnswers.push(existingAnswer.answer);
    }

    for(let i = 0; i < answers.length; i++){
        if(!existingAnswers.includes(answers[i])){
            const newAnswerTags = answerTags[i] != null ? answerTags[i] : [];

            const newAnswer = new Answer({
                answer: answers[i],
                tags: newAnswerTags
            });

            const newAnswerData = await newAnswer.save();
            answerIDs.push(newAnswerData._id.toString());
        }
    }

    for(let i = 0; i < answerIDs.length; i++){
        const answer = await Answer.findOne({ _id: answerIDs[i] });
        const newAnswerTags = answerTags[i] != null ? answerTags[i] : [];
        const parsedAnswerTags = [];

        newAnswerTags.map(answerTag => {
            if(answerTag.length > 0){
                parsedAnswerTags.push(answerTag);
            }
        })

        answer.answer = answers[i];
        answer.tags = parsedAnswerTags;
        answer.save();
    }

    const parsedQuestionTags = [];
    questionTags.map(questionTag => {
        if(questionTag.length > 0){
            parsedQuestionTags.push(questionTag);
        }
    });

    const existingQuestion = await Question.findOne({ _id: questionID });
    existingQuestion.question = question;
    existingQuestion.answerIDs = answerIDs;
    existingQuestion.tags = parsedQuestionTags;
    existingQuestion.answerSorting = answerSorting;
    existingQuestion.type = questionType;
    existingQuestion.save().then(() => {
        res.status(200).send("Question Updated Successfully");
    }).catch(error => {
        res.status(400).send(error);
    });
};

exports.deleteQuestionAndAnswers = (req, res) => {
    const questionID = req.params.id;

    Question.findOne({ _id: questionID }).then(async question => {
        const answerIDs = question.answerIDs;

        for(let i = 0; i < answerIDs.length; i++){
            await Answer.deleteOne({ _id: answerIDs[i] });
        }

        Question.deleteOne({ _id: questionID }).then(() => {
            res.status(200).send("Question Deleted Successfully");
        }).catch(error => {
            res.status(400).send(error);
        });
    }).catch(error => {
        res.status(400).send(error);
    });
};