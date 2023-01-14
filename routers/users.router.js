const express = require('express');
const userController = require('../controllers/users.controller.js');

const router = express.Router();

router.get('/:id', userController.getUser);
router.get('/delete/:id', userController.deleteUser);
router.get('/tags/:id', userController.getUserQuestionTags);

router.get('/answered-questions/:id', userController.getAnsweredQuestions);
router.post('/submit-answer', userController.submitAnswers);

router.post('/register', userController.register);
router.post('/login', userController.login);

module.exports = router;