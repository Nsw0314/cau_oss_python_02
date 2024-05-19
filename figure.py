"""
'figure' 모듈은 클래스 'Line'과 함수 'area_square',
'area_circle', 'area_regular_triangle'의 기능을 담고있다.   
"""

class Line:
    """
    Line 클래스는 figure모듈 내에 있는 함수들에 매개변수로써
    사용될 객체인 __length의 정보를 설정하고, __length에 접근하기
    위한 메소드 set_length와 get_length를 정의했다.
    """
    def __init__(self, length=1): 
        # 초기 생성 시 __length 필드의 유효성 검사 #
        if isinstance(length, (int, float)) and length > 0:
            self.__length = length
        else:
            self.__length = 1               # 위반 시 기본 값 '1' 적용

    def set_length(self, length):
        # 이후 변경 시 __length 필드의 유효성 검사 #
        previous_length = self.__length     # 이전 값 저장
        if isinstance(length, (int, float)) and length > 0:
            self.__length = length
        else:
            self.__length = previous_length # 위반 시 이전 값 적용

    def get_length(self):
        return self.__length      

def area_square(line):
    """
    정사각형의 넓이를 게산한다.
    Args:
        line: 한 변의 길이
    Retruns:
        int or float: 정사각형의 넓이
    """
    if not isinstance(line, Line):
        return 0 # 매개변수의 타입이 Line 클래스가 아닌 경우 0 반환
    else:
        length = line.get_length()
        return length ** 2

import math
def area_circle(line):
    """
    원의 넓이를 계산한다.
    Args:
        line: 원의 반지름
    Returns:
        int or float: 원의 넓이
    """
    if not isinstance(line, Line):
        return 0 # 매개변수의 타입이 Line 클래스가 아닌 경우 0 반환
    else:
        radius = line.get_length()
        return math.pi * (radius ** 2)

def area_regular_triangle(line):
    """
    정삼각형의 넓이를 계산한다.
    Args:
        line : 한 변의 길이
    Retruns:
        int or float: 정삼각형의 넓이
    """
    if not isinstance(line, Line):
        return 0 # 매개변수의 타입이 Line 클래스가 아닌 경우 0 반환
    else:
        length = line.get_length()
        return (math.sqrt(3) / 4) * (length ** 2)