const express = require('express');
const questionTagSuggestionsController = require("../controllers/questionTagSuggestions.controller.js");

const router = express.Router();

router.post('/add', questionTagSuggestionsController.addTagSuggestions);

module.exports = router;