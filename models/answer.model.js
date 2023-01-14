module.exports = mongoose => {
    const Answer = mongoose.model(
        "answers",
        mongoose.Schema({
            answer: String,
            tags: [String]
        },
        { timestamps: true })
    );

    return Answer;
};