def doc_practice():
    """함수에 대한 설명을 넣는 Docstring(Documentation String)을 연습해보는 함수입니다."""
    print('PEP 8에서는 """를 Docstring에 사용하길 권장합니다.\n')


print(doc_practice.__doc__)
doc_practice()
help(doc_practice)  # help에 함수를 넣으면 함수의 이름, 매개변수, 독스트링을 도움말 형태로 출력
