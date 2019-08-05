import os
os.chdir("C:/Users/musicman/Desktop/learn_python/effective_python")

# Use descriptors for resuable @property methods
# The big problem with @property is reuse. The methods it decorates cannot
# be reused for multiple attributes of the same class, nor can be used by
# unrelated classes.


class Homework(object):
    def __init__(self):
        self._grade = 0

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._grade = value


galileo = Homework()
galileo.grade = 95
print(galileo.grade)


class Exam(object):
    # This quickly gets tedius. Each section of the exam reuires adding a new
    # @property and related validation.
    def __init__(self):
        self._writing_grade = 0
        self._math_grade = 0

    @staticmethod
    def _check_grade(value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')

    @property
    def writing_grade(self):
        return self._writing_grade

    @writing_grade.setter
    def writing_grade(self, value):
        self._check_grade(value)
        self._writing_grade = value

    @property
    def math_grade(self):
        return self._math_grade

    @math_grade.setter
    def math_grade(self, value):
        self._check_grade(value)
        self._math_grade = value


# A better solution: descriptor.
# The descriptor protocol defines how attribute access is interpreted.
# A descriptor class can provide __get__ and __set__ methods that let you
# reuse the grade validation behavior without any boilerplate. Descriptors
# allow you to use the same logic for different attributes in the same class.


class Grade(object):
    def __get__(*args, **kwargs):
        pass

    def __set__(*args, **kwargs):
        pass


class Exam(object):
    # Class attributes
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


# Mechanism of descriptor:
# 1. When an Exam instance(exam) doesn't have the attribute named math_grade,
# Python will fall back to the Exam class's atribute instead.
# 2. If this class attribute is an object with __get__ and __set__ method
# defined, Python will assume you want to follow the descriptor protocol: when
# accessing the attribute, __get__ is called; when setting the attribute,
# __get__ is called.


exam = Exam()
exam.math_grade = 40  # => Exam.__dict__['math_grade'].__set__(exam, 40)
print(exam.math_grade)  # => Exam.__dict__["math_grade"].__get__(exam, Exam)


class Grade(object):
    def __init__(self):
        self._value = 0

    def __get__(self, instance, instance_type):
        return self._value

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._value = value


class Exam(object):
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


first_exam = Exam()
first_exam.writing_grade = 82
first_exam.science_grade = 99
print('Writing', first_exam.writing_grade)
print('Science', first_exam.science_grade)

# However, accessing these attributes on multiple Exam instances is unexpected. 
# THe problem is that: a single Grade instance is stored across all Exam 
# instances for the class attribute writing_grade. The Grade instance for this
# attribute is constructed only once in the program lifetime when the Exam
# class is first defined, not each time an Exam instance is created. In short,
# multiple Exam instances are sharing the same Grqde instance.
second_exam = Exam()
second_exam.writing_grade = 75
print('Second', second_exam.writing_grade, 'is right')
print('First ', first_exam.writing_grade, 'is wrong')


# Solution: Make Grade class to keep track of its value for each unique Exam
# instance by saving them in a dict. 
class Grade(object):
    def __init__(self):
        self._values = {}

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._values[instance] = value


# The above implementation is simple and works well, except it leaks memory. 
# The _value dict would hold a reference to every instance of Exam evey passed 
# to __set__ over the lifetime of the program. This prevents cleanup by garbage
# collector.
# A fix would be using Python's weakref built-in module, which provides a
# WeakKeyDictionary that can replace the simple dictionary.
class Grade(object):
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._values[instance] = value

