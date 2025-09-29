from rest_framework import serializers
from accounts.models import User
from .models import Student,Standards, Section,ParentStudent,Attendance


class StudentRegistrationSerializers(serializers.ModelSerializer):
    name=serializers.CharField(write_only=True)
    email=serializers.EmailField(write_only=True)
    password=serializers.CharField(write_only=True)
    standard_id=serializers.IntegerField(write_only=True)
    section_id=serializers.IntegerField(write_only=True)

    class Meta:
        model=Student
        fields=['id','name','email','password','standard_id','section_id']

    def create(self,validated_data):

        user=User.objects.create(
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['name'],
            role='STUDENT'
        )
        user.set_password(validated_data['password'])
        user.save()

        standard=Standards.objects.get(id=validated_data['standard_id'])
        section=Section.objects.get(id=validated_data['section_id'])


        student=Student.objects.create(
            user=user,
            standard=standard,
            section=section
        )
        return student

    

   
    
    def to_representation(self, instance):
        return {
            "student_id": instance.id,
            "name": instance.user.first_name,
            "email": instance.user.email,
            "standard": instance.standard.names if instance.standard else None,
            "section": instance.section.name if instance.section else None,
            "message": "Student registered successfully"
        }
    

class LinkParentSerializer(serializers.ModelSerializer):
    parent_id=serializers.IntegerField()
    student_id=serializers.IntegerField()

    class Meta:
        model=ParentStudent
        fields=['id','parent_id','student_id']


    def validate(self,data):
        try:
            parent=User.objects.get(id=data['parent_id'],role="parent")

        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid parent_id or user is not a parent")
        
        try:
            student=Student.objects.get(id=data['student_id'])

        except Student.DoesNotExist:
            raise serializers.ValidationError("Invalid student_id")
        
        return data
    
    def create(self,validated_data):
        parent=User.objects.get(id=validated_data['parent_id'])
        student=Student.objects.get(id=validated_data['student_id'])
        link,created=ParentStudent.objects.get_or_create(parent=parent,student=student)

        return link
    
    def to_representation(self, instance):
        return{
            "link_id":instance.id,
            "student":instance.student.user.first_name,
            "parent":instance.parent.first_name,
            "message":"Parent linked to student successfully"
        }
    

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Section
        fields=["id","name","standard"]


class StandardSerializer(serializers.ModelSerializer):
    sections=SectionSerializer(many=True,read_only=True)
    class Meta:
        model=Standards
        fields=["id","names","sections"]





class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance
        fields=["id","student","date","status","marked_by"]
        read_only_fields=["marked_by"]

class AttendanceMarkSerializer(serializers.Serializer):
    student_id=serializers.IntegerField()
    date=serializers.DateField()
    status=serializers.ChoiceField(choices=[("PRESENT","Present"),("ABSENT","Absent")])

class AttendanceDailySerializer(serializers.ModelSerializer):
    student_name=serializers.CharField(read_only=True)
    standard=serializers.CharField(read_only=True)
    section=serializers.CharField(read_only=True) 

    class Meta:
        model=Attendance
        fields=["date","status","student_name","standard","section"]

class AttendanceSummarySerializer(serializers.Serializer):
    student_name=serializers.CharField()
    standard=serializers.CharField()
    section=serializers.CharField()
    total_present=serializers.IntegerField()
    total_absent=serializers.IntegerField()
    attendance_percentage=serializers.CharField()