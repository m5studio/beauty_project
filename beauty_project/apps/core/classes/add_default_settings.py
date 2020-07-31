from django.contrib.auth.models import Group


class AddDefaultSettings:
    def createGroups(self):
        groups = ['Manager', 'Salon', 'Client']
        for group in groups:
            try:
                gr = Group.objects.get(name=group)
                print(f"Group {gr.name} already exists")
            except Group.DoesNotExist:
                gr = Group(name=group)
                gr.save()
                print(f"Group {gr.name} created!")

    def addSettings(self):
        self.createGroups()