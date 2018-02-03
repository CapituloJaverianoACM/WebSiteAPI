from django.contrib import admin
from .models import *

admin.site.register(Contest)
admin.site.register(Member)
admin.site.register(Team)
admin.site.register(Award, AwardAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(Tutorial)
admin.site.register(Activity)
admin.site.register(Project)
# admin.site.register(TeamContest)
# admin.site.register(TutorialFile)
# admin.site.register(ActivityFile)
# admin.site.register(ActivityMember)
# admin.site.register(ProjectFile)
# admin.site.register(ProjectMember)
# admin.site.register(TeamMember)
