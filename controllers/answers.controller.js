const mongoose = require('mongoose');
const db = require('../models');
const Answer = db.answer;

exports.getAnswer = async (req, res) => {
    const id = req.params.id;

    Answer.findOne({ _id: mongoose.Types.ObjectId(id) }).then(answer => {
        res.send(answer);
    });
};