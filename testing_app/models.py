from django.db import models
from django.utils.translation import gettext_lazy as _


class TestSet(models.Model):
    """
    модель набора тестовых вопросов
    """
    title = models.CharField(_('title'), max_length=250)
    description = models.TextField(_('description'), max_length=2500)
    slug = models.SlugField(_('slug'), max_length=120)

    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)
    sort_order = models.PositiveIntegerField(_('sort order'), default=0)

    class Meta:
        verbose_name = _("Test Set")
        verbose_name_plural = _("Test Sets")
        ordering = ('sort_order',)

    def __str__(self):
        return self.title[:50]


class TestQuestion(models.Model):
    """
    модель вопроса
    """
    question = models.TextField(_('question'))
    slug = models.SlugField(_('slug'), max_length=120)

    several_correct_answers = models.BooleanField(_('several correct'), default=False)
    test_set = models.ForeignKey(TestSet, on_delete=models.CASCADE, related_name='questions',
                                 verbose_name=_('test set'))
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)
    sort_order = models.PositiveIntegerField(_('sort order'), default=0)

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ('sort_order', )
        unique_together = ('test_set', 'question')

    def __str__(self):
        return self.question[:50]


class Answer(models.Model):
    """
    модель ответа на вопрос
    """
    answer = models.TextField(_('answer'))
    is_correct = models.BooleanField(_('is correct'), default=False)
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE, related_name='answers',
                                 verbose_name=_('question'))
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)
    sort_order = models.PositiveIntegerField(_('sort order'), default=0)

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ('sort_order', )
        unique_together = ('question', 'answer')

    def __str__(self):
        return self.answer[:50]
