module.exports = mongoose => {
    const Question = mongoose.model(
        "questions",
        mongoose.Schema({
            question: String,
            answerSorting: String,
            type: String,
            answerIDs: [String],
            tags: [String]
        },
        { timestamps: true })
    );

    return Question;
};