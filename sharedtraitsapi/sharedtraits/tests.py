# from django.test import TestCase
# from .models import UserAnswerModel
# from .models import QuestionModel

# class UserAnswerModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         UserAnswerModel.objects.create(username='charlieengler')
#         UserAnswerModel.objects.create(questionID=0)
#         UserAnswerModel.objects.create(answer='#squirtsquad')

#     def test_username_content(self):
#         userAnswerModel = UserAnswerModel.objects.get(id=1)
#         expected_object_username = f'{UserAnswerModel.username}'
#         self.assertEquals(expected_object_username, 'charlieengler')

#     def test_questionID_content(self):
#         userAnswerModel = UserAnswerModel.objects.get(id=2)
#         expected_object_questionID = f'{userAnswerModel.questionID}'
#         self.assertEquals(expected_object_questionID, 0)
    
#     def test_answer_content(self):
#         userAnswerModel =UserAnswerModel.objects.get(id=3)
#         expected_object_answer = f'{userAnswerModel.answer}'
#         self.assertEquals(expected_object_answer, '#squirtsquad')

# class QuestionModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         QuestionModel.objects.create(question='Are you #squirtsquad or #creamteam?')
#         QuestionModel.objects.create(answers='[#squirtsquad], [#creamteam]')

#     def test_question_content(self):
#         questionModel = QuestionModel.objects.get(id=1)
#         expected_object_question = f'{QuestionModel.question}'
#         self.assertEquals(expected_object_question, "Are you #squirtsquad or #creamteam?")
    
#     def test_answer_content(self):
#         questionModel = QuestionModel.objects.get(id=2)
#         expected_object_answer = f'{QuestionModel.answers}'
#         self.assertEquals(expected_object_answers, '[#squirtsquad], [#creamteam]')