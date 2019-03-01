from django.db import models

from django.template.defaultfilters import slugify

from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length = 150)
	slug = models.SlugField(unique = True)
	text = models.TextField()
	created_on = models.DateTimeField(auto_now_add = True)
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	
	def __unicode__(self):
		return self.title
		
	@models.permalink
	def get_absolute_url(self):
		return('blog_post_detail',(),
			{
				'slug' : self.slug,
			})
	def save(self, *args, **kwargs):
		if not_self.slug:
			self.slug = slugify(self.title)
		super(Post,self).save(*args, **kwargs)

class comment(models.Model):
	name = models.CharField(max_length = 42)
	email = models.EmailField(max_length = 75)
	website = models.URLField(max_length = 200, null=True, blank = True)
	text = models.TextField()
	post = models.ForeignKey(Post,on_delete=models.CASCADE)
	created_on = models.DateTimeField(auto_now_add = True)
	
	def __unicode__(self):
		return self.text
		
