from django.contrib import admin
from cropalert.models import *


class PlantAdmin(admin.ModelAdmin):
    pass
admin.site.register(Plant,PlantAdmin)

class PestAdmin(admin.ModelAdmin):
    pass
admin.site.register(Pest,PestAdmin)

class PlantPestSusceptibilityAdmin(admin.ModelAdmin):
    pass
admin.site.register(PlantPestSusceptibility,PlantPestSusceptibilityAdmin)

class PesticideAdmin(admin.ModelAdmin):
    pass
admin.site.register(Pesticide,PesticideAdmin)

class PestPlantPesticideRelAdmin(admin.ModelAdmin):
    pass
admin.site.register(PestPlantPesticideRel,PestPlantPesticideRelAdmin)

class CropAdmin(admin.ModelAdmin):
    pass
admin.site.register(Crop,CropAdmin)

class PestIdentificationAdmin(admin.ModelAdmin):
    pass
admin.site.register(PestIdentification,PestIdentificationAdmin)

class PestIdentificacionRequestAdmin(admin.ModelAdmin):
    pass
admin.site.register(PestIdentificacionRequest,PestIdentificacionRequestAdmin)



