def valid(result):
    # 주관식 문제의 경우 디폴트를 입력한거 필터링
    if result[3] == "둘 중 하나만 적어주세요!":
        return False
    if result[6] == "힌트 : OOO OO":
        return False
    return True
