const express = require('express');
const answerController = require('../controllers/answers.controller.js');

const router = express.Router();

router.get('/:id', answerController.getAnswer);

module.exports = router;