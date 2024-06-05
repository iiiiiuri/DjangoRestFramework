from rest_framework import serializers

class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    completed = serializers.BooleanField(default=False)
    created_at = serializers.DateTimeField()

    #! RENOMEANDO O CAMPO
    public = serializers.BooleanField(source = 'is_private')

    #! CAMPO DE METODO
    text = serializers.SerializerMethodField(method_name='get_text')

    #! RELACIONAMENTO
    category = serializers.StringRelatedField()

    def get_text(self, obj):
        return f'({obj.title}) - {(obj.description)[0:20]} ...'

    def __str__(self):
        return self.title