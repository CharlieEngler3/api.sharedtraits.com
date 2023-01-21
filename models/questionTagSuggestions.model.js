module.exports = mongoose => {
    const QuestionTagSuggestions = mongoose.model(
        "question-tag-suggestions",
        mongoose.Schema({
            questionID: String,
            question: String,
            tags: [String],
            addressed: Boolean
        },
        { timestamps: true })
    );

    return QuestionTagSuggestions;
};