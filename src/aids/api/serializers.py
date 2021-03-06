from rest_framework import serializers

from aids.models import Aid


class ArrayField(serializers.ListField):
    child = serializers.CharField()

    def __init__(self, choices, *args, **kwargs):

        self.repr_dict = dict(choices)
        return super().__init__(*args, **kwargs)

    def to_representation(self, obj):

        representation = [self.repr_dict[choice] for choice in obj]
        return representation


class AidSerializer(serializers.ModelSerializer):

    backers = serializers.StringRelatedField(many=True)
    perimeter = serializers.StringRelatedField()
    mobilization_steps = ArrayField(Aid.STEPS)
    targeted_audiances = ArrayField(Aid.AUDIANCES)
    aid_types = ArrayField(Aid.TYPES)
    destinations = ArrayField(Aid.DESTINATIONS)
    recurrence = serializers.CharField(source='get_recurrence_display')

    class Meta:
        model = Aid
        fields = ('name', 'backers', 'description', 'eligibility', 'perimeter',
                  'mobilization_steps', 'url', 'application_url',
                  'targeted_audiances', 'aid_types', 'destinations',
                  'start_date', 'predeposit_date', 'submission_deadline',
                  'subvention_rate', 'contact_email', 'contact_phone',
                  'contact_detail', 'recurrence')
