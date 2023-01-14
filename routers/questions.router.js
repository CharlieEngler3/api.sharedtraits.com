const express = require('express');
const questionController = require('../controllers/questions.controller.js');

const router = express.Router();

router.post('', questionController.getQuestionsByTag);
router.post('/add', questionController.addQuestion);
router.post('/update', questionController.updateQuestion);

router.get('/:question', questionController.getQuestionByQuestion);
router.get('/delete/:id', questionController.deleteQuestionAndAnswers);

module.exports = router;