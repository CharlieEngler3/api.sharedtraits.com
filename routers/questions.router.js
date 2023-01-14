const express = require('express');
const questionController = require('../controllers/questions.controller.js');

const router = express.Router();

router.post('', questionController.getQuestions);
router.post('/add', questionController.addQuestion);

module.exports = router;