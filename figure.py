import math

class Line:
    '''
    숫자를 저장하며 set_length, get_length를 통해 length를 입력받는다.
    '''
    def __init__(self, length=1):
        '''
        length가 정수 또는 실수이며 0보다 크면 그 값을 사용, 아니면 1로 초기화한다.
        '''
        if type(length) not in [int, float] or length <= 0:
            self.__length = 1
        else:
            self.__length = length

    def set_length(self, length):
        '''
        길이를 설정하는 메서드이고
        length가 정수 또는 실수이고 0보다 크면 길이를 설정한다.
        '''
        if type(length) in [int, float] and length > 0:
            self.__length = length

    def get_length(self):
        '''
        길이를 반환하는 메서드이다.
        '''
        return self.__length

def area_square(line):
    '''
    정사각형의 면적을 계산하는 함수이고
    인자로 받은 객체가 Line 클래스의 인스턴스가 아니면 0을 반환한다.
    '''
    if not isinstance(line, Line):
        return 0
    else:
        '''
        Line 클래스의 인스턴스이면 길이의 제곱을 반환한다.
        '''
        return line.get_length() ** 2

def area_circle(line):
    '''
    원의 면적을 계산하는 함수
    인자로 받은 객체가 Line 클래스의 인스턴스가 아니면 0을 반환한다.
    '''
    if not isinstance(line, Line):
        return 0
    else:
        '''
        Line 클래스의 인스턴스이면 길이의 제곱에 파이를 곱한 값을 반환한다.
        '''
        return line.get_length() ** 2 * math.pi

def area_regular_triangle(line):
    '''정삼각형의 면적을 계산하는 함수
    인자로 받은 객체가 Line 클래스의 인스턴스가 아니면 0을 반환한다.
    '''
    if not isinstance(line, Line):
        return 0
    else:
        '''
        Line 클래스의 인스턴스이면 길이의 제곱에 (루트3/4)를 곱한 값을 반환한다.
        '''
        return line.get_length() ** 2 * math.sqrt(3) / 4
