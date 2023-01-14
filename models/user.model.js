module.exports = mongoose => {
    const User = mongoose.model(
        "users",
        mongoose.Schema({
            username: String,
            email: String,
            password: String,
            profileTags: [String],
            questionTags: [String],
            answeredQuestions: [String],
            answers: [String]
        },
        { timestamps: true })
    );

    return User;
};