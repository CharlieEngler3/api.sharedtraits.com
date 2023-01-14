const dbConfig = require("../config/db.config.js");

const mongoose = require('mongoose');
mongoose.Promise = global.Promise;

const db = {};
db.mongoose = mongoose;
db.url = dbConfig.url;
db.user = require("./user.model.js")(mongoose);
db.question = require("./question.model.js")(mongoose);
db.answer = require("./answer.model.js")(mongoose);

module.exports = db;