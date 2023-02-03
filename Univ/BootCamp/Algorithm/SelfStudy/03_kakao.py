# 카톡 친구 이름과 카톡 횟수를 입력하면 자동으로 위치를 찾아 삽입하는 프로그램

def find_and_insert_data(friend, k_count):
    find_position = -1
    for i in range(0, len(kakao_talk)):
        pair = kakao_talk[i]
        if k_count >= pair[1]:
            find_position = i
            break
            if find_position == -1:
                find_position = len(kakao_talk)

    insert_data(find_position, (friend, k_count)) # 매개 값으로 ()묶어 튜플 생성


def insert_data(position, friend):
    if position < 0 or position > len(kakao_talk):
        print("Out of range!")
        return

    kakao_talk.append(None)

    for i in range(len(kakao_talk)-1, position, -1):
        kakao_talk[i] = kakao_talk[i-1]

    for i in range(0, len(kakao_talk)):
        if i == position:
            kakao_talk[position] = friend


kakao_talk = [('다현', 200), ('정연', 150), ('쯔위', 90), ('사나', 30), ('지효', 15)]


if __name__ == "__main__":
    while True:
        data = input("신규 친구 이름 : ")
        count = int(input("카톡 횟수 : "))
        find_and_insert_data(data, count)
        print(kakao_talk)
