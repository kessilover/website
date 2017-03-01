from django.contrib import admin
from stories.models import Story


class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'summary', 'cover')
    list_filter = ('fandom', 'status')
    search_fields = ('summary', 'title')
    ordering = ('title',)
    def summary(self, story):
        text = story.summary[:40]
        if len(story.summary) > 40 :
            return "%s..." % text
        else :
            return text




admin.site.register(Story, StoryAdmin)

