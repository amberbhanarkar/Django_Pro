from django.db import models

from django.contrib.auth.models import user
from django.template.defaultfilters import slugify

class PublishedArticlesManager(models.Manager):
	def get_query_set(self):
		return super(PublishedArticlesManager, self).get_query_set().filter(is_published=True)
		
class Article(models.Model):
	"""Represents a Wiki article"""
	title = models.CharField(max_length = 150)
	slug = models.SlugField(max_length = 50, unique = True)
	text = models.TextField(help_text="Formatted using ReST")
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	is_published = models.BooleanField(default = False, verbose_name"Publish?") 
	created_on = models.DAteTimeField(auto_now_add = True)
	objects = models.Manager()
	published = PublishedArticlesManager()
	
	def __unicode__(self):
		return self.title
	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super(Article, self).save(*args, **kwargs)
	@models.permalink
	def get_absolute_url(self):
		return ('wiki_article_detail', (), {'slug':self.slug})
		
class Edit(models.Model):
	"""Stores on edit session"""
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	editor = models.ForeignKey(User, on_delete = models.CASCADE)
	edited_on = models.DateTimeField(auto_add_now = True)
	summary = models.CharField(max_length = 100)
	
	class Meta:
		ordering = ['-edited_on']
		
	def __unicode__(self):
		return "%s - %s - %s" % (self.summary, self.editor, self.edited_on)
	
	@models.permalink
	def get_absolute_url(self):
		return ('wiki_edit_detail', self.id)
	
